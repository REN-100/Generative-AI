# Assignment 2: Codebase Genius

## Overview

Codebase Genius is an AI-powered, multi-agent system that automatically generates high-quality documentation for any software repository. This system analyzes codebases, extracts structural information, and produces comprehensive markdown documentation.

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://generative-ai-ghqzfnzx4qjnfnwdnz6xhf.streamlit.app/)

## System Architecture

### Multi-Agent Design

- **Code Genius (Supervisor)** - Orchestrates the workflow and coordinates agents
- **Repo Mapper** - Clones repositories and generates file structure maps
- **Code Analyzer** - Parses code and builds Code Context Graphs
- **DocGenie** - Synthesizes final markdown documentation

### Technology Stack

- **Backend**: Python with Jac language implementations
- **Frontend**: Streamlit web interface
- **APIs**: GitHub integration for repository access
- **Analysis**: Abstract Syntax Tree (AST) parsing

## 📋 How to Run the System

### Prerequisites

- Python 3.8+
- Git
- GitHub account (for repository access)

### Method 1: Local Python Backend

```bash
# Navigate to backend directory
cd Assignment2/BE

# Create virtual environment
python -m venv genius-env

# Activate virtual environment
# Windows:
genius-env\Scripts\activate
# macOS/Linux:
source genius-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the main system
python main.py

# Or run individual components
python python_repo_mapper.py
python python_code_analyzer.py
python python_doc_genie.py
```
