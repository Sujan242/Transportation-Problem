import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
data= pd.read_csv('input.csv')

output=[]
costs_list=[]
for instance in range(640):
	print(instance+1)
	costs=ast.literal_eval(data['Costs'].iloc[instance])
	demand=ast.literal_eval(data['Demand'].iloc[instance])
	supply=ast.literal_eval(data['Supply'].iloc[instance])
	cols = sorted(demand.keys())
	costs1=copy.deepcopy(costs)
	# print(supply['S1'])
	# break
	# costs1=copy.deepcopy(costs)

	costs2=copy.deepcopy(costs)
	costs3=copy.deepcopy(costs)
	ma=0 
	for i in supply:
		for j in demand:
			ma=max(ma,costs[i][j])
	
	
	for i in supply:
		for j in demand:
			if costs[i][j]!=0:
				costs[i][j]=costs[i][j]/ma 
	            

	res = dict((k, defaultdict(int)) for k in costs)
	g = {}
	for x in supply:
	    g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
	for x in demand:
	    g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])
	# print(costs1)
	flag=0
	while g:
	   
	    d = {}
	    # print(demand,supply)

	    for x in demand:
	        d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x])/(1.0*demand[x]) if len(g[x]) > 1 else (costs[g[x][0]][x])/(1.0*demand[x])
	    s = {}
	    for x in supply:
	        s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]])/(1.0*supply[x]) if len(g[x]) > 1 else costs[x][g[x][0]]/(1.0*supply[x])
	    f = max(d, key=lambda n: d[n])
	    t = max(s, key=lambda n: s[n])
	    # print(d,s,"ds")
	    t1, f1 , maxp= (f, g[f][0] , d[f]) if d[f] > s[t] else (g[t][0], t , s[t])
	    v = min(supply[f1], demand[t1])
	    # print(f1,t1)
	    
	    m1= maxp* costs[f1][t1]
	    # print(m1)
	    # print(costs1[f1][t1])
	    kd=copy.deepcopy(d)
	    
	    del kd[f]
	    ks=copy.deepcopy(s)
	    del ks[t]
	    # t,f=t1,f1
	    tfin , fin = t1,f1
	    if(kd):
	        fm = max(kd, key=lambda n: kd[n])
	        if(d[fm]>s[t]):
	            t2,f2= fm,g[fm][0]
	            v = min(supply[f2], demand[t2])
	            if( d[fm]*costs[f2][t2] > m1):
	                tfin , fin = t2,f2
	                m1=costs[f2][t2]*d[fm]
	                # v = min(supply[f], demand[t])
	        else :
	            t2,f2= g[t][0] , t 
	            if s[t]*costs[f2][t2]>m1 :
	                tfin , fin = t2,f2 
	                m1=costs[f2][t2]* s[t]
	    
	    if(ks):
	        sm=max(ks, key=lambda n: ks[n])
	        # print(sm)
	        if (s[sm]>d[f]):
	            
	            t3,f3 = g[sm][0] , sm
	            v = min(supply[f3], demand[t3])
	            if(s[sm]*costs[f3][t3]>m1):
	                tfin , fin = t3,f3
	        else :
	            t3,f3 = f,g[f][0]
	            if s[sm]*costs[f3][t3]>m1 :
	                tfin, fin = t3,f3
	                
	    t,f=tfin,fin
	    # print(t,f)
	    v = min(supply[f], demand[t])        
	    res[f][t] += v
	    demand[t] -= v
	    
	    if demand[t] == 0:
	        for k, n in supply.items():
	            if n != 0:
	                g[k].remove(t)
	        del g[t]
	        del demand[t]
	    supply[f] -= v
	    if supply[f] == 0:
	        for k, n in demand.items():
	            if n != 0:
	                g[k].remove(f)
	        del g[f]
	        del supply[f]
	    
	 
	# print(costs1)
	cost = 0
	for g in sorted(costs1):
	    # print (g, " ",)
	    for n in cols:
	        y = res[g][n]
	        if y != 0:
	            pass
	            # print (y,)
	        cost += y * costs1[g][n]
	        # print ("  ",)
	    # print(" ")
	# print ("Total Cost = ", cost)
	
	costs_list.append(cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('Max-TOM-costperunit.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
