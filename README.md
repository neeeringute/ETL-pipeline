# ETL Pipeline v1
![Web capture_25-1-2024_123919_](https://github.com/neeeringute/ETL-pipeline/assets/145553499/f6393f48-bda2-4f1e-b270-9fe6335db710)

## Introduction
This code contains the steps to build an ETL pipeline that carries out the following tasks:
- Extracts 400k transactions from Redshift
- Identifies and removes duplicates
- Loads the transformed data to a s3 bucket

## Requirements
The minimum requirements:
- Python 3+

## Instructions on how to execute the code

1. Clone the repository, and go to the week19 folder
````

````

2. Install the libraries that they need to run `main.py`
````
pip3 install -r requirements.txt
````

3. Copy the `.env.copy` file to `.env`and fill out the environment variabls.

4. Run the `main.py` script
Mac users:
```
python3 main.py
```


```
python main.py
