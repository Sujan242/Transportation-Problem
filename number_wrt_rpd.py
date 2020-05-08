import pandas as pd 
data=pd.read_csv('RPD.csv',header=None)

num=[[0 for _ in range(32)] for _ in range(5)]

ls=[[],[]]
for i in range(640):

	for m in range(32):
		v=float(data.iloc[i,m])
		if m==2 or m==3:
			if abs(v)<=0.000006:
				ls[m-2].append(i)



		
		if abs(v-0)<=0.000006 :
			num[0][m]+=1
		elif v<=0.5:
			num[1][m]+=1
		elif v<=1:
			num[2][m]+=1
		elif v<=2:
			num[3][m]+=1
		elif v<=3:
			num[4][m]+=1


# print(len(ls[0]), len(ls[1]))
print(ls)
# import csv
# from itertools import zip_longest
# d = num
# # d=list(map(list, zip(*d)))
# # d=list(map(list, zip(*d)))
# export_data = zip_longest(*d, fillvalue = '')
# with open('number_wrt_arpd.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
#       wr = csv.writer(myfile)
#       #wr.writerow(("SIZE", "ERT","LPT ","EDD","ODD", "FDD","CGH_LST","CI","SIZE-ANN","ERT-ANN","LPT-ANN","EDD-ANN","ODD-ANN","FDD-ANN","ANN-LST",))
#       wr.writerows(export_data)
# myfile.close()


