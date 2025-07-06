import numpy as np
print(np.array ([1,2,3,4,5])+np.array ([1,2,3,4,5]))#行向量可以相加
print(np.zeros((3,2)))#3行2列的零矩阵
print(np.arange(3,7))#3-7范围内的元素组成的行向量
print(np.linspace(0,1,5))#第一个和第二个数字表示的是样本的区间范围，第三个数字表示的是样本的个数
print(np.random.rand(2,3))#随机数，逗号左右分别为随机生成矩阵的行数和列数，随机数数值在[0,1)中

a=np.zeros((4,2))
print(a.dtype)
#numpy默认定义为64位浮点型

a=np.zeros((4,2),dtype=np.int32)
print(a.dtype)
#强制更改数据类型

print(np.array([1,2,3,4,5])+np.array([3,2,4,5,8]))
print(np.array([1,4,9,16,25])/np.array([1,2,3,4,5]))
#矩阵的加减乘除

a=np.array([1,4,15,46,87])
b=np.array([3,7,45,12,4])
print(np.dot(a,b))#内积运算

a=np.array([[1,2],
            [3,4]])
b=np.array([[3,4],
            [5,6]])
print(a@b)#矩阵乘法