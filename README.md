# Study Planner

# Setting up Python virtual environment

```
py -m pip install --user virtualenv
```

## Mac
```
python3 -m pip install --user virtualenv
```
### Activate the environment
## Windows
```
.\env\Scripts\activate
```

## Mac
```
source env/bin/activate
```

## install flask and update pip

```
pip install flask
pip install --upgrade pip
```

## manage packages installed:

```
pip freeze > requirements.txt
```

## Later when you clone or start fresh, you can install packages:

```
pip install -r requirements.txt
```

### runnning the application

```
flask run
```