#!/usr/bin/env python
# coding: utf-8

# ## Exercise_Importing_KNN_what_is_the_best_k_value-step_0

# In[191]:


# part 2 - also includes the exercize conclusion with chart
# hint: command shift p to see shortcuts
# run cell and select next -> [option][shift]
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)


# In[176]:


# print the targets (numbers 0,1,2 represent the names of the target data as numeric values)
print(iris.target)


# In[177]:


# names of targets (0,1,2)
print(iris.target_names)


# In[178]:


print(iris.data.shape)


# In[179]:


print(iris.target.shape)


# ## Importing KNN

# In[180]:


# KNeighborsClassifier is case sensetive
# make KNeighborsClassifier a function passing in n_neighbors=1
# create a new variable, knn -> knn = KNeighborsClassifier(n_neighbors=1) - 1 may not be the best value, we will try to choose the best value later
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)


# In[181]:


# capital X is usally the data and y is the target

X = iris.data
y = iris.target


# In[182]:


# the fit function is used to train the computer - pass in X and y as parameters
knn.fit(X,y)
# information about the projection is returned as an Out value, notice the n_neighbors value


# In[183]:


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

# In[184]:


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
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.40, random_state=42) # performance = 0.9833333333333333


# In[185]:


# print(X_train) - will show the training data
# print(X_train.shape) - will show the number of observations used to train
# print(X_test.shape) - will show the number of observations use to test
print(X_test.shape)


# In[186]:


# lets see what is predicted - observations are done ramdomly by the train_test_split module
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(predictions)


# In[187]:


# compare with predictions above, visual inspection seems to match
print(y_test)


# In[188]:


# use the sklearn metrics module to help with the analysis
from sklearn import metrics
performance = metrics.accuracy_score(y_test, predictions)
print(performance)


# In[189]:


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
    


# In[190]:


# make a chart for easier analysis
import matplotlib.pyplot as plt

# to show inline, use the next line
### get_ipython().run_line_magic('matplotlib', 'inline')

# make a list from the k_values dictionary 
plt.plot(list(k_values.keys()), list(k_values.values()))
plt.xlabel("Values of K")
plt.ylabel("Performance")
plt.show()


# In[ ]:




