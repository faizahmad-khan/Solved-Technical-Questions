# # # file = open ("/Users/faizahmadkhan/Desktop/filename.txt","r")
# # # content = file.readline(10)
# # # print (content)
# # # file.close() 

# # import math
# # n= int(input("Enter a number"))
# # num= math.pi
# # num2= n*n
# # print(num*num2)

# import random
# fruits =["apple","banana","cherry"]
# random.shuffle(fruits)
# print ("Suffledlist:",fruits)

import datetime
today = datetime.date.today()
days_ago = today - datetime.timedelta(days=200)
print ("Days ago:",days_ago)
year1=today.month
print (year1)