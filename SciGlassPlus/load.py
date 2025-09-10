import pandas as pd
import os
import json


def available_columns(output: bool = True):
    """Return and/or print available items in SciGlassPlus

    Args:
        output: whether to print the information in the command line
    Returns:
        A python dictionary containing available items in SciGlassPlus

    """
    if output:
        print("--------")
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, "ColumnNames.json")
    with open(json_path, "r", encoding="utf-8") as f:
        column_names = json.load(f)

    if output:
        for key, value in column_names.items():
            print(key)
            # print(value)
            for v in value:
                print("    {:s}".format(v))
            print("--------")
    return column_names


class SGP:
    """Loader of SciGlassPlus data

    Args:
        elements_cfg: dictionary configuring how to deal with information in "Elements" items.
        compounds_cfg: dictionary configuring how to deal with information in "Compounds" items.
        properties_cfg: dictionary configuring how to deal with information in "Properties" items.
        metadata_cfg: dictionary configuring how to deal with information in "Metadata" items.

    Returns:
        The filtered SciGlassPlus data
    """
    def __init__(
            self,
            elements_cfg: dict | None = None,
            compounds_cfg: dict | None = None,
            properties_cfg: dict | None = None,
            metadata_cfg: dict | None = None,
    ):
        current_dir = os.path.dirname(__file__)
        DB_path = os.path.join(current_dir, "SciGlass_Plus_properties.xlsx")
        column_names = available_columns(output=False)
        keep_columns = available_columns(output=False)
        print("reading total data")
        self.data = pd.read_excel(DB_path)

        # drop unwanted rows
        print("filtering")
        indices_to_drop = []

        if elements_cfg is not None:
            if "drop" in elements_cfg:
                for i in elements_cfg["drop"]:
                    if i not in column_names["Elements"]:
                        raise ValueError("Element {:s} is not supported. Please call available_columns() to check the  supported elements".format(i))
                    condition = self.data[i].notna() & (self.data[i] > 0)
                    indices_to_drop.extend(self.data[condition].index.tolist())
                    keep_columns["Elements"].remove(i)
            if "keep" in elements_cfg:
                # to_keep = []
                for i in elements_cfg["keep"]:
                    if i not in column_names["Elements"]:
                        raise ValueError("Element {:s} is not supported. Please call available_columns() to check the  supported elements".format(i))
                    condition = self.data[i].isna()
                    indices_to_drop.extend(self.data[condition].index.tolist())

        if compounds_cfg is not None:
            if "drop" in compounds_cfg:
                for i in compounds_cfg["drop"]:
                    if i not in column_names["Compounds"]:
                        raise ValueError("Compound {:s} is not supported. Please call available_columns() to check the  supported compounds".format(i))
                    condition = self.data[i].notna() & (self.data[i] > 0)
                    indices_to_drop.extend(self.data[condition].index.tolist())
                    keep_columns["Compounds"].remove(i)
            if "keep" in compounds_cfg:
                # to_keep = []
                for i in compounds_cfg["keep"]:
                    if i not in column_names["Compounds"]:
                        raise ValueError("Compound {:s} is not supported. Please call available_columns() to check the  supported compounds".format(i))
                    condition = self.data[i].isna()
                    indices_to_drop.extend(self.data[condition].index.tolist())

        if properties_cfg is not None:
            if "drop" in properties_cfg:
                for i in properties_cfg["drop"]:
                    if i not in column_names["Properties"]:
                        raise ValueError("Property {:s} is not supported. Please call available_columns() to check the  supported properties".format(i))
                    keep_columns["Properties"].remove(i)
            if "keep" in properties_cfg:
                # to_keep = []
                for i in properties_cfg["keep"]:
                    if i not in column_names["Properties"]:
                        raise ValueError("Property {:s} is not supported. Please call available_columns() to check the  supported properties".format(i))
                    condition = self.data[i].isna()
                    indices_to_drop.extend(self.data[condition].index.tolist())

        if metadata_cfg is not None:
            if "drop" in metadata_cfg:
                for i in metadata_cfg["drop"]:
                    if i not in column_names["Metadata"]:
                        raise ValueError("Metadata {:s} is not supported. Please call available_columns() to check the  supported metadata".format(i))
                    keep_columns["Metadata"].remove(i)
            if "keep" in metadata_cfg:
                # to_keep = []
                for i in metadata_cfg["keep"]:
                    if i not in column_names["Metadata"]:
                        raise ValueError("Metadata {:s} is not supported. Please call available_columns() to check the  supported metadata".format(i))
                    condition = self.data[i].isna()
                    indices_to_drop.extend(self.data[condition].index.tolist())

        indices_to_drop = list(set(indices_to_drop))
        self.data = self.data.drop(indices_to_drop)

        keep_columns = ["ID"] + keep_columns["Elements"] + keep_columns["Compounds"] + keep_columns["Properties"] + keep_columns["Metadata"]
        self.data = self.data[keep_columns]


