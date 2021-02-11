#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# final exercize
# see Exercise - Finding the best value of K below
# hint: command shift p to see shortcuts
# run cell and select next -> [option][shift]
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)


# In[ ]:


# print the targets (numbers 0,1,2 represent the names of the target data as numeric values)
print(iris.target)


# In[ ]:


# names of targets (0,1,2)
print(iris.target_names)


# In[ ]:


print(iris.data.shape)


# In[ ]:


print(iris.target.shape)


# # Importing KNN

# In[ ]:


# KNeighborsClassifier is case sensetive
# make KNeighborsClassifier a function passing in n_neighbors=1
# create a new variable, knn -> knn = KNeighborsClassifier(n_neighbors=1) - 1 may not be the best value, we will try to choose the best value later
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)


# In[ ]:


# capital X is usally the data and y is the target

X = iris.data
y = iris.target


# In[ ]:


# the fit function is used to train the computer - pass in X and y as parameters
knn.fit(X,y)
# information about the projection is returned as an Out value, notice the n_neighbors value


# In[ ]:


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


# In[ ]:


# google -> random_state, train_test_split and sklearn for expinations on making adjustments to the test_size and random_state can be tweaked to achive better results
# test_size=0.4, random_state=42 were adjusted from test_size=0.25, random_state=42
# making adjustments to those values effect the performance of the test (p value)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


# In[ ]:


print(X_test.shape)


# In[ ]:


knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(predictions)


# In[ ]:


from sklearn import metrics
performance = metrics.accuracy_score(y_test, predictions)
print(performance)

performance = p
# print('p: ', p)
print('y_test: ', y_test)


# # Exercise - Finding the best value of K

# In[ ]:


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
    k_values[k] = round(performace,4) # add to dictionary with k as the key and performance as the value
    k += 1
print(k_values)
    
    


# In[ ]:




