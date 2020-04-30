import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
from math import sqrt
from statistics import stdev 
costs  = {'S1': {'D1': 503, 'D2': 494, 'D3': 492, 'D4': 494, 'D5': 490, 'D6': 503, 'D7': 495, 'D8': 502, 'D9': 500, 'D10': 495, 'D11': 508, 'D12': 496, 'D13': 497, 'D14': 490, 'D15': 490, 'D16': 506, 'D17': 508, 'D18': 493, 'D19': 505, 'D20': 507}, 'S2': {'D1': 492, 'D2': 506, 'D3': 501, 'D4': 507, 'D5': 502, 'D6': 501, 'D7': 493, 'D8': 503, 'D9': 506, 'D10': 494, 'D11': 493, 'D12': 507, 'D13': 494, 'D14': 498, 'D15': 491, 'D16': 490, 'D17': 490, 'D18': 505, 'D19': 506, 'D20': 502}, 'S3': {'D1': 505, 'D2': 509, 'D3': 502, 'D4': 497, 'D5': 495, 'D6': 507, 'D7': 496, 'D8': 505, 'D9': 496, 'D10': 505, 'D11': 496, 'D12': 509, 'D13': 495, 'D14': 497, 'D15': 502, 'D16': 493, 'D17': 502, 'D18': 497, 'D19': 494, 'D20': 509}, 'S4': {'D1': 506, 'D2': 507, 'D3': 508, 'D4': 498, 'D5': 494, 'D6': 503, 'D7': 491, 'D8': 493, 'D9': 502, 'D10': 490, 'D11': 495, 'D12': 491, 'D13': 507, 'D14': 505, 'D15': 504, 'D16': 502, 'D17': 501, 'D18': 490, 'D19': 504, 'D20': 495}, 'S5': {'D1': 490, 'D2': 504, 'D3': 491, 'D4': 497, 'D5': 504, 'D6': 498, 'D7': 492, 'D8': 500, 'D9': 495, 'D10': 503, 'D11': 508, 'D12': 498, 'D13': 498, 'D14': 505, 'D15': 509, 'D16': 502, 'D17': 508, 'D18': 502, 'D19': 498, 'D20': 497}, 'S6': {'D1': 507, 'D2': 494, 'D3': 492, 'D4': 494, 'D5': 501, 'D6': 500, 'D7': 496, 'D8': 494, 'D9': 502, 'D10': 493, 'D11': 490, 'D12': 507, 'D13': 494, 'D14': 506, 'D15': 504, 'D16': 496, 'D17': 500, 'D18': 507, 'D19': 508, 'D20': 495}, 'S7': {'D1': 502, 'D2': 504, 'D3': 509, 'D4': 500, 'D5': 492, 'D6': 506, 'D7': 501, 'D8': 508, 'D9': 491, 'D10': 509, 'D11': 509, 'D12': 491, 'D13': 499, 'D14': 494, 'D15': 505, 'D16': 505, 'D17': 498, 'D18': 498, 'D19': 507, 'D20': 492}, 'S8': {'D1': 508, 'D2': 509, 'D3': 504, 'D4': 506, 'D5': 491, 'D6': 504, 'D7': 501, 'D8': 495, 'D9': 490, 'D10': 509, 'D11': 505, 'D12': 501, 'D13': 494, 'D14': 490, 'D15': 506, 'D16': 498, 'D17': 509, 'D18': 496, 'D19': 505, 'D20': 495}, 'S9': {'D1': 499, 'D2': 501, 'D3': 490, 'D4': 497, 'D5': 508, 'D6': 492, 'D7': 496, 'D8': 492, 'D9': 497, 'D10': 493, 'D11': 507, 'D12': 509, 'D13': 498, 'D14': 508, 'D15': 494, 'D16': 495, 'D17': 496, 'D18': 493, 'D19': 508, 'D20': 496}, 'S10': {'D1': 493, 'D2': 492, 'D3': 509, 'D4': 494, 'D5': 504, 'D6': 492, 'D7': 506, 'D8': 497, 'D9': 493, 'D10': 494, 'D11': 504, 'D12': 505, 'D13': 492, 'D14': 502, 'D15': 504, 'D16': 491, 'D17': 498, 'D18': 494, 'D19': 509, 'D20': 505}, 'S11': {'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0, 'D8': 0, 'D9': 0, 'D10': 0, 'D11': 0, 'D12': 0, 'D13': 0, 'D14': 0, 'D15': 0, 'D16': 0, 'D17': 0, 'D18': 0, 'D19': 0, 'D20': 0}}


demand = {'D1': 84, 'D2': 124, 'D3': 95, 'D4': 113, 'D5': 118, 'D6': 120, 'D7': 104, 'D8': 99, 'D9': 75, 'D10': 116, 'D11': 122, 'D12': 95, 'D13': 95, 'D14': 75, 'D15': 91, 'D16': 115, 'D17': 119, 'D18': 79, 'D19': 98, 'D20': 95}

cols = sorted(demand.keys())
supply ={'S1': 166, 'S2': 166, 'S3': 168, 'S4': 243, 'S5': 158, 'S6': 232, 'S7': 165, 'S8': 235, 'S9': 176, 'S10': 167, 'S11': 156}

res = dict((k, defaultdict(int)) for k in costs)

rij={}
for x in supply:
	dd={}
	for y in demand:
		dd[y]=0
	rij[x]=dd 

for x in supply:
	for y in demand:
		rij[x][y]= supply[x]/demand[y] 
# print(rij)
for x in supply:
	for y in demand:
		rij[x][y]*=costs[x][y]

print(rij)

while supply or demand:
	mi=10000000000000
	l=[]
	for x in supply:
		for y in demand:
			if rij[x][y]<mi:
				mi=rij[x][y]
				l=[x,y]

	sup=l[0]
	dem=l[1]
	v=min(supply[sup],demand[dem])
	demand[dem]-=v
	supply[sup]-=v
	res[sup][dem]+=v
	if supply[sup]==0:
		del supply[sup]
	if demand[dem]==0:
		del demand[dem]

	


print(demand,supply)

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
