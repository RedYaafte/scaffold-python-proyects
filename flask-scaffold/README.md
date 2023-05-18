# Flask Scaffold

## Prerequisites

- Python 3.10+
- (Optional) Docker

## How to use

### Docker

```sh
> docker build --tag python-docker .
> docker run -d -p 5000:5000 python-docker
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
> python3 app.py
```

### TEST

```sh
> pytest tests
```
