# rapid-test-api

## About

Quick script to spin up an API with either FastAPI or Flask.<br>
Parses JSON files to dictate the endpoints and what they return.

## Preview

[Base Command Screenshot](screenshots/base-command.png?raw=true)
[Postman Screenshot](screenshots/postman.png?raw=true)

## Prerequisites

1. Python3.12
2. Python Requirements
    - For Both:
        - pydantic 2.8.2
    - For FastAPI:
        - fastapi 0.115.0
        - uvicorn 0.31.0
    - For Flask:
        - Flask 3.0.3

```python
pip install -r ./fastapi_requirements
```
```python
pip install -r ./flask_requirements
```

## Instruction

1. Clone this repository
```bash
$ git clone https://github.com/tu-nguyen/rapid-test-api.git
```
2. (Optional) Create JSON file(s) base on what's in the sample directory
3.  Run to spin
```bash
$ python rapid-api.py
```

## Usage

```
rapid-api [options]

-p, --port <port>
-m, --model <model>
-e, --endpoint <endpoint>
```

## Examples

### No args
### Simple
### Complex