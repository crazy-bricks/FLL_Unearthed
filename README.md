# FLL Code for Unearthed

## Project structure

```
src/
  ├── run/            # code for attachment runs
  │     └── yellow.py, red.py ...
  ├── config.py       # constants & config
  ├── helper.py       # misc helper functions
  ├── main.py         # program startup
  ├── movement.py     # handles robot movement
  ├── pid.py          # pid control implementation
  ├── pose.py         # current position & angle
  └── robot.py        # hardware abstraction

models/               # 3d models of the robot and attachments
```

## How to run

```bash
# Download packages
pip install -r ./requirements.txt

# Run
pybricksdev run -n [NAME] ble src/main.py
```