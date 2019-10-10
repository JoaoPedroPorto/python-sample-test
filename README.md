# python-sample-test
Unit Testing in Python

# Commands
### INSTALL VM 
#### Somente 1º vez
```
sudo apt-get install python3-venv
```

### CREATE VM
#### Somente 1º vez
```
python3 -m venv sandbox 
```

### ACTIVE VM
```
source sandbox/bin/activate
``` 

### RUN TESTS
```
python -m unittest tests/test.py 
```

### FREEZE DEPENDENCIES
```
pip freeze > requirements.txt
```
