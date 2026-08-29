#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
fixture_root="$(mktemp -d)"

cleanup() {
    find "$fixture_root" -depth -delete
}
trap cleanup EXIT

mkdir -p "$fixture_root/scripts" "$fixture_root/docs" "$fixture_root/appendix" "$fixture_root/examples"
cp "$script_dir/generate-search-index.sh" "$script_dir/generate_search_index.py" "$fixture_root/scripts/"
printf '%s\n' \
    '# Search "quotes" safely' \
    '' \
    '> A quoted summary stays valid JSON.' \
    '' \
    '## Stable heading' \
    '## Stable heading' \
    '**Search term**' \
    > "$fixture_root/docs/guide.md"
printf '%s\n' \
    '# Community resources' \
    '' \
    '### TweetClaw: X/Twitter search with Xquik' \
    > "$fixture_root/appendix/community.md"

bash "$fixture_root/scripts/generate-search-index.sh" >/dev/null
cp "$fixture_root/search-index.json" "$fixture_root/first-index.json"
bash "$fixture_root/scripts/generate-search-index.sh" >/dev/null

cmp "$fixture_root/first-index.json" "$fixture_root/search-index.json"
cmp "$fixture_root/search-index.json" "$fixture_root/search-index-expanded.json"

python3 - "$fixture_root/search-index.json" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as index_file:
    entries = json.load(index_file)

assert len(entries) == 3

entries_by_url = {entry["url"]: entry for entry in entries}
guide = entries_by_url["/docs/guide.html"]
assert guide["title"] == 'Search "quotes" safely'
assert guide["category"] == "docs"
assert guide["content"].startswith('Search "quotes" safely Stable heading Search term ')

community = entries_by_url["/appendix/community.html"]
assert community["category"] == "appendix"
assert "TweetClaw" in community["content"]
assert "Twitter" in community["content"]
assert "Xquik" in community["content"]
PY

echo "Search index generator tests passed."
