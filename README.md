# Master_thesis

# Fact-checker support system for CIMPLE Project

REST API for the Fact-checker support system.

This API provides the one research paper and author ranking of this paper. 

## Prerequisites

We require a Python 3.10.6 or above.

Requirement by service:

| Service     | Requirement(s)                          |
|-------------|-----------------------------------------|
| `/fact_checker_suggestion/`          | `User keyword or a set of keywords`     |


## How to run

### With ``docker-compose``


```commandline
docker-compose up -d
```

### Manually
```commandline

Run FastAPI

uvicorn main:app --reload

```
For local development you may run the web server using ``uvicorn`` with the ``--reload`` option:

```commandline
uvicorn app.main:app --host 0.0.0.0 --port 4321 --reload
```


| Sample Input                                                                                   | Output                                                                                    | Explannation                       |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------|
| `COVID-19,clinical research, ethics, infectious disease, outbreak, pandemic, public health`    | '10.2196/18887', "Prasad R  Padala": 1,  "Ashlyn M  Jendro": 2,"Kalpana P  Padala": 2     | Higher number means higher ranking |   
| `COVID-19 pandemic, China, Healthcare services, Inequality, Megacities, Spatial accessibility` | "10.1016/j.healthplace.2020.102406", "Pengjun  Zhao": 1, "Shengxiao  Li": 1, "Di  Liu": 0 | Higher number means higher ranking |    

## API Documentation
After successfully running the application, check the documentation at `localhost:4321/docs`
or `localhost:4321/redoc` (please adapt your `host:port` in case you configured them).
