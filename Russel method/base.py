import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
from math import sqrt
from statistics import stdev 
costs  = {"S1":{"D1":73,"D2":40,"D3":9,"D4":79 ,"D5":20,},"S2":{"D1":62,"D2":93,"D3":96,"D4":8 ,"D5":13,},"S3":{"D1":96,"D2":65,"D3":80,"D4":30 ,"D5":65,},"S4":{"D1":57,"D2":58,"D3":29,"D4":12 ,"D5":87,},"S5":{"D1":56,"D2":23,"D3":87,"D4":18 ,"D5":12,}}

demand = {"D1":6,"D2":8,"D3":10,"D4":4 ,"D5":4,}
cols = sorted(demand.keys())
supply ={"S1":8,"S2":7,"S3":9,"S4":3,"S5":5}
costs1=copy.deepcopy(costs)
# print(supply['S1'])
# break
# costs1=copy.deepcopy(costs)

costs2=copy.deepcopy(costs)
costs3=copy.deepcopy(costs)

# for i in supply:
# 	mi=min(costs[i].values())
# 	# print(costs[i])
# 	# print(mi)
# 	for j in costs2[i]:
# 		costs2[i][j]-=mi
# # print(costs2)
# for i in demand :
# 	mi=10000
# 	for j in supply:
# 		if costs[j][i]<mi :
# 			mi=costs[j][i]
# 	for j in supply:
# 		costs3[j][i]=costs3[j][i]-mi 
# # print(costs3)

# for i in demand:
# 	for j in supply:
# 		costs[j][i]= costs2[j][i]+costs3[j][i]

			

res = dict((k, defaultdict(int)) for k in costs)
g = {}
for x in supply:
	g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g], reverse=True)
for x in demand:
	g[x] = sorted(costs.keys(), key=lambda g: costs[g][x] , reverse=True)
g1={}
for x in supply:
	g1[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
for x in demand:
	g1[x] = sorted(costs.keys(), key=lambda g: costs[g][x] )

# print(costs1)
flag=0
while supply and demand:
   
	d = {}
	# print(demand,supply)
	for x in demand:
		d[x] = (costs[g1[x][0]][x]*costs[g[x][0]][x]) 
	# s = {}
	for x in supply:
		d[x] = (costs[x][g1[x][0]]*costs[x][g[x][0]]) 

	# print(d)
	f = max(d, key=lambda n: d[n])
	# print(f)
	
	# break
	t="D"
	if demand.get(f)!=None:

		t, f= (f, g1[f][0] )
	else:
		t,f = (g1[f][0], f)
	v = min(supply[f], demand[t])        
	res[f][t] += v
	demand[t] -= v
	
	if demand[t] == 0:
		for k, n in supply.items():
			if n != 0:
				g[k].remove(t)
				g1[k].remove(t)
		del g[t]
		del g1[t]
		del demand[t]
	supply[f] -= v
	if supply[f] == 0:
		for k, n in demand.items():
			if n != 0:
				g[k].remove(f)
				g1[k].remove(f)
		del g[f]
		del g1[f]
		del supply[f]

print(demand,supply)	
 
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
print ("Total Cost = ", cost)