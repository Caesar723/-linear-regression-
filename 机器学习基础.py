import  pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as color
from sklearn import neighbors,datasets
import time
#kn=neighbors.KNeighborsClassifier()#临近算法knn
def target(data):#主要用在字符串数据
    arr = []

    uni=list(data.unique())
    #print(uni)
    for i in data:
        #print(i)
        arr.append(uni.index(str(i)))
    return pd.Series(arr)
def knn(data,mydata):#临近算法
    title=Df2Lis(data)
    #print(title)
    dis=0
    check=9999999999999999999999999999999999999999999999999999999999999999999
    index=0
    small=findsmall(title)
    max=findbig(title)
    spac=space(small,max)
    print(max)
    print((small))
    for i in range(len(title[0])):
        for ii in range(len(mydata)):
            #print(ii)
            dis=(title[ii][i]/small[ii]-mydata[ii]/small[ii])**2+dis
        if np.square(dis)<=check:
            #print("goood")
            check=np.square(dis)
            #print(check)
            index=i
        dis=0
    #print(index)
    return [title[len(title)-1][index],spac]
    #print(title[0])
def space(small,max):#求出一个数组最大和最小的过度
    arr=[]
    for i in range(len(small)):
        getar=(max[i]-small[i])/100
        array=np.arange(small[i]-getar,max[i]+getar,getar)
        #print(array)
        arr.append(array)
    return arr
def findsmall(list):#最小
    small=999999
    arr=[]
    for i in range(len(list)-1):
        for ii in list[i]:
            if(ii<small):
                small=ii
        arr.append(small)
        small=999999
    return arr
def findbig(list):#最大
    arr=[]
    for i in range(len(list) - 1):
        arr.append(pd.Series(list[i]).max())
    return arr
def Df2Lis(data):#把dataframe转成list
    if type(data)==list:
        return data
    else:
        arr=[]
        arr2=[]
        for i in list(data):
            for ii in data[str(i)]:
                #print(ii)
                arr2.append(ii)
            arr.append(arr2)
            arr2=[]
        return arr
def filter(data,name):#通过name把data中的数据提取出来
    arr={}
    for i in name:
        #print(i)
        arr[i]=(list(data[i]))
    return pd.DataFrame(arr)
def filrow(data):#把数据分成一横一横的
    da=Df2Lis(data)
    arr=[]
    ar=[]
    for i in range(len(da[0])):
        for ii in range(len(da)):
            ar.append(da[ii][i])
        arr.append(ar)
        ar=[]
    return np.array(arr)
def knn1():
    uri = "mostprise.csv"
    df = pd.read_csv(uri)
    kn = neighbors.KNeighborsClassifier()  # 临近算法knn
    arr = ["width", "length", "curb-weight", "engine-size", "num-of-cylinders2", "PriceRange"]
    final = filter(df, arr)
    all = knn(final, [50, 50, 1000, 200, 2])
    spa = all[1]
    print(spa)
    xx, yy = np.meshgrid(spa[2], spa[1])
    #print(xx,yy)
    grid = np.c_[xx.ravel(), yy.ravel()]
    kn.fit(filrow(filter(df,[ "curb-weight", "length"])),df["PriceRange"])
    #print(grid)
    z=kn.predict(grid)
    #print(z)
    plt.pcolormesh(xx,yy,np.array(target(pd.Series(z))).reshape(xx.shape),cmap=color.ListedColormap(["#FFAAAA","#AAFFAA","#AAAAFF"]))
    plt.scatter(final["curb-weight"],final["length"],c=target(final["PriceRange"]))

    plt.show()
    #print(kn.predict([[50,50,1000,200,2]]))
class xxhg:
    arr=[]
    coefficient=[]
    ready=[]
    res=0
    variance=0
    run=True
    count=0
    min=9*10**99
    tidu=0
    spacing=0.000000000000000000000001
    def train(self,data,result):

        for i in range(len(data[0])+1):
            self.coefficient.append(1)
            self.ready.append(0)

        while self.run:
            self.variance=0
            for iiiiiii in range(len(self.ready)):
                self.ready[iiiiiii]=0
            for ii in range(len(data)):
                self.res +=self.coefficient[0]
                for iii in range(len(data[ii])):
                    self.res+=(data[ii][iii]**(iii+1))*self.coefficient[iii+1]
                #print(self.res)
                self.variance+=(self.res-result[ii])**2

                for iiii in range(len(data[0])+1):
                    #print(self.res-result[ii])
                    self.ready[iiii]+=((self.res-result[ii])*(data[ii][(iiii-1 if iiii!=0 else 0)]**iiii))
                #print(self.ready)
                self.res=0
            for iiiii in range(len(data[0])+1):
                self.ready[iiiii]=self.ready[iiiii]/len(data)
            self.variance=self.variance/(2*len(data))
            #print(self.variance)
            if self.variance<self.min:
                if int(self.min)==int(self.variance):
                    break
                self.min=self.variance

                #print(self.min)
                #print("good")
                for iiiiii in range(len(data[0])+1):
                    self.coefficient[iiiiii]-=self.ready[iiiiii]*self.spacing
                #print(self.coefficient)
            else:
                self.spacing=self.spacing/1.5
                self.count+=1
                if self.count>1:
                    self.run=False
        print(self.coefficient)
def function(data,arr):
    price=0
    for i in range(len(arr)):
        price+=arr[i]*(data[i-1 if i!=0 else 0]**i)
    return price
uri = "mostprise.csv"
df = pd.read_csv(uri)
#print(df.info())
a=xxhg()
#print(filrow(filter(df,["curb-weight", "length","width","engine-size","city-mpg","wheel-base"])))
a.train(filrow(filter(df,["curb-weight", "length","width","engine-size","city-mpg","wheel-base"])),list(df["price"]))
#print(function([3750,200],[0.9817618490145733, 17.85934449872654, -1.0540663193467563]))

