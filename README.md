# python-sample-test
Unit Testing in Python

# Commands
### INSTALL VM 
#### Only 1º 
```
sudo apt-get install python3-venv (Linux)
sudo pip install virtualenv (Mac)
```

### CREATE VM
#### Only 1º (create only to os different)
```
python3 -m venv $name-machine 
```

### ACTIVE VM
```
source $name-machine/bin/activate
``` 

### RUN TESTS
```
python -m unittest tests.test
```

### FREEZE DEPENDENCIES
```
pip freeze > requirements.txt
```
