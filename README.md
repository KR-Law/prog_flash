# Prog-Flash 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/)

## Description

Prog-Flash is a command-line flashcard application designed to help users memorize and study various topics efficiently. It allows for the creation, management, and review of digital flashcards in a structured and engaging manner.

This project provides a robust framework for spaced repetition or simple quiz-style learning right from your terminal.

## Features

*   **Card Management:** Easily create and edit flashcards with distinct front (question) and back (answer) sides.
*   **Review Mode:** Dedicated mode to test knowledge by presenting the card question first, allowing users to recall the answer before revealing it.
*   **Structured Learning:** Organize multiple sets of cards for different subjects or topics within a single application.
*   **CLI Interface:** Designed for quick and seamless use directly in the terminal environment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You must have **Python 3.13 or later** installed on your system.

```bash
# You can check your version with:
python --version
```

## Development

1.  Clone the repository (if necessary):
    ```bash
    git clone https://github.com/kr-law/prog_flash.git
    cd prog_flash
    ```
2.  Setup a virtual env
    ```bash
    uv venv
    ```
3. Activate virtual env
    ```bash
    source .venv/bin/active
    ```
4. Install Dependencies
    ```bash
    uv pip install --group dev
    ```

### Testing

Tests are in pytest. 

```bash
    uv pip run pytest
```

## Usage

Once installed, you can run the application using the package name defined in `pyproject.toml`:

```bash
prog-flash
```

Follow the on-screen prompts to create a new flashcard deck or start reviewing existing ones.

---
*Developed by Kyle Law | Built with Python.*

