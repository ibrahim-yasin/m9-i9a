# SPARQL CLI Dispatcher

## Overview
This project is a Command Line Interface (CLI) tool that translates natural language intents into SPARQL queries. It demonstrates a simple Natural Language → Query mapping system using predefined intents.

---

## Project Structure
m9-i9a/
│
├── query.py # Main CLI dispatcher
├── requirements.txt # Dependencies
├── README.md # Documentation
│
└── tests/
└── test_dispatcher.py # Pytest test suite


---

## Features
- CLI input using argparse
- Maps natural language intents to SPARQL queries
- Supports multiple query types:
  - SELECT
  - ASK
  - CONSTRUCT
- Handles unknown intents with error messages
- Includes automated testing using pytest

---

## How to Run

### Run a query
```bash
python query.py "list authors at neurips"

| Intent                   | Type      |
| ------------------------ | --------- |
| list authors at neurips  | SELECT    |
| papers per topic         | SELECT    |
| top 5 cited              | SELECT    |
| is ai research available | ASK       |
| citation graph           | CONSTRUCT |


Unknown Intent Example
python query.py "random text"

Output:

Unknown intent

Supported intents:
- list authors at neurips
- papers per topic
- top 5 cited
- is ai research available
- citation graph
Install Dependencies
pip install pytest
Run Tests
python -m pytest -v
Test Coverage

The test suite verifies:

Correct SPARQL output for each intent
Proper handling of SELECT, ASK, and CONSTRUCT queries
Unknown intent handling
Correct exit codes
Design Notes
Uses a dictionary-based intent → SPARQL mapping
Designed as a lightweight NLP-to-SPARQL dispatcher
Acts as a foundation for more advanced knowledge graph query systems
Learning Outcomes
Building CLI tools in Python
Basic NLP intent mapping
SPARQL query design
Unit testing with pytest
Error handling and user feedback

---