### Getting started

### AAD Secrets

```bash
export AAD_TENANT_ID=""
export AAD_CLIENT_ID=""
export AAD_CLIENT_SECRET=""
```


#### Activate the python venv
```
source bin/activate
```

#### Install dependencies

```
pip install -r requirements.txt
```

### Starting the server

```
python app.py
```

### Dev Workflow

#### Freeze Dependencies
```
pip freeze > requirements.txt
```
#### Starting local https & ssl

```
npx local-ssl-proxy --key ~/server.key --cert ~/server.crt --source 3001 --target 3000
```

#### Run pylint
```
pylint *.py
```

### Help?
- https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment
- https://github.com/Azure-Samples/ms-identity-python-webapp/blob/master/app_config.py
