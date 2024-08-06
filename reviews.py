data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for (line) in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為',sum_len / len(data))
new = []
for d in data:
	if len(d) < 100:
	    new.append(d)
print('這裡面總共有',len(new) ,'筆留言，長度小於100。')
print(new[0])  
print(new[1])  

