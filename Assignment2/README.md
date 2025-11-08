# Assignment 2: Codebase Genius

## Overview
Codebase Genius is an AI-powered, multi-agent system that automatically generates high-quality documentation for any software repository.

## System Architecture
- **Code Genius (Supervisor)** - Orchestrates the workflow
- **Repo Mapper** - Clones repository and generates file structure
- **Code Analyzer** - Parses code and builds Code Context Graph
- **DocGenie** - Generates final markdown documentation

## Quick Start

### Prerequisites
- Python 3.8+
- Git
- LLM API key (OpenAI)

### Installation
1. Set up virtual environment:
\\\ash
cd Assignment2/BE
python -m venv genius-env
genius-env\Scripts\activate
\\\

2. Install dependencies:
\\\ash
pip install -r requirements.txt
\\\

3. Set up environment variables:
\\\ash
# Create .env file with  API key
echo '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' > .env
\\\

### Running the System
1. Start the backend:
\\\ash
jac serve main.jac
\\\

2. (Optional) Start the frontend:
\\\ash
cd ../FE
streamlit run app.py
\\\

## Usage
Send a POST request to analyze a repository:
\\\ash
curl -X POST http://localhost:8000/analyze -H 'Content-Type: application/json' -d '{\"github_url\": \"https://github.com/username/repo\"}'
\\\

## Sample Output
See [outputs/](./outputs/) for example generated documentation.
