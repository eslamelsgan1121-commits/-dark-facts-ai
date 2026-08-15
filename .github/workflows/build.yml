name: Build Automation System

on:
  workflow_dispatch:
  push:
    branches: [ "main" ]

jobs:
  run-ai-script:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install Dependencies
      run: pip install google-generativeai

    - name: Run Main Script
      env:
        GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
      run: python3 main.py
