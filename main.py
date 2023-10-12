import random

random_num = random.randint(1,100)
# print(random_num)
flag = 0
attemped = 0

temp = []
n = len(temp) - 1


def initial_res(num):
  if num <= 0 and num > 100:
    return "OUT OF BOUND"
  elif abs(num - random_num) <= 10:
    return "WARM"
  else:
    return "COLD"


print("Let's the Guess begins...")

while True:

  user_num = int(input("Enter the Guess number: "))
  attemped += 1

  if user_num == random_num:
    print(f"Bingo!, You have guessed number on your {attemped} Attemp.")
    break


  else:

    if flag == 0:
      res = initial_res(user_num)
      print(res)
      flag = 1
      temp.append(user_num)
    else:

      temp.append(user_num)
      # print(f"user num = {user_num}")
      # print(f"temp = {temp[n]}")
      # print(temp)

      if abs(random_num - user_num ) < abs(random_num - temp[n-1]):

        print("Warmer")

      else:
        print("Colder")



print(temp)



