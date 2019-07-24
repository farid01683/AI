import pandas as pd
import numpy as np
import glob
import cv2
import os

def load_house_attributes(inputpath):
	cols = ["bedroom","bathroom","area","zipcode","price"]
	df = pd.read_csv(inputpath,sep=" ",header=None,names=cols)
	#df.head()
	#print(df)
#load_house_attributes("C:/Users/STUDENT LOGIN/Desktop/uy lab/Houses-dataset/Houses Dataset/HousesInfo.txt")
	zipcode = df["zipcode"].value_counts().keys().tolist()
	counts = df["zipcode"].value_counts().tolist()

	for (zipcode,count) in zip(zipcode,counts):
		if count > 25:
			id =df[df["zipcode"]==zipcode].index
			df.drop(id,inplace=True)
			print(df)
load_house_attributes("C:/Users/STUDENT LOGIN/Desktop/uy lab/Houses-dataset/Houses Dataset/HousesInfo.txt")
