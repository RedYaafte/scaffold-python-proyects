# FastAPI Scaffold

## Prerequisites

- Python 3.10+
- (Optional) Docker

## How to use

### Docker

```sh
> docker-compose up
```

### Local

Create virtual environment with dependencies

```sh
> python3 -m venv venv
> . venv/bin/activate
> pip install -r requirements.txt
```

Start proyect

```sh
> uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### TEST

```sh
> pytest
```
