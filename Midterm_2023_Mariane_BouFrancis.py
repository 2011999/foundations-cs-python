import random
from datetime import datetime

#-----------------------------------------------------------------------------------
def readFile(filename):#Read the Tickets data from the file and returns a dictionary
  #https://www.pythontutorial.net/python-basics/python-create-text-file/
  #https://stackoverflow.com/questions/71837032/python3-file-open-write-exception-handling
  
  tickets = {}
  try:
    with open(filename, "r") as f:
      for line in f:
        parts = line.split(",")
        print(parts)
        ticket_id, event_id = parts[:2]
        username = parts[2]
        timestamp = parts[3]
        priority = parts[4]
        tickets[ticket_id] = {
          "event Id": event_id,
          "username": username,
          "time stamp": timestamp,
          "Priority": priority,
        }

  except FileNotFoundError:
    print("File not found.")
  return tickets


f = open("tickets.txt", "w+")
f.write(f"tick101, ev003, fred,20230801, 5\n"
        f"tick102, ev002, gio,20230802, 2\n"
        f"tick103, ev003, mario,20230724, 0\n"
        f"tick104, ev005, clara,20230721, 3\n"
        f"tick105, ev006, edy,20230801, 2\n"
        f"tick106, ev003, ella,20230807, 4\n"
        f"tick107, ev008, teddy,20230730, 1\n")
f.close()

tickets = readFile("tickets.txt")


#----------------------------------------------------------------------------------
def displayMenuUser():  #create a menu to the user
  print("OPTIONS are \n" + "1-Book a ticket \n" + "2- Exit \n")


def displayMenuAdmin():  #create a menu to the admin
  print("OPTIONS are \n" + "1-Display Statistics \n" + "2-Book a Ticket \n" +
        "3- Display All tickets \n" + "4-Change Ticket’s Priority \n" +
        "5-Disable Ticket\n" + "6- Run Events\n" + "7-Exit\n")


#-----------------------------------------------------------------------------------
#OPTION1#######
#https://datagy.io/python-get-dictionary-key-with-max-value/#:~:text=The%20simplest%20way%20to%20get,maximum%20value%20of%20any%20iterable.
def displayStatistics(
    tickets):  #display the highest number of tickets for an event
  event_ticket_counts = {}  # create a empty dic to store the tickets
  for ticket_id in tickets:
    event_id = tickets[ticket_id]['event Id']
    event_ticket_counts[event_id] = event_ticket_counts.get(event_id, 0) + 1
    highest_event_id = max(
      event_ticket_counts, key=event_ticket_counts.get
    )  # max function to find the highest number of tickets
    highest_count = event_ticket_counts[highest_event_id]
  return ("the highest number of ticket is ", highest_count, "for event   Id",
          highest_event_id)


#----------------------------------------------------------------------------------
#OPTION2#######
#https://stackoverflow.com/questions/31436691/how-would-i-concatenate-a-random-randint
def bookTicketAdmin(tickets):  #book ticket for an event
  username = input("enter the username: ")
  event_id = input("enter the event id: ")
  priority = input("enter the priority: ")
  date_event = input("enter the date of the event(%Y%m%d) : ")
  id = random.randint(0, 200)  #to create a random ticket number
  ticket_id = "tick" + str(id)  #to give a random tick number

  updated_tickets = tickets.update({
    ticket_id: {
      "event_id": event_id,
      "username": username,
      "time stamp": date_event,
      "priority": priority
    }  #this update the dictionary without saving to the txt file
  })
  return updated_tickets


#---------------------------------------------------------------------------------
#https://www.tutorialspoint.com/How-to-get-formatted-date-and-time-in-Python#:~:text=To%20convert%20a%20datetime%20object,hh%3Amm%3Ass%20format.
#OPTION3#######
#https://www.programiz.com/dsa/merge-sort
def sorTicket(ticket):  #we use merge sort for sorting large files
  if len(ticket) > 1:

    r = len(ticket) // 2
    L = ticket[:r]
    M = ticket[r:]
    sorTicket(L)
    sorTicket(M)
    i = j = k = 0
    while i < len(L) and j < len(M):
      if L[i]['event Id'] < M[j]['event Id']:  #sorted by event id
        ticket[k] = L[i]
        i += 1
      else:
        ticket[k] = M[j]
        j += 1
      k += 1

    while i < len(L):
      ticket[k] = L[i]
      i += 1
      k += 1

    while j < len(M):
      ticket[k] = M[j]
      j += 1
      k += 1
    return ticket


def displayTicket(
    tickets):  #display the tickets after sorting them by event id
  today = datetime.today()  #to display the today time
  today_date = today.strftime("%Y%m%d")
  ticket = {}  #empty to after the loop to store the tickets sorted by event id
  for ticket_id in tickets:
    td = tickets[ticket_id]['time stamp']
    if td >= today_date:  #for date of event equal or above today's date
      ticket[ticket_id] = tickets[ticket_id]
  sorted_updated_tickets = list(ticket.values())
  sorted_tick = sorTicket(sorted_updated_tickets)
  print(sorted_tick)
  return sorted_tick


