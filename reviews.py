import time
import progressbar
data = []
count = 0
with open ('reviews.txt', 'r') as f:
	bar = progressbar.ProgressBar(max_value = 1000000)
	for (line) in f:
		data.append(line)
		count += 1
		bar.update(count)
print('檔案讀取完了,總共有', len(data),'筆留言')
print(data[0])

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
good = []
for d in data:
   if 'good' in d:
       good.append (d)
print('有', len(good),'筆留言中，有good的字眼')
print(good[0])

# 文字計數
start_time = time.time()
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
end_time = time.time()
print('花了', end_time - start_time, 'sec')
while True:
	word = input('請問你要查什麼字: ')
	if word == 'q':
		break
	elif word in wc:
		print(wc[word])
	elif word not in wc:
		print('找不到這個字喔!!!')
print('感謝使用本查詢功能!!!')
