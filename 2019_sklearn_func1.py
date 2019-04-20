from sklearn import datasets #importing hand-written digits datasets
import matplotlib.pyplot as plt #importing library to plot
#from sklearn import svm #importing support_vector_machine from sklrearn

digits = datasets.load_digits() #loading digits dataset
#print(digits.data) #.data return the total data in the dataset
#print(digits.target) #target returns the nth feature to which the index of sample belongs to
print(digits.data.shape) #.shape returns nsamples, sfeatures
print(digits.data)
x = [[1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1],
     [1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,1]]
plt.gray()
plt.matshow(digits.images[1]) #.images[n] return the nth integer pixel dataset in a array of 8by8
plt.show()