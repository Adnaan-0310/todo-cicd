#!/bin/bash
TASKS_FILE="$1"
TEST_FILE="$2"
HTML=/app/index.html
[ -f "$HTML" ] || HTML=index.html

TODO=$(awk '/^ToDo Tasks:/{f=1;next}/^Done Tasks:/{f=0}f' "$TASKS_FILE")
DONE=$(awk '/^Done Tasks:/{f=1;next}f' "$TASKS_FILE")
TESTS=$(cat "$TEST_FILE")

update_pre() {   # $1=id  $2=content  $3=file
  CONTENT="$2" perl -0pi -e 's|(<pre id="'"$1"'">).*?(</pre>)|$1$ENV{CONTENT}$2|s' "$3"
}

update_pre todo  "$TODO"  "$HTML"
update_pre done  "$DONE"  "$HTML"
update_pre tests "$TESTS" "$HTML"

git config --global user.email "github-actions@users.noreply.github.com"
git config --global --add safe.directory /app
git add "$HTML" 2>/dev/null
git commit -m "Update index.html with tasks and test results" 2>/dev/null || echo "Nothing to commit"
git push 2>/dev/null || echo "Push skipped (done by workflow)"
