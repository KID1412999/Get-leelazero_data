import requests
import json
st=[]
url='http://null:null@zero.sjeng.org/data/elograph.json'
html=requests.get(url)
t=html.text
t= json.loads(t)
for i in range(len(t)):
	if t[i]['best']==True:
		print(t[i])
		st.append(str(t[i]['net'])+'>'+str(t[i]['rating'])+'>'+str(t[i]['hash']))
print(st)
f=open('E:\\leelazero_data.txt','w')
f.write('训练数量'+'>'+'Elo值'+'>'+'权重名'+'\n')
for i in range(len(st)):
	f.write(st[i]+'\n')
f.close()
print('请打开E://leelazero_data.txt查看数据!')
