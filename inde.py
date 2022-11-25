# import matplotlib.pyplot as plt
# import numpy as np
# a=np.linspace(0,10,50)
# b=np.linspace(3,15,50)
# c=a+b
# q=a*b
# print(c)
# print(q)

# a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a)
# #a[0,0]
# print(a[:,0])
# print(a<9)
# print(a[a<9])

# import matplotlib.pyplot as plt
# import numpy as np
# T=np.random.randint(0,50,(5,5))
# print(T)
# B=print(T[1:4,1:4])
# C=print(T[::2])#le nombre de ligne en commencant par 1 
# D=print(T[:,::2])
# E=T.shape# la taille de la matrice
# print(E)
# A=T.size# le nombre d'element de la matrice
# print(A)
# Ce=np.random.randint(0,50,(5,5))
# print(Ce)
# produit=T.dot(Ce)# le produit matriciel
# print(produit)
# z=np.transpose(produit)# transposer d'une matrix
# print(z)

# def f(x):
#     return (x*x-2*x)
# x=np.arange(0,20,1)
# print(f(x))
# y=np.sin(x)
# x=x=np.arange(0,20,1)
# plt.figure()
# plt.plot(x,f(x))
# plt.plot(x,np.exp(x))
# plt.show()
import matplotlib.pyplot as plt
import numpy as np
plt.figure()
X=Y=np.arange(0,100,1)
plt.scatter(X,Y)
plt.show




    
    
