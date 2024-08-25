data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for (line) in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data),'筆留言')
print(data[0])

# 文字計數
wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('請問你要查什麼字: ')
	if word == 'q':
		break
	elif word in wc:
		print(wc[word])
	elif word not in wc:
		print('找不到這個字喔!!!')
print('感謝使用本查詢功能!!!')
