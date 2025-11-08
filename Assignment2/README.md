# Assignment 2: Codebase Genius

## Overview

Codebase Genius is an AI-powered, multi-agent system that automatically generates high-quality documentation for any software repository.

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://generative-ai-ghqzfnzx4qjnfnwdnz6xhf.streamlit.app/)

## System Architecture

- **Code Genius (Supervisor)** - Orchestrates workflow
- **Repo Mapper** - Clones repositories and generates file structure
- **Code Analyzer** - Parses code and builds Code Context Graphs
- **DocGenie** - Generates final markdown documentation

## How to Run the System

### Prerequisites

- Python 3.8+
- Git

### Method 1: Local Python Backend

```bash
cd Assignment2/BE
python -m venv genius-env
genius-env\Scripts\activate
pip install -r requirements.txt
python main.py
```
