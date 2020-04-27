
import pandas as pd 
data=pd.read_excel('Comparsion of costs.xlsx')

# print(data.iloc[:640,1])

vom = data.iloc[:640,1]
# print(vom[0],vom[639])

o=[]
for v in range(2,21):

	k= data.iloc[:640,v]
	# print(k)
	ng=0
	ne=0
	for i in range(640):
		if k[i]< vom[i]:
			ng=ng+1
		if k[i]==vom[i]:
			ne=ne+1
	o.append([ng,ne])
	
print(o)

print(len(o))


