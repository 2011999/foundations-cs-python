#####################
def countDigits(n2):
  if (n2 // 10 == 0):  # If the number is less than 10
    return 1  # Return 1 since it has only one digit
  else:
    return 1 + countDigits(
      n2 //
      10)  # Recursive call to count the digits by dividing the number by 10


def findMax(z):
  if len(z) == 1:  #list with only one element
    return z[0]  #return the only element in this list
  else:
    if z[0] > findMax(
        z[1:]
    ):  # If the first element is bigger than the maximum of the remaining list
      return z[0]  #else  the first element is the maximum

    else:
      return findMax(z[1:])  # find the maximum in the remaining list


def countTags(html, tag):
  #to find the opening and closing tags we should use the find
  opening_tag = html.find("<" + tag + ">")

  closing_tag = html.find("</" + tag + ">")

  if opening_tag == -1 and closing_tag == -1:  #if we didnt find the opening return zero
    return 0
  else:  #if we found the opening tage we add one and we continue until the code is finished
    return 1 + countTags(html[closing_tag + len("</" + tag + ">"):], tag)


####################


def displayMenu():
  print("OPTIONS are \n" + "1-Count digits \n" + "2-Find Max\n" +
        "3-Count Tags \n" + "4-exit")


def main():
  print("------ASSIGNMENT 2------\n")
  displayMenu()
  option = int(input("Enter your option:  "))

  if option == 1:
    n = int(input("Enter the number that you want to count  :"))
    cd = countDigits(n)
    print("Count digits ", n, "is : ", cd)

  elif option == 2:
    m = input("Enter a list of integers separeted by space: "
              )  #we separeted by space for the split function
    lst = m.split(
    )  # I use this split function to return each integer into a list
    print(lst)
    w = findMax(lst)
    print("the maximun of this list is ", w)
  elif option == 3:
    html_lines = [
    ]  #### I searched on google I found this method to how to make the user write a proper html code
    print("Enter the HTML code (type 'END' on a new line to finish): ")
    while True:
      line = input()
      if line.strip() == 'END':
        break
      html_lines.append(line)
    html = '\n'.join(html_lines)  ####

    tag = input("Enter a tag to count occurrences: ")
    occurrences = countTags(html, tag)
    print("the occurrences of tag ", tag, " : ", occurrences)

  elif option == 4:  #option 4 will make the user exit the program
    print("Thank you")
    exit()
  else:
    print('Invalid option. Please enter a number between 1 and 4.')

  print(" \n------------------- ")


main()
