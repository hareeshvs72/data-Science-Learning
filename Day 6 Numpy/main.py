
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(np.__version__)


#check dimension of array 

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


a1 = np.array([1,2,3,4,5,6],ndmin=5)
print("number of dimention " ,a1.ndim)


# array itrating 

arr = np.array( [1,2,3,4,5])
for x in np.nditer(arr) :
   print(x*4)
   
arr1 = np.array([5, 10, 15])

for index, value in np.ndenumerate(arr1):
    print(index, value)
    
    
# array sum , mean ,zero

arr = np.array([1, 2, 3, 4])

print(np.sum(arr))
arr = np.array([1, 2, 3, 4])
print(np.sum(arr))
print(np.mean(arr))
print(np.zeros(arr))