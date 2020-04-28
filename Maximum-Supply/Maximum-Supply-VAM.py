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
	
	            

	res = dict((k, defaultdict(int)) for k in costs)
	ls=len(supply)

	flag=0
	flagd=0
	sddd=""
	if ls%10==1:
		s="S"+ str(ls)
		sddd=s
		flagd=supply[s]
		del supply[s]
		ls=ls-1
		flag=1

	g={}
	for x in supply:
	    g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
	for x in demand:
	    g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])

	num=0
	while num<ls:
		num=num+1
		s={}
		for x in supply:
		    s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]])/(1.0*supply[x]) if len(g[x]) > 1 else costs[x][g[x][0]]/(1.0*supply[x])
		

		k=max(supply.items(), key=lambda x: x[1])
		# print(d)
		# print(k)
		sd=[]
		for x in supply:
			if supply[x]==k[1]:
				sd.append(x)
		ma=-1
		for x in sd :
			if s[x]>ma :
				ma=s[x]
		nd=[]
		for x in sd:
			if s[x]==ma :
				nd.append(x)
		dem="D"
		mi=1000000
		for x in nd :
			for y in demand:
				if (costs[x][y]) <mi :
					mi= (costs[x][y]) 
					dem = x 
	    
		# print(dem)
		while(supply[dem]>0):
			mi=100000
			mind="D"
	        
			for y in demand :
				if costs[dem][y]<mi:
					mi=costs[dem][y]
					mind=y
			v= min(supply[dem],demand[mind])
			res[dem][mind]+=v
			supply[dem]-=v 
			demand[mind]-=v
			if demand[mind] == 0:
				for k, n in supply.items():
				    if n != 0:
				        g[k].remove(mind)
				del g[mind]
				del demand[mind]
		
		for k, n in demand.items():
		    if n != 0:
		        g[k].remove(dem)
		del g[dem]
		del supply[dem]	   
		

	if flag==1:

		while flagd >0 :
			mi=100000
			mind="D"
			
			for y in demand:
				if costs[sddd][y]<mi:
					mi=costs[sddd][y]
					mind=y
			v= min(demand[mind],flagd)
			res[sddd][mind]+=v
			demand[mind]-=v 
			flagd-=v
			if demand[mind] == 0:
				for k, n in supply.items():
				    if n != 0:
				        g[k].remove(mind)
				del g[mind]
				del demand[mind]




	print(demand)	
	cost = 0
	for g in sorted(costs):
	    # print (g, "\t",)
	    for n in cols:
	        y = res[g][n]
	        if y != 0:
	        	pass
	            # print (y,)
	        cost += y * costs[g][n]
	        # print ("\t",)
	    # print()
	# print ("\n\nTotal Cost = ", cost)
	
	costs_list.append(cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('Max-supply-VOM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
