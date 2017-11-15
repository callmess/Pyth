import random

secret = random.randint(1,10)
temp = input("猜下我心里想的是哪个数字:")
guess = int(temp)

while guess != secret:
      temp= input("错了, 重新来吧:")
      guess = int(temp)
      if guess == secret:
	  print("你好厉害")
