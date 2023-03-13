import numpy as np 



# listNest = [[1, 2], [3, 4], [5, 6]]
# print(np.array(listNest))

# print(np.arange(0, 11, 2))
# print(np.zeros((4,4)))
# print(np.eye(5))
# print(np.random.randn(3, 4))

# np.random.seed(42)
# print(np.random.rand(4))

arr = np.arange(25)



arr = np.arange(0, 11)
arr[0:5] = 100
arrcopy = arr.copy()

# print(arrcopy)


arr =  np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
# print(arr.shape)
# print(arr > 25)

arr = np.arange(0, 11)

# print(np.sin(arr))

arr = np.arange(0, 25).reshape(5, 5)
print(arr.sum(axis=0))


