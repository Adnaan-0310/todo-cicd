#!/bin/bash
cd /app
python3 .github/scripts/todo.py      | tee /tmp/tasks.txt
python3 .github/scripts/todo-test.py | tee /tmp/tests.txt
bash .github/scripts/update_index.sh /tmp/tasks.txt /tmp/tests.txt
