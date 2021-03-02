#PACKAGES 
import pandas as pd 
import numpy as np
import nltk
from nltk.corpus import stopwords

#QUESTION1:

dataFrm = pd.read_csv("IMDB.csv")  
dataFrm.columns= ["review", "sentiment"]

print(dataFrm.head())

# QUESTION 2:

#*************QUESTION 2-1**************
print(dataFrm.sentiment.value_counts())
#**************Ou bien : *********
#nbr_pos = len( [ x for x in dataFrm.sentiment if x == "positive"] )
#nbr_neg = len( [ x for x in dataFrm.sentiment if x == "negative"] )
#print("Positive revies:",nbr_pos, " ; Negative reviews:",nbr_neg)

#************QUESTION 2-2**************
dataFrm["phrase_len"] = [len(x) for x in dataFrm.review]
print(dataFrm.head(2))

#************QUESTION 2-3***************

group = dataFrm.groupby("sentiment")
#mean: moyenne
print("Taille moyenne pour neg. reviews: ", group.get_group("negative")["phrase_len"].mean())
print("Taille moyenne pour pos. reviews: ", group.get_group("positive")["phrase_len"].mean())

#************QUESTION 2-4***************
#loc : Access a group of rows and columns by label(s) or a boolean array.
dataFrm = dataFrm.loc[ (dataFrm["phrase_len"] > 3) , : ]
print(dataFrm.head(5))

#************QUESTION 2-5***************

dataFrm = dataFrm.drop(columns = "phrase_len" )
print(dataFrm.head(2))

#Question3
#------------QUESTION3.1: netoyage de corpus ----------
# upper to lower
def wordLowerCase(text):
	return text.lower()
def tokenization(text):
	return (text.split())
print(tokenization("chahrazed djida"))

