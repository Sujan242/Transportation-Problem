import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
costs  = {'S1': {'D1': 494, 'D2': 491, 'D3': 509, 'D4': 506, 'D5': 494, 'D6': 509, 'D7': 498, 'D8': 491, 'D9': 503, 'D10': 490, 'D11': 495, 'D12': 492, 'D13': 506, 'D14': 499, 'D15': 491, 'D16': 494, 'D17': 495, 'D18': 490, 'D19': 498, 'D20': 503, 'D21': 0}, 'S2': {'D1': 500, 'D2': 495, 'D3': 496, 'D4': 509, 'D5': 495, 'D6': 509, 'D7': 500, 'D8': 497, 'D9': 490, 'D10': 491, 'D11': 491, 'D12': 508, 'D13': 490, 'D14': 497, 'D15': 494, 'D16': 502, 'D17': 502, 'D18': 497, 'D19': 494, 'D20': 499, 'D21': 0}, 'S3': {'D1': 490, 'D2': 493, 'D3': 497, 'D4': 491, 'D5': 498, 'D6': 495, 'D7': 494, 'D8': 509, 'D9': 499, 'D10': 493, 'D11': 503, 'D12': 502, 'D13': 496, 'D14': 492, 'D15': 499, 'D16': 506, 'D17': 502, 'D18': 496, 'D19': 500, 'D20': 498, 'D21': 0}, 'S4': {'D1': 499, 'D2': 496, 'D3': 503, 'D4': 509, 'D5': 495, 'D6': 496, 'D7': 496, 'D8': 490, 'D9': 501, 'D10': 502, 'D11': 498, 'D12': 504, 'D13': 503, 'D14': 494, 'D15': 501, 'D16': 508, 'D17': 500, 'D18': 493, 'D19': 504, 'D20': 503, 'D21': 0}, 'S5': {'D1': 506, 'D2': 503, 'D3': 507, 'D4': 494, 'D5': 507, 'D6': 509, 'D7': 499, 'D8': 499, 'D9': 503, 'D10': 501, 'D11': 501, 'D12': 492, 'D13': 503, 'D14': 506, 'D15': 504, 'D16': 490, 'D17': 493, 'D18': 504, 'D19': 493, 'D20': 492, 'D21': 0}, 'S6': {'D1': 495, 'D2': 509, 'D3': 503, 'D4': 492, 'D5': 509, 'D6': 492, 'D7': 491, 'D8': 495, 'D9': 493, 'D10': 493, 'D11': 509, 'D12': 502, 'D13': 508, 'D14': 506, 'D15': 509, 'D16': 506, 'D17': 506, 'D18': 508, 'D19': 498, 'D20': 498, 'D21': 0}, 'S7': {'D1': 495, 'D2': 503, 'D3': 506, 'D4': 501, 'D5': 509, 'D6': 499, 'D7': 500, 'D8': 490, 'D9': 500, 'D10': 505, 'D11': 495, 'D12': 497, 'D13': 500, 'D14': 508, 'D15': 493, 'D16': 492, 'D17': 492, 'D18': 495, 'D19': 491, 'D20': 502, 'D21': 0}, 'S8': {'D1': 504, 'D2': 501, 'D3': 491, 'D4': 493, 'D5': 493, 'D6': 498, 'D7': 508, 'D8': 504, 'D9': 505, 'D10': 490, 'D11': 497, 'D12': 492, 'D13': 494, 'D14': 496, 'D15': 502, 'D16': 497, 'D17': 503, 'D18': 505, 'D19': 508, 'D20': 505, 'D21': 0}, 'S9': {'D1': 505, 'D2': 500, 'D3': 492, 'D4': 501, 'D5': 507, 'D6': 497, 'D7': 497, 'D8': 496, 'D9': 498, 'D10': 504, 'D11': 498, 'D12': 499, 'D13': 494, 'D14': 507, 'D15': 502, 'D16': 491, 'D17': 490, 'D18': 496, 'D19': 494, 'D20': 505, 'D21': 0}, 'S10': {'D1': 490, 'D2': 504, 'D3': 492, 'D4': 497, 'D5': 499, 'D6': 509, 'D7': 506, 'D8': 507, 'D9': 506, 'D10': 495, 'D11': 505, 'D12': 509, 'D13': 502, 'D14': 494, 'D15': 491, 'D16': 507, 'D17': 507, 'D18': 500, 'D19': 494, 'D20': 506, 'D21': 0}}


demand = {'D1': 91, 'D2': 124, 'D3': 103, 'D4': 100, 'D5': 114, 'D6': 75, 'D7': 79, 'D8': 77, 'D9': 104, 'D10': 113, 'D11': 103, 'D12': 112, 'D13': 96, 'D14': 76, 'D15': 84, 'D16': 113, 'D17': 124, 'D18': 101, 'D19': 97, 'D20': 76, 'D21': 20}

cols = sorted(demand.keys())
supply = {'S1': 201, 'S2': 226, 'S3': 208, 'S4': 214, 'S5': 222, 'S6': 156, 'S7': 209, 'S8': 174, 'S9': 220, 'S10': 152}
summ=0
for x in supply:
	summ+= supply[x]
res = dict((k, defaultdict(int)) for k in costs)
ld=len(demand)

flag=0
flagd=0
sddd=""
if ld%10==1:
	s="D"+ str(ld)
	sddd=s
	flagd=demand[s]
	del demand[s]
	ld=ld-1
	flag=1

g={}
for x in supply:
    g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
for x in demand:
    g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])

num=0
while num<ld:
	num=num+1
	dem="D"
	mi2=100000000
	for x in demand:
		supply1=copy.deepcopy(supply)
		cst=0
		ful=demand[x]
		while(ful>0):
			mi=100000
			mind="D"
		       
			for y in supply1 :
				if costs[y][x]<mi:
					mi=costs[y][x]
					mind=y
			v= min(supply1[mind],ful)
			
			cst=cst+ v* costs[mind][x]
			supply1[mind]-=v 
			ful-=v
			if supply1[mind] == 0:
			    
			        
			    # del g[mind]
			    del supply1[mind]
		# print()
		# print(x,cst/(1.0*demand[x]))
		if (cst/(1.0*demand[x])) <=mi2 :
			mi2 = (cst/(1.0*demand[x]))
			dem = x 
	# print(dem)
	# break
	while(demand[dem]>0):
		mi=100000
		mind="D"
	       
		for y in supply :
			if costs[y][dem]<mi:
				mi=costs[y][dem]
				mind=y
		v= min(supply[mind],demand[dem])
		res[mind][dem]+=v
		supply[mind]-=v 
		demand[dem]-=v
		if supply[mind] == 0:
		    
		    del supply[mind]
	
	del demand[dem]
	# break

	






if flag==1:

	while flagd >0 :
		mi=100000
		mind="D"
		
		for y in supply :
			if costs[y][sddd]<mi:
				mi=costs[y][sddd]
				mind=y
		v= min(supply[mind],flagd)
		res[mind][sddd]+=v
		supply[mind]-=v 
		flagd-=v
		if supply[mind] == 0:
		    for k, n in demand.items():
		        if n != 0:
		            g[k].remove(mind)
		    del g[mind]
		    del supply[mind]

smm=0
for x in res.keys():
	for y in res[x].keys():
		smm=smm+ res[x][y]

print(smm,summ)
print(supply,demand)	
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
print ("\n\nTotal Cost = ", cost)



	


