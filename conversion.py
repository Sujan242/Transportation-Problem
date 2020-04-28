
import pandas as pd 
from collections import defaultdict
import math
import csv
import copy
import json
import ast
data= pd.read_csv('input.csv')

output=[]
costs_list=[]
# my_df=pd.DataFrame()
n=0
for instance in range(10):
	print(instance+1)
	costs=ast.literal_eval(data['Costs'].iloc[instance])
	demand=ast.literal_eval(data['Demand'].iloc[instance])
	supply=ast.literal_eval(data['Supply'].iloc[instance])
	if len(supply)%10 ==1:
		del supply["S"+str(len(supply))]
		del costs["S"+str(len(supply)+1)]
	if len(demand)%10==1:
		del demand["D" + str(len(demand))]
		for x in supply:
			del costs[x]["D"+str(len(demand)+1)]
	l1=["Plant"]+ 	list(range(1,11))
	l2=["Capacity"] + list(supply.values())
	l3=["Customer"]+list(range(1,21))
	l4=["Demand"] + list(demand.values())
	my_df=pd.DataFrame(costs)
	l5=[f"Instance{instance+1}",10,20]
	my_df.to_csv(f'converted{n}.csv', index=False, header=False)

	with open('document.csv','a',newline='') as fd:
		writer = csv.writer(fd)
		writer.writerow(l5)
	
	with open('document.csv','a',newline='') as fd:
		writer = csv.writer(fd)
		writer.writerow(l1)
	with open('document.csv','a',newline='') as fd:
		writer = csv.writer(fd)
		writer.writerow(l2)	
	with open('document.csv','a',newline='') as fd:
		writer = csv.writer(fd)
		writer.writerow(l3)
	with open('document.csv','a',newline='') as fd:
		writer = csv.writer(fd)
		writer.writerow(l4)	
		writer.writerow([])
		writer.writerow(["Cost"])

		for x in supply :
			# r=[]+list()
			writer.writerow([""]+list(costs[x].values()))

		writer.writerow([])
		# writ




	n+=1