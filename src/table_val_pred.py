# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
import random
from simpletransformers.classification import ClassificationModel,ClassificationArgs
import sklearn
#

with open("./val_tables.json", "r", encoding="utf-8") as f:
    abstract2 = json.load(f)

model = ClassificationModel("roberta", "./outputs/")
predictions, raw_outputs=model.predict(abstract2)


with open('./pred_val_tables.json', 'w') as file:
    file.write(json.dumps(predictions))
