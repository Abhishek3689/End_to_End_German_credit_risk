### Dataset Source
Data is present in Azure Storage account so to connect with azure you need to provide secrets and is provided in secrets.yml file.
The secret file you can create yourself with similar key value as config.yml.

Connection_string:"your connection string from azure"
blob_name: "credit_data/data.csv"


## 

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Abhishek3689/End_to_End_German_credit_risk.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -p venv python=3.10 -y
```

```bash
conda activate venv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```
## To build Docker Image and push in azure container Registry
Run from terminal:
```bash
docker build -t creditregistry1.azurecr.io/mltest:latest .
```
login to azure registry 
```bash
docker login creditregistry1.azurecr.io
```
push your Docker to azure resitry container
```bash
docker push creditregistry1.azurecr.io/mltest:latest
```
