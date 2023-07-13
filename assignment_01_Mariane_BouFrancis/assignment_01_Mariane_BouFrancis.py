def factorialNumber(n):
  fact_numb = 1
  for i in range(2, n + 1):
    fact_numb = i * fact_numb
  return fact_numb


def divisors(n1):
  div_list = [
  ]  #we create a empty list so we can add the elements after the for loop
  for i in range(1, n1 + 1):  #this for loop
    if n1 % i == 0:
      div_list.append(i)
  return div_list


def revString(strg):
  for i in range(len(strg)):
    strg_revs = strg[::
                     -1]  #this iteration will go backwords and will reverse the string

  return strg_revs


def updatedList(user_list):
  updated_list = [
  ]  #we create an empty list to store after the loop the even numbers
  for i in user_list:
    if i % 2 == 0:
      updated_list.append(i)

  return updated_list


def strongPassword(password):
  if len(password) < 8:  #first we check if the lenght of the password is 8
    return "weak password"
  else:  #pass_upper&lower&digit is initially set to False. we use them to know if the upper& lower case& digit is found in the string.
    pass_upper = False
    pass_lower = False
    pass_digit = False
    pass_special = "@ % $ &"
    for i in range(len(password)):
      if password[i].isupper(
      ):  #isupper,islower&isdigit are used to verify if uppercase, lowercase or digit are found in the string
        pass_upper = True
      elif password[i].islower():
        pass_lower = True
      elif password[i].isdigit():
        pass_digit = True
      elif password[i] == pass_special:
        pass_special = True
  return "strong password"


def main():
  n = eval(input("Choose an integer: "))
  y = factorialNumber(n)
  print("factorial number for ", n, "is : ", y)
  n1 = eval(input("Choose an integer: "))
  z = divisors(n1)
  print("divisors of  ", n1, "is : ", z)
  strg = input("enter the string : ")
  strgw = revString(strg)
  print("the reverse of the string is :", strgw)
  user_list = eval(input("enter a list: "))
  new_list = updatedList(user_list)
  print("the new list is : ", new_list)
  password = input("enter a password: ")
  password_result = strongPassword(password)
  print("the password", password, "is", password_result)


main()
