import matplotlib.pyplot as plt
import numpy as np
plt.figure()
X=np.arange(0,100,1)
Y=np.arange(0,100,1)
# plt.scatter(X,Y,marker=".")
# plt.show()
y=np.random.randint(0,100,(100,100))
plt.scatter(X,y[0])# tracer le nuance de point
plt.show()
