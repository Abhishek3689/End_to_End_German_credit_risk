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
https://github.com/Abhishek3689/End_toEnd_German_credit_risk
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
