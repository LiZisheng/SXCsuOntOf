import pickle
from path  import *
#设置递归深度，为了解决数据存储问题
import sys
sys.setrecursionlimit(10000)


output = open(FileDir+'/data.pkl', 'rb')


data=pickle.load(output)

print(len(data))


output.close()
