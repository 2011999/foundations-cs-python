class letsMeet:
  
    def __init__(self):
        self.users = {}  #store users and their friends
      
    def addUser(self, username):#add a new user 
        if username in self.users:
            return "User already exists "
        else:
            self.users[username]=[]
            return "User is added"
          
    def removeUser(self, username):#remove the user
        if username in self.users:
            self.users[username]
            return "User removed"
        else:
            return "User not found"

    def sendFriendRequest(self,user1,user2):#send request by entering 2 inputs(user1 and user 2)
        if user1 in self.users and user2 in self.users:#https://www.geeksforgeeks.org/add-and-remove-edge-in-adjacency-list-representation-of-a-graph/
            self.users[user1].append(user2)
            self.users[user2].append(user1)
            return "Friend Request Sent"

        else:
            return "Do not exist"

    def removeFriend(self, user11, user22):#remve the friend by also entering the 2 inputs
         if user11 in self.users and user22 in self.users:
           self.users[user11].remove(user22)
           self.users[user22].remove(user11)
           return "Friend Removed"
         else:
            return "Do not exist"
           
    def viewListFriends(self):#view all lists of friends
        friends_List=[]
        for username, friends in self.users.items():
          friends_List.append(f"{username}: {friends}")
        return friends_List

def main():
  print("______Assignment 4_____\n")
  print("__Welcome to Lets Meet__")
  sm_platform=letsMeet()#call the letsMeet class
  
  while True:#to reappear the options
    print("1. Add a user\n2. Remove a user\n3. Send a friend request\n4. Remove a friend\n5. View your list of friends\n6. View the list of all users\n7. Exit")

    option = input("Enter an option: ")

    if option == "1":
      username = input("Enter a username: ")
      print(sm_platform.addUser(username))
      
    elif option == "2":
      username = input("Enter a username: ")
      print(sm_platform.removeUser(username))
      
    elif option == "3":
      user1_username = input("Enter the username of the first user: ")
      user2_username = input("Enter the username of the second user: ")
      print(sm_platform.sendFriendRequest(user1_username, user2_username))
      
    elif option == "4":
      user1_username = input("Enter the username of the first user: ")
      user2_username = input("Enter the username of the second user: ")
      print(sm_platform.removeFriend(user1_username, user2_username))
      
    elif option == "5":
      print(sm_platform.viewListFriends())
      
main()