#---------------------------------------------------------------------------------
#OPTION4#######
def changeTicketPriority(
  tickets
):  #enter the ticket that you want to change the priority and update the system with new changes
  ticket_id = input("enter the ticket ID: ")
  if ticket_id in tickets:
    priority = int(input("change the priority : "))
    tickets[ticket_id][
      'Priority'] = priority  #this method is to change the ticket priority in the dic without saving into the txt file
    return ("the tickets ", tickets)

  else:
    return "ticket is not found"


#----------------------------------------------------------------------------------
#OPTION6#######
def sortTicketPriority(ticket):  #we use merge sort for sorting large files
  if len(ticket) > 1:

    r = len(ticket) // 2
    L = ticket[:r]
    M = ticket[r:]

    sortTicketPriority(L)
    sortTicketPriority(M)

    i = j = k = 0

    while i < len(L) and j < len(M):
      if int(L[i]['Priority']) < int(M[j]['Priority']):  #sorted by priority
        ticket[k] = L[i]
        i += 1
      else:
        ticket[k] = M[j]
        j += 1
      k += 1

    while i < len(L):
      ticket[k] = L[i]
      i += 1
      k += 1

    while j < len(M):
      ticket[k] = M[j]
      j += 1
      k += 1
    return ticket


def runEvent(tickets):  #in option 6 we should remove the event of today event
  today = datetime.today()
  today_d = today.strftime("%Y%m%d")
  same_date = {}
  for ticket_id in tickets:
    ticket_today = tickets[ticket_id]['time stamp']
    if str(ticket_today) == today_d:
      same_date[ticket_id] = tickets[ticket_id]
  same_date_sorted = sortTicketPriority(list(same_date.values()))
  print(same_date_sorted)
  for ticket_id in same_date:
    del tickets[ticket_id]

  return tickets


#----------------------------------------------------------------------------------
#OPTION5#######
def disableTicket(tickets):  #delete the ticket after the user enters the Id
  ticket_id = input("enter the ticket id : ")
  if ticket_id in tickets:
    del tickets[
      ticket_id]  # if the ticket is found the del function delete it from the dic
    return tickets
  else:
    print("ticket is not found")
    return tickets


#----------------------------------------------------------------------------------
#https://stackoverflow.com/questions/31436691/how-would-i-concatenate-a-random-randint
#https://stackoverflow.com/questions/31753330/save-the-user-input-to-existing-text-file-everytime-running-the-script-python
#OPTION1_USER#######
def bookTicket(
  tickets
):  #for user option, the ticket that will be booked will be save in the txt file
  username = input("enter the username: ")
  event_id = input("enter the event id: ")
  priority = input("enter the priority: ")
  date_event = input("enter the date of the event(%Y%m%d) : ")
  id = random.randint(0, 1000)
  ticket_id = "tick" + str(id)

  new_ticket = {
    ticket_id: {
      "event Id": event_id,
      "username": username,
      "time stamp": date_event,
      "priority": priority
    }
  }

  with open(
      "tickets.txt",
      "a+") as textfile:  #this method to save the data to the new txt file
    textfile.write(
      f"{ticket_id}, {new_ticket[ticket_id]['event Id']} ,{new_ticket[ticket_id]['username']}, {new_ticket[ticket_id]['time stamp']}, {new_ticket[ticket_id]['priority']} \n"
    )

  return tickets


#__________________________________________________________________________________
#https://stackoverflow.com/questions/58986088/print-menu-after-selection
def main():
  for i in range(5):  #use for loop to sepcify the number of attempts
    print("\n WELCOME TO TICKETING BOX OFFICE! \n")
    username = input("enter your username: ")
    password = input("enter your password: ")
    if username == "admin" and password == "admin123123":

      while True:  #using while true to be able to display the menu after each selection
        displayMenuAdmin()
        option = int(input("Enter your option:  "))
        if option == 1:
          displayStatistics(tickets)
          print(displayStatistics(tickets))
        elif option == 2:
          bookTicketAdmin(tickets)
          print(tickets)
        elif option == 3:
          displayTicket(tickets)
        elif option == 4:
          print("priority : ",changeTicketPriority(tickets))
        elif option == 5:
          print("tickets:", disableTicket(tickets))
        elif option == 6:
          runEvent(tickets)
          print("the tickets are: ", runEvent(tickets))
        elif option == 7:
          print("Thank you")
          exit()
        else:
          print('Invalid option. Please enter a number between 1 and 7.')
    elif username != "admin" and password == "":

      while True:
        displayMenuUser()
        option = int(input("Enter your option:  "))
        if option == 1:
          bookTicket(tickets)
        elif option == 2:
          print("Thank you for using ticketing box office")
          exit()

    elif username != "admin " and password != "":
      print("incorrect password and/or username")
  exit()


#----------------------------------------------------------------------------------
main()
