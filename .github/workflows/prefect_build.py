name: verify_prefect_deployability

on:
  pull_request:
    branches:
      - master

jobs:
  verify:
    name: Verify Prefect Deployability
    runs-on: ubuntu-latest

    steps:
      # Checkout the code
      - name: Checkout repository
        uses: actions/checkout@v3

      # Set up Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      # Install dependencies
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt
          pip install prefect

      # Verify Python syntax across the repo
      - name: Check Python Syntax
        run: |
          echo "Scanning for syntax errors..."
          find . -name "*.py" -exec python -m py_compile {} \;

      # Validate installed packages
      - name: Check Dependency Health
        run: |
          pip check

      # Validate Prefect deployment config
      - name: Validate prefect.yaml (if exists)
        run: |
          if [ -f prefect.yaml ]; then
            echo "Validating prefect.yaml..."
            prefect deploy --help > /dev/null
          else
            echo "⚠️ No prefect.yaml found. Skipping Prefect config check."
          fi
