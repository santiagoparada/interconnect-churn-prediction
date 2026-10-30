# Data files

The original datasets are not distributed in this repository because they were supplied for an educational project.

To reproduce the notebook, place these files in `data/raw/`:

```text
contract.csv
personal.csv
internet.csv
phone.csv
```

The notebook also supports TripleTen's original `/datasets/final_provider/` path.

Expected population:

- `contract.csv`: 7,043 customers
- `personal.csv`: 7,043 customers
- `internet.csv`: 5,517 customers
- `phone.csv`: 6,361 customers

All joins are performed by `customerID`, using `contract.csv` as the customer universe.
