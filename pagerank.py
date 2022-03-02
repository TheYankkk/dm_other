from numpy import *
#
#构造转移矩阵a = array([[0,0,0,1],[0.5,0,0,0],[1/2,1,0,0],[0,0,1,0]],dtype=float)
a = array([[1/2,1/2,0],[1/2,0,0],[0,1/2,1]],dtype=float)
def transPre(data):
    b = transpose(data) #把矩阵转置
    c = zeros((a.shape),dtype=float)
    #把所有的元素重新分配
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i][j] = 1 / a.shape[1]

    return c
# print(transPre(a))

def initiPre(c):
    # pr值的初始化
    pr = zeros((c.shape[0],1),dtype=float)
    for i in range(c.shape[0]):
        pr[i] = float(1)/c.shape[0]
    print("this is pr:",pr)
    return pr
# print(initiPre(a))

def PageRank(p,m,v):
    #pageRank算法
    #p是网页跳转概率，m是转移矩阵，v是pr值
    i=0
    ori=m
    while ((v == p*dot(a,v) + (1-p)*ori).all() == False):
        v = dot(p*a+(1-p)*ori,v)
        # print(v)
        #print((v == p*dot(m,v) + (1-p)*v).all())

        if i<=20:#迭代次数
            print("第%d次:" % (i + 1), v)

        elif i==100:
            break
        i += 1


    return v
if __name__ == '__main__':
    M = transPre(a)
    pr = initiPre(M)
    p = 0.8#β的值
    print(PageRank(p,M,pr))