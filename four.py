import numpy as np
#list="1 3 4 5 6 7"
#print(list[1:-1])
'''data =list.split(" ")
embedding = np.array([float(num) for num in data[1:-1]])
print(embedding)
dict={}
word=["er","ty","er","gb"]
print(len(dict))
dict[word[0]]=len(dict)
print(dict)
print(len(dict))

dict[word[1]]=len(dict)
print(dict)
print(len(dict))

dict[word[2]]=len(dict)
print(dict)
print(len(dict))

dict[word[3]]=len(dict)
print(dict)
print(len(dict))'''
'''
embedding_list=[]
data="2 3 4 5 6 7"
ll=data.split(" ")
print(ll)
embedding=np.array([float(num) for num in ll[1:-1]])
print(embedding)
embedding_list.append(embedding)
data2="24 36 47 55 67 7o"
l2=data2.split(" ")
embedding1=np.array([float(num) for num in l2[1:-1]])

embedding_list.append(embedding1)
data3="45 34 67 78 89 90"
l3=data3.split(" ")
embedding2=np.array([float(num) for num in l3[1:-1]])


embedding_list.append(embedding2)
data4="45 67 78 89 80"
l4=data4.split(" ")

embedding3=np.array([float(num) for num in l4[1:-1]])
embedding_list.append(embedding3)
#print(embedding_list)
embedding_list = np.array(embedding_list)
#print(embedding_list)
embedding_size=3
#embedding_list.append([0.] * embedding_size)
print(embedding_list)
cleared_embedding_list=[]
row=embedding_list[0]
cleared_embedding_list.append(row)
row2=embedding_list[1]
cleared_embedding_list.append(row2)
row3=embedding_list[2]
cleared_embedding_list.append(row3)
print(cleared_embedding_list)
cleared_embedding_list.append([0.] * embedding_size)
print("ggg:",cleared_embedding_list)
cleared_embedding_list.append([-1.] * embedding_size)
print("rrr:", cleared_embedding_list)
embedding_matrix = np.array(cleared_embedding_list)
print("embedding_matrix:",embedding_matrix)
print("embedding_matrix.shape[0]:",embedding_matrix.shape[0])
#print(len(embedding_list[0]))'''

'''dict1={'my':0,'mother':1,'I':2,'love':3,'you':4}
id_to_word = dict((id, word) for word, id in dict1.items())
print(id_to_word)'''
'''
l1=[]
s1="0.23 0.23 -0.56 0.36 0.21"
s2="0.523 0.723 -0.566 0.936 0.821"
s3="0.623 -0.23 -0.856 0.736 0.621"
s4="0.723 0.123 -0.756 0.436 0.621"
data1=s1.split(" ")
data2=s2.split(" ")
data3=s3.split(" ")
data4=s4.split(" ")
e1=np.array([float(num) for num in data1[1:-1]])
e2=np.array([float(num) for num in data2[1:-1]])
e3=np.array([float(num) for num in data3[1:-1]])
e4=np.array([float(num) for num in data4[1:-1]])
l1.append(e1)
l1.append(e2)
l1.append(e3)
l1.append(e4)
l1=np.array(l1)
print(l1)


ll1=[]
ss1="0.823 0.2673 -0.596 0.236 0.21"
ss2="0.5723 0.7423 -0.5666 0.4936 0.821"
ss3="0.6623 -0.323 -0.9856 -0.736 0.621"
ss4="0.723 0.8123 -0.1756 0.8436 0.621"
ddata1=ss1.split(" ")
ddata2=ss2.split(" ")
ddata3=ss3.split(" ")
ddata4=ss4.split(" ")
ee1=np.array([float(num) for num in ddata1[1:-1]])
ee2=np.array([float(num) for num in ddata2[1:-1]])
ee3=np.array([float(num) for num in ddata3[1:-1]])
ee4=np.array([float(num) for num in ddata4[1:-1]])
ll1.append(ee1)
ll1.append(ee2)
ll1.append(ee3)
ll1.append(ee4)
ll1=np.array(ll1)
print(ll1)

print("-------------------") '''
#print((ll1[0]+l1[0])/2)

s1="0.213 0.23 -0.56 0.36 0.21"
data1=s1.split(" ")[1:-1]
ddata1=s1.split(" ")[:-1]

print(data1)
print(ddata1)