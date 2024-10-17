## Dataset Source
Data is present in Azure Storage account so to connect with azure you need to provide secrets and is stored in key vault.
 Create secret key in key vault to store your connection string .
 Conection is present inside access keys of your storage account

azure-connection-string:"your connection string from azure" .                                                                             
key_vault_url:"https://<keyvaultname>.vault.azure.net"                                          
blob_name: "credit_data/data.csv" .




# How to run?
### STEPS:

Clone the repository  make some changes for secrets

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
## Steps to follow in azure cloud
1. create secret key in key vault to store your connection string of storage account for data ingestion purpose.Allow access policiy for your web app
2.  Create azure container registry and copy Login server,user name  and password  from Access keys to be needed while login from local vs
3. Create Web app 
 
   


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
