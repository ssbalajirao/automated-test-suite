# Automated Web Application Test Suite

A professional-grade test automation framework built with Selenium and Python.

## Overview

This project demonstrates:
- Page Object Model (industry standard)
- Reusable test components
- Comprehensive test cases
- CI/CD pipeline integration

## Installation

1. Create virtual environment: `python -m venv venv`
2. Activate: `venv\Scripts\activate`
3. Install: `pip install -r requirements.txt`

## Running Tests
```bash
pytest tests/ -v
pytest tests/ -v --html=reports/report.html --self-contained-html
```

## Project Structure
```
automated-test-suite/
├── config/
│   └── config.py
├── pages/
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/
│   └── test_login.py
├── conftest.py
├── requirements.txt
└── README.md
```

## Features

Page Object Model

Reusable Components

Explicit Waits

Comprehensive Test Cases
Professional Documentation
