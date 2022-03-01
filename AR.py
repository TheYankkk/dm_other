#print("test")
import pandas as pd
import math
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
d=[["a"],["a","b"],["b","c"],["a","b","d"]]
"""
for each in range(len(d)):
    d[each][0]="BI-RADS:"+d[each][0]
    d[each][1] = "Age:" + d[each][1]
    d[each][2] = "Shape:" + d[each][2]
    d[each][3] = "Margin:" + d[each][3]
    d[each][4] = "Density:" + d[each][4]
    d[each][-1]="Severity:"+str(d[each][-1])
#print(d)
"""
te = TransactionEncoder()
te_ary = te.fit(d).transform(d)
#print(te.columns_)
df = pd.DataFrame(te_ary,columns=te.columns_)
#print(df)

#computing frequent itemsets and association rules
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

a=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.9)

#visualizing association rules results
print(a[["antecedents","consequents","support","confidence"]])
"""
#Question 2
dnew=[]
for each in range(len(d)):
    dnew.append(d[each][1:])
#print(dnew)
te_new = TransactionEncoder()
te_ary_new = te_new.fit(dnew).transform(dnew)
#print(te.columns_)
df_new = pd.DataFrame(te_ary_new,columns=te_new.columns_)
print(df_new)
frequent_itemsets_new = apriori(df_new, min_support=0.1, use_colnames=True)
#print(frequent_itemsets_new)
a=association_rules(frequent_itemsets_new, metric="confidence", min_threshold=0.9)
#print(a[["antecedents","consequents","support","confidence"]])
#"Severity:1"in a["antecedents"][i] or "Severity:0"in a["antecedents"][i]or

for i in range(len(a["antecedents"])):
    if ("Severity:1" in a["consequents"][i] or "Severity:0" in a["consequents"][i]):
        print(a["antecedents"][i],":",a["consequents"][i])


#Question 3
special_itemsets = apriori(df, min_support=0.002, use_colnames=True)
s=association_rules(special_itemsets, metric="confidence", min_threshold=0)
#print(a)
for i in range(len(s)):
    if ("BI-RADS:0" in s["antecedents"][i] and "Severity:1" in s["consequents"][i]):
        print("\n",s["antecedents"][i],":",s["consequents"][i])

#Question 4
frequent_itemsets = apriori(df, min_support=0.001, use_colnames=True)
a=association_rules(frequent_itemsets, metric="confidence", min_threshold=0)
for i in range(len(a)):
    if (a["antecedents"][i]==frozenset({'Age:35'}) and a["consequents"][i])==frozenset({'Severity:0'}):
        print(a["antecedents"][i],":",a["consequents"][i],",Support:",a["support"][i],",Confidence:,",a["confidence"][i])


#Question 5
data=pd.read_csv(r"mammographic_masses.csv",delimiter=",",header=0)
#print(data)
#index_special=data[data['Age'].isin(["?"])].index.tolist()
#give up the method above
#print(index_special)
#data_new=data.drop(index_special)#drop the rows with Age is ?
d_num=data.values.tolist()
sum=0
for each in range(len(d_num)):
    d_num[each][0]="BI-RADS:"+d_num[each][0]
    if d_num[each][1]!="?":
        d_num[each][1] = int(d_num[each][1])
        sum+=d_num[each][1]
    d_num[each][2] = "Shape:" + d_num[each][2]
    d_num[each][3] = "Margin:" + d_num[each][3]
    d_num[each][4] = "Density:" + d_num[each][4]
    d_num[each][-1]="Severity:"+str(d_num[each][-1])
mean=sum/len(d_num)
mean=int(mean)
#print(mean)
for each in range(len(d_num)):
    if d_num[each][1]=="?":
        d_num[each][1]="Age<="+str(mean)
    elif d_num[each][1]>mean:
        d_num[each][1] = "Age>"+str(mean)
        #print(d_num[each][1])
    else:
        d_num[each][1] = "Age<=" + str(mean)

te = TransactionEncoder()
te_ary = te.fit(d_num).transform(d_num)
#print(te.columns_)
df = pd.DataFrame(te_ary,columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)
a=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.9)
print(a[["antecedents","consequents","support","confidence"]])
"""