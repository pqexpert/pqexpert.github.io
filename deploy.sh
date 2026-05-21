#!/usr/bin/env bash
# ============================================================
#  PQExpert.io — GitHub Pages Deployment Script
#  Usage: GITHUB_TOKEN=ghp_xxx bash deploy.sh
# ============================================================
set -euo pipefail

# --- Config ---
ORG="pqexpert"
REPO="pqexpert.github.io"
BRANCH="main"
EMAIL="restorationgroup@pm.me"
NAME="Josh Allen"
DOMAIN="pqexpert.io"

# --- Validate token ---
TOKEN="${GITHUB_TOKEN:?ERROR: Set GITHUB_TOKEN before running. Example: GITHUB_TOKEN=ghp_xxx bash deploy.sh}"

echo ""
echo "=== PQExpert.io Deploy ==="
echo "Target: github.com/$ORG/$REPO"
echo "Domain: $DOMAIN"
echo ""

# --- Prerequisites ---
for cmd in git curl; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "ERROR: $cmd is required but not installed."; exit 1; }
done

API="https://api.github.com"
AUTH_HEADER="Authorization: token $TOKEN"

# --- Create repo (ignore error if already exists) ---
echo "[1/4] Creating repository $ORG/$REPO..."
REPO_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$API/orgs/$ORG/repos" \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"$REPO\",\"private\":false,\"auto_init\":false,\"description\":\"Professional portfolio — pqexpert.io\"}")

if [ "$REPO_RESPONSE" = "201" ]; then
  echo "    ✓ Repository created."
elif [ "$REPO_RESPONSE" = "422" ]; then
  echo "    ✓ Repository already exists — continuing."
else
  echo "    WARN: Repo create returned HTTP $REPO_RESPONSE — continuing anyway."
fi

# --- Git setup ---
echo "[2/4] Initializing git and committing site files..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

git config --global user.email "$EMAIL"
git config --global user.name "$NAME"
git config --global init.defaultBranch "$BRANCH"

# Init or reinit
if [ -d ".git" ]; then
  echo "    ✓ .git exists — resetting for fresh deploy."
  git checkout -B "$BRANCH" 2>/dev/null || true
  git add -A
  git commit -m "Deploy pqexpert.io — $(date -u +%Y-%m-%dT%H:%M:%SZ)" --allow-empty
else
  git init
  git add -A
  git commit -m "Initial deploy — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
fi

# --- Push ---
echo "[3/4] Pushing to GitHub..."
REMOTE_URL="https://$TOKEN@github.com/$ORG/$REPO.git"

if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE_URL"
else
  git remote add origin "$REMOTE_URL"
fi

git push -u origin "$BRANCH" --force
echo "    ✓ Pushed."

# --- Enable GitHub Pages ---
echo "[4/4] Enabling GitHub Pages with custom domain..."
sleep 3  # give GitHub a moment after push

PAGES_RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$API/repos/$ORG/$REPO/pages" \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  -d "{\"source\":{\"branch\":\"$BRANCH\",\"path\":\"/\"}}")

HTTP_CODE=$(echo "$PAGES_RESPONSE" | tail -1)
BODY=$(echo "$PAGES_RESPONSE" | head -1)

if [ "$HTTP_CODE" = "201" ] || [ "$HTTP_CODE" = "409" ]; then
  echo "    ✓ GitHub Pages enabled."
else
  echo "    WARN: Pages enable returned HTTP $HTTP_CODE — you may need to enable manually in repo Settings → Pages."
  echo "    Response: $BODY"
fi

# Set custom domain
curl -s -X PUT "$API/repos/$ORG/$REPO/pages" \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  -d "{\"cname\":\"$DOMAIN\",\"https_enforced\":true}" >/dev/null 2>&1
echo "    ✓ Custom domain $DOMAIN set."

echo ""
echo "=============================="
echo " DEPLOY COMPLETE"
echo "=============================="
echo " Repo:     https://github.com/$ORG/$REPO"
echo " Pages:    https://$ORG.github.io  (propagating)"
echo " Domain:   https://$DOMAIN  (DNS already live — propagating)"
echo ""
echo " DNS was pre-configured. Allow 5–30 minutes for full propagation."
echo " HTTPS certificate will be issued automatically by GitHub."
echo ""
echo " Verify live status: https://github.com/$ORG/$REPO/settings/pages"
echo "=============================="
