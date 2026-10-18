name: Build Android AAB

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y build-essential libffi-dev libssl-dev ccache zip unzip openjdk-17-jdk git python3-pip

      - name: Install Build tools
        run: |
          python -m pip install --upgrade pip setuptools
          pip install buildozer cython==0.29.33 kivy

      - name: Build AAB with Buildozer
        run: |
          buildozer android release

      - name: Upload AAB Artifact
        uses: actions/upload-artifact@v4
        with:
          name: elyor-ai-aab
          path: bin/*.aab
