import numpy as np

print(np.array ([1,2,3,4,5]))#行向量的生成

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
print(np.sqrt(a))#对矩阵元素做开根运算

print(np.sin(a))
print(np.cos(b))
#对矩阵进行三角函数运算

print(np.power(a,2))
print(np.log(b) / np.log(10))
#对矩阵进行指对运算，注意指数运算还要说明指数是多少,若要说明log的指数，则要用换底公式来表达
print((np.array([1,2,3]))*5)
#数乘的运算，在numpy也称为广播

a=np.array([[1],
           [2],
           [3]])
b=np.array([4,5,6])
print(a+b)
"""注意！！当a,b的矩阵形状不同时，会把a扩成为 [1,1,1]的形式，b也同理，
                                        [2,2,2|
                                        [3,3,3]
再通过3*3的矩阵加法进行运算
"""
print(np.max(a))
print(np.min(a))
#返回矩阵中最小或最大的元素

print(np.argmax(a),np.argmin(a))
#返回矩阵中最小或最大元素的索引（如1元素位于第一行，返回第一行的序数）

print(np.sum(a))
#返回样本的总和

a=np.array([1,2,3,4,5])
print(np.median(a))
print(a.mean())
#返回a的平均值

print(a.var())
print(a.std())
#返回a的方差和标准方差

a=np.array([[1,2,3,4,5],
           [6,7,8,9,0]])
print(a.sum(axis=0))
#axis为张量的维度，axis=0时，以行为基准，按每一列的元素进行求和
#同理axis=1时，以列为基准，按每一行的元素进行求和，矩阵为2个元素的向量
#元素分别为15,30

a=np.array([1,2,3,4,5])
print(a[(a>3)&(a%2==0)])