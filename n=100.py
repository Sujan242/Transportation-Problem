
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
for insta in range(480,640):
	print(insta+1)
	costs=ast.literal_eval(data['Costs'].iloc[insta])
	demand=ast.literal_eval(data['Demand'].iloc[insta])
	supply=ast.literal_eval(data['Supply'].iloc[insta])
	ls=len(supply)
	ld=len(demand)
	di = 0
	instance=insta%160
	# print((instance+1)/40)
	if int((instance)/40) == 0:
		di = 1 
	elif int((instance)/40) == 1:
		di = 2
	elif int((instance)/40 )== 2:
		di = 5
	else :
		di=10
	fan = (instance%40)
	cos=0
	if int(fan/10) ==0:
		cos=20
	elif int(fan/10)==1:
		cos=100
	elif int(fan/10)==2:
		cos=500
	else:
		cos=1000



	l1=["Plant"]+ 	list(range(1,ls+1))
	l2=["Capacity"] + list(supply.values())
	l3=["Customer"]+list(range(1,ld+1))
	l4=["Demand"] + list(demand.values())
	my_df=pd.DataFrame(costs)
	l5=[f"Instance {insta+1}",ls-ls%10,ld-ld%10,f"{100},{di},{cos},{(insta%10 +1)}"]
	# my_df.to_csv(f'converted{n}.csv', index=False, header=False)

	with open('n=100.csv','a',newline='') as fd:
		writer = csv.writer(fd)
		writer.writerow(l5)
	
	# with open('document.csv','a',newline='') as fd:
	# 	writer = csv.writer(fd)
	# 	writer.writerow(l1)
	with open('n=100.csv','a',newline='') as fd:
		writer = csv.writer(fd)
		writer.writerow(l2)	
	# with open('document.csv','a',newline='') as fd:
	# 	writer = csv.writer(fd)
	# 	writer.writerow(l3)
	with open('n=100.csv','a',newline='') as fd:
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