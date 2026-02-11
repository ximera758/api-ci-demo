# API CI Demo – QA Automation

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/PyTest-Testing-orange)](https://docs.pytest.org/)
[![CI Status](https://github.com/ximera758/api-ci-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/ximera758/api-ci-demo/actions/workflows/ci.yml)

This repository contains API automation tests with a focus on CI/CD integration using GitHub Actions.

## 📋 Project Overview

This demo includes:
- API tests written in Python using PyTest
- Example of continuous integration
- Easily extendable for real API services

## 🛠 Technology Stack

- Python
- PyTest
- Requests

## 📁 Project Structure
api-ci-demo/
├── tests/
│ ├── test_api_endpoints.py
├── .github/
│ └── workflows/
│ └── ci.yml
├── requirements.txt
├── .gitignore
└── README.md

## 🚀 How to Run Locally

1. Clone repository:

```bash
git clone https://github.com/ximera758/api-ci-demo.git
cd api-ci-demo
2 Install dependencies:
pip install -r requirements.txt
3 Run tests:
pytest -v

📌 What is tested

Describe here what your tests actually validate. For example:

API returns valid HTTP status codes

Response contains expected JSON schema

Error handling validation
🧠 Example Output
============================ test session starts ============================
collected 1 item

tests/test_api_endpoints.py .                                            [100%]

=========================== 1 passed in 0.34s ===========================
📈 CI with GitHub Actions

The repository is configured to run tests on each push.

📓 Notes

This demo can be extended to:

Include API schema validations (e.g., JSON schema)

Add reporting (pytest-html)

Add Docker execution
---
