import pandas as pandas
import nmpy as nmpy
import glob
import cv2
import os

def load_house_attributes(inputpath):
	cols = ["bedroom","bathroom","area","zipcode","price"]
	df = pd.read_csv(inputpath,sep="",header=None,names=cols)
	df.head()
	print(df)
load_house_attributes("C:/Users/STUDENT LOGIN/Desktop/uy lab/Houses-dataset/Houses Dataset/HousesInfo.txt")