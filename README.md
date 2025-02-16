- https://blog.pamelafox.org/2022/09/how-i-setup-python-project.html

-- python3 -m venv .venv
-- source .venv/bin/activate 
-- pip install -r requirements-dev.txt 
-- lint: ruff . --select=E9,F63,F7,F82 
-- black --verbose --check . tests 
-- pytest
-- coverage report

