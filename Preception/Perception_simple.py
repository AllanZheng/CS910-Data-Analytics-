from matplotlib import pyplot as plt
import numpy as np
dataSet = [[1,1],[2,1],[3,-1],[4,-1]]

w = 0
b = 0
bo =1
while bo:
    bo =0
    for i in dataSet:
        if((w*i[0]+b)*i[1]<=0):
            bo = 1
            w += i[0]*i[1]
            b += i[1]

print(w,b)
dataSet = np.mat(dataSet)
print(dataSet[:,0])
f1 =plt.figure()
axe =f1.add_subplot(111)
dataSet[:,1]=0
axe.scatter([dataSet[0:2,0]],[dataSet[0:2,1]],color='red')
axe.scatter([dataSet[2:4,0]],[dataSet[2:4,1]],color='green')
plt.plot([(-b/w),0],[0,b])
plt.show()