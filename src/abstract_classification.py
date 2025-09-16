# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
import random
from simpletransformers.classification import ClassificationModel,ClassificationArgs
import sklearn
#
path='/data/home/zhaoyj/nlp/'
filename='sample.json'
file=open(path+filename)
d0=json.load(file)
file.close()

train_data=d0['train_data']

folder=''
	
train_df = pd.DataFrame(train_data[0])
train_df.columns = ["text", "labels"]
model_args = ClassificationArgs(num_train_epochs=40,n_gpu=1,sliding_window=True,save_model_every_epoch=True,overwrite_output_dir=True,save_steps=-1)

#dir2=os.listdir("./output"+str(1))
#for d in dir2:
    #tmp=d.split("-")
    #if int(tmp[-1])==20:
        #folder=d

model = ClassificationModel("roberta", "/data/home/zhaoyj/nlp/output"+str(1), args=model_args)
model.train_model(train_df,output_dir="output"+str(1))
