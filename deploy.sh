#!/usr/bin/env bash
# PQExpert.io — safe GitHub Pages publish helper
#
# Normal production path:
#   branch -> pull request -> Site quality green -> merge to main -> Pages publish
#
# This helper validates a clean local main branch and performs a normal
# fast-forward push. It intentionally does NOT create repositories, change
# GitHub Pages settings, change DNS, inject tokens into remotes, or force-push.

set -euo pipefail

REPO="pqexpert/pqexpert.github.io"
BRANCH="main"
DOMAIN="pqexpert.io"

command -v git >/dev/null 2>&1 || { echo "ERROR: git is required"; exit 1; }
command -v python >/dev/null 2>&1 || { echo "ERROR: python is required"; exit 1; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ ! -d .git ]; then
  echo "ERROR: deploy.sh must be run from a clone of $REPO"
  exit 1
fi

CURRENT_BRANCH="$(git branch --show-current)"
if [ "$CURRENT_BRANCH" != "$BRANCH" ]; then
  echo "ERROR: expected branch '$BRANCH', found '$CURRENT_BRANCH'."
  echo "Use the pull-request workflow to merge changes before publishing."
  exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
  echo "ERROR: working tree is not clean. Commit/review changes through a PR first."
  exit 1
fi

if [ ! -f CNAME ] || [ "$(tr -d '\r\n' < CNAME)" != "$DOMAIN" ]; then
  echo "ERROR: CNAME is missing or does not equal '$DOMAIN'."
  exit 1
fi

echo "=== PQExpert.io pre-publish validation ==="
echo "Repository: $REPO"
echo "Branch:     $BRANCH"
echo "Domain:     $DOMAIN"
echo

python scripts/check_site.py

echo

echo "Fetching origin and checking divergence..."
git fetch origin "$BRANCH"

LOCAL_SHA="$(git rev-parse HEAD)"
REMOTE_SHA="$(git rev-parse "origin/$BRANCH")"
BASE_SHA="$(git merge-base HEAD "origin/$BRANCH")"

if [ "$LOCAL_SHA" = "$REMOTE_SHA" ]; then
  echo "main is already synchronized with origin. No push needed."
elif [ "$BASE_SHA" != "$REMOTE_SHA" ]; then
  echo "ERROR: local main is not a fast-forward of origin/main."
  echo "Pull/reconcile normally; do not force-push production history."
  exit 1
else
  echo "Pushing fast-forward main..."
  git push origin "$BRANCH"
fi

echo

echo "Source publish step complete."
echo "Next checks:"
echo "  1. Confirm the GitHub 'Site quality' run for main is green."
echo "  2. Confirm repository CNAME and Pages settings still target $DOMAIN."
echo "  3. Verify https://$DOMAIN after GitHub Pages propagation."
echo

echo "Recovery runbook: docs/DEPLOYMENT_RECOVERY.md"
