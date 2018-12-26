# 產生一個隨機整數 1~100
# 讓使用者重複輸入去猜
# 猜對的話印出 "你猜對了"
# 猜錯的話,告訴使用者 比答案大/小
import random
r = random.randint(1, 100)
while True:
	a = int(input('請輸入答案:'))
	if a == r:
		print("你猜對了")
		break
	elif a > r:
		print("比答案大")
	else:
		print("比答案小")