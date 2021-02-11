#!/usr/bin/env python
# coding: utf-8

# In[102]:


# 42_The_Logistic_Regression_Model.py
# Logistic Regression
# Used in Machine Learning categoric predictions
# Examples: Is an email a spam? Yes or No What is the species of a plant? A, B or C (Like the Iris dataset)
# Is normally used in binary classifications
# How does it work:
# A binary example first, with two possible species of a plant.
# Working with more than two variables:
# One vs All

# 43_Applying_the_Logistic_Refression_Model.py
# Applying the Logistic Refression Model


# hint: command shift p to see shortcuts
# run cell and select next -> [option][shift]

from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)


# In[103]:


# print the targets (numbers 0,1,2 represent the names of the target data as numeric values)
print(iris.target)


# In[104]:


# names of targets (0,1,2)
print(iris.target_names)


# In[105]:


print(iris.data.shape)


# In[106]:


print(iris.target.shape)


# # Importing KNN

# In[107]:


# KNeighborsClassifier is case sensetive
# make KNeighborsClassifier a function passing in n_neighbors=1
# create a new variable, knn -> knn = KNeighborsClassifier(n_neighbors=1) - 1 may not be the best value, we will try to choose the best value later
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)


# In[108]:


# capital X is usally the data and y is the target

X = iris.data
y = iris.target


# In[109]:


# the fit function is used to train the computer - pass in X and y as parameters
knn.fit(X,y)
# information about the projection is returned as an Out value, notice the n_neighbors value


# In[110]:


# Now we predict 
# The Iris Dataset - Ronald Foisher - Biologist
# Collected 150 samples pf Iris flowers
# 50 samples of each of three different species
# Of each sample, he took the measurements of the petal and the sepal
# see -> https://www.kaggle.com/ for additional info including tutorials
# The Iris Dataset - Ronald Foisher - Biologist
# Collected 150 samples pf Iris flowers
# 50 samples of each of three different species
# Of each sample, he took the measurements of the petal and the sepal
# get a sample from the Iris Dataset (species data) - choose one set and clean the data
# Sepal.Length, SepalWidth, Petel.Length, Petal.Width, Species
# google for more info -> iris dataset machine learning

# list of observations coipied from above 
print(knn.predict( [ [5.9,3,5.1,1.8 ] ] ) )
# get a sample from the Iris Dataset (species data) - choose one set and clean the data
# Sepal.Length, SepalWidth, Petel.Length, Petal.Width, Species
# google for more info -> iris dataset machine learning
### print(knn.predict( [ [5.9,3,5.1,1.8 ] ] ))


# ## Seperate data into train and test groups

# In[111]:


# use sklearn -> https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
# X_train - train the computer
# X_test - test permance of the train
# y_train - y train the computer
# y_test - y test the training of the computer

# test_size = 0.25 means that 75 % of data will be used for training
# test_size = 0.25, random_state=42 
# the random_state=42 will provide more accuracy across testors

from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25)   # performance = 0.9736842105263158
## X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=42) # performance = 1.0


#### X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.40, random_state=42) # performance = 0.9833333333333333

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=20) # performance = 


# In[112]:


# print(X_train) - will show the training data
# print(X_train.shape) - will show the number of observations used to train
# print(X_test.shape) - will show the number of observations use to test
print(X_test.shape)


# In[113]:


# lets see what is predicted - observations are done ramdomly by the train_test_split module
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(predictions)


# In[114]:


# compare with predictions above, visual inspection seems to match
print(y_test)


# In[115]:


# use the sklearn metrics module to help with the analysis
from sklearn import metrics
performance = metrics.accuracy_score(y_test, predictions)
print(performance)


# In[116]:


# Picking the best value of k
# Create a loop to apply KNN with values ranging from 1 to 25.
# Test the perfomance of each K value and present the ones that best suits our dataset.
# answer below
# create a dictionary of K values (k_values)
# build the dictionary as we loop

k_values = {}
k = 1

while k <= 25:
    ### NO  answers.append(correct_answer)
    ### NO k_values.append('k':k, 'p_val':p)
    
    knn = KNeighborsClassifier(n_neighbors = k) # copied from above but 1 replaced by k - looping
    knn.fit(X_train, y_train)  # use the X_train and y_train parameters
    predictions = knn.predict(X_test)
    performance = metrics.accuracy_score(y_test, predictions)  # copied from above
    k_values[k] = round(performance,4) # add to dictionary with k as the key and performance as the value
    k += 1
print(k_values)
    


# In[117]:


# make a chart for easier analysis
import matplotlib.pyplot as plt

# to show inline, use the next line
### get_ipython().run_line_magic('matplotlib', 'inline')

# make a list from the k_values dictionary 
plt.plot(list(k_values.keys()), list(k_values.values()))
plt.xlabel("Values of K")
plt.ylabel("Performance %")
plt.title("A Super Good Chart!")
plt.show()


# ## Logistic Regression

# In[118]:


#
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
## choose from above in the iris.data
# names: ['setosa' 'versicolor' 'virginica']
####### 5.1 3.5 1.4 0.2  - the first set
## 6.9 3.1 4.9 1.5 - virginica I think
# instructors set 6.7,3.3,5.7,2.5
## print(logreg.predict_proba([ [ 6.9, 3.1, 4.9, 1.5 ] ] ) ) # [[0.00178733 0.67559769 0.32261498]]  67% chance of virginica
### instructor values
#### print("logreg.predict_proba", logreg.predict_proba([ [ 6.7,3.3,5.7,2.5 ] ] ) ) # his values [[0.0094236 018246443 0.81759321]] very different -> [[1.46650288e-05 2.27887927e-02 9.77196542e-01]]
#### print("logreg.predict", logreg.predict([[ 6.7,3.3,5.7,2.5]]))
predictions_logreg = logreg.predict(X_test)
performance_logreg = metrics.accuracy_score(y_test, predictions_logreg)
print("performance_logreg", performance_logreg)


# In[ ]:




