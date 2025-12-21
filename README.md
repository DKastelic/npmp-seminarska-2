## Setup

1. Initialise GReNMlin submodule
```bash
git submodule update --init --recursive
```

2. Fix GReNMlin to be a python package
```bash
git apply changes.patch --directory=GReNMlin
```

3. Install requirements
```bash
python -m venv .venv
pip install -r requirements.txt
```


## Running

Example of how to run the repressilator simulation: from base directory (seminarska-2) run
```bash
python -m motifs.repressilator
```

(regular way doesn't work because of how python's module system works)


# Using tellurium

You will need a bit older version of python 3.12. should work.

1. install tellurium
```bash
pip install tellurium
```

if you get problems here you will need to switch python version probably.

2. you are done, just run the code