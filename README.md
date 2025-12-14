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