import pandas as pd
import json

df = pd.read_excel("SciGlass_Plus_properties.xlsx")

all_columns = df.columns.tolist()

Elements = all_columns[1: 77]
Compounds = all_columns[77: 628]
Properties = all_columns[628: 720]
Metadata = all_columns[720: 728]

ColumnNames = {
    "Elements": Elements,
    "Compounds": Compounds,
    "Properties": Properties,
    "Metadata": Metadata
}

with open("ColumnNames.json", 'w', encoding="utf-8") as f:
    json.dump(ColumnNames, f, ensure_ascii=False, indent=4)
