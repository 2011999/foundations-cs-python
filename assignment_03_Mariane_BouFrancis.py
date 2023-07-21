#########################################
def sumTuple(tpl1, tpl2):
  if len(tpl1) == len(tpl2):
    tpl3 = []
    for i in range(len(tpl1)):
      tpl = tpl1[i] + tpl2[i]
      tpl3.append(tpl)
    return tuple(tpl3)
  else:
    return 0


def dictionary_to_json(dictionary):
  json_str = "{\n"
  for key, value in dictionary.items():
    json_str += f'  "{key}": '
    if isinstance(value, str):
      json_str += f'"{value}"'
    else:
      json_str += str(value)
    if key != list(dictionary.keys())[-1]:
      json_str += ','
    json_str += '\n'
  json_str += "}"
  return json_str


def displayMenu():
  print("OPTIONS are \n" + "1-Sum Tuples \n" + "2-Export JSON \n" +
        "3-Import JSON \n" + "4-exit")


def main():
  print("------ASSIGNMENT 3 ------\n")
  displayMenu()
  option = int(input("Enter your option:  "))

  if option == 1:
    tpl1 = eval(input("Enter a tuple:"))
    tpl2 = eval(input("Enter a tuple:"))
    w = sumTuple(tpl1, tpl2)
    print("the sum of the tuples is ", w)
  elif option == 2:
    dictionary = {"store": "Happy", "item": "apples", "price": 2}
    json_str = dictionary_to_json(dictionary)
    print(json_str)
    with open("my_dictionary.json", "w") as file:
      file.write(json_str)
  elif option == 4: 
    print("Thank you")
    exit()
  else:
    print('Invalid option. Please enter a number between 1 and 4.')

  print(" \n------------------- ")


main()
