# Welcome to SciGlassPlus

A python library for the access of SciGlassPlus database.

## How to install

```commandline
pip install SciGlassPlus
```

## Examples

### 1. Access available elements, compounds, properties and metadata

```python
from SciGlassPlus.load import SGP, available_columns

columnNames = available_columns()
```
The function `available_columns()` will return a python dictionary containing 4 `keys`: `"Elements"`, `"Compounds"`, `"Properties"`, `"Metadata"`. The `value` of each key form a list, which includes available items.

### 2. Access all data

```python
df_all = SGP()
```
### 3. Access the specified data

This method can  help you filter out items you do not pay attention to and filter out data you do care about.
```python
elements_cfg = {
    "drop": ["Ca"],
    "keep": ["Si"]
}

compounds_cfg = {
    "drop": ["CaO", "TiO2"],
    "keep": ["SiO2", "Al2O3"]
}

properties_cfg = {
    "drop": ["T1", "T2"],
    "keep": ["Tg"]
}

metadata_cfg = {
    "drop": ["Institutions"],
    "keep": ["Doi"]
}

df_filtered = SGP(
    elements_cfg=elements_cfg,
    compounds_cfg=compounds_cfg,
    properties_cfg=properties_cfg,
    metadata_cfg=metadata_cfg
)
```
For all the 4 configurations, the items in the list after the key `"drop"` means that the columns of these items are deleted from the returned data.
By the way, for *elements* and *compounds*, entries containing non-zero values in these items are filtered out.

For all the 4 configurations, the items in the list after the key `"keep"` means that only entries with defined values in these items are kept in the filtered data.
