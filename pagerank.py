from numpy import *
a = array([[0,1,1,0],[1,0,0,1],[1,0,0,1],[1,1,0,0]],dtype=float)
#构造转移矩阵
def transPre(data):
    b = transpose(data) #把矩阵转置
    c = zeros((a.shape),dtype=float)
    #把所有的元素重新分配
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i][j] = data[i][j] / (b[j].sum())

    return c
# print(transPre(a))

def initiPre(c):
    # pr值的初始化
    pr = zeros((c.shape[0],1),dtype=float)
    for i in range(c.shape[0]):
        pr[i] = float(1)/c.shape[0]
    return pr
# print(initiPre(a))

def PageRank(p,m,v):
    #pageRank算法
    #p是网页跳转概率，m是转移矩阵，v是pr值
    while ((v == p*dot(m,v) + (1-p)*v).all() == False):
        v = p*dot(m,v) + (1-p)*v
        # print(v)
        print((v == p*dot(m,v) + (1-p)*v).all())
    return v
if __name__ == '__main__':
    M = transPre(a)
    pr = initiPre(M)
    p = 0.85
    print(PageRank(p,M,pr))