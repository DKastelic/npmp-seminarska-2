## Setup

1. Initialise GReNMlin submodule
```bash
git submodule update --init --recursive
```

2. Fix GReNMlin to be a python package
```bash
git apply changes.patch --directory=GReNMlin
```


## Running

Example of how to run the repressilator simulation: from base directory (seminarska-2) run
```bash
python -m motifs.repressilator
```

(regular way doesn't work because of how python's module system works)