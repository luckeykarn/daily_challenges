chat_rooms = {}

def add_user(room,user):
    if room not in chat_rooms:
        chat_rooms[room] = set() 
        chat_rooms[room].add(user)   
    print(f"{user} added to {room}.")

def remove_user(room,user):
    if room in chat_rooms and user in chat_rooms[room]:
        chat_rooms[room].remove(user) 
        print(f"{user} removed from {room}.")
    else:
        print(f"{user} not found in {room}.")

def list_users(room):
    if room in chat_rooms:
        print(f"Users in {room}:")
        for i, user in enumerate(chat_rooms[room], 1):
            print(f"{i}. {user}")
    else:
        print(f"No users in {room}.")

def common_users(room1, room2):
    if room1 in chat_rooms and room2 in chat_rooms:
        common = chat_rooms[room1].intersection(chat_rooms[room2])
        if common:
            print(f"Common users in {room1} and {room2}:")
            for user in common:
                print(user)
        else:
            print(f"No common users between {room1} and {room2}.")
    else:
        print("One or both rooms do not exist.")

while True:
    print("Commands: add, remove, list, common, exit")
    command = input("Enter command: ").lower()

    if command == "add":
        room = input("Enter room name: ")
        user = input("Enter username: ")
        add_user(room, user)

    elif command == "remove":
        room = input("Enter room name: ")
        user = input("Enter username to remove: ")
        remove_user(room, user)

    elif command == "list":
        room = input("Enter room name: ")
        list_users(room)

    elif command == "common":
        room1 = input("Enter first room: ")
        room2 = input("Enter second room: ")
        common_users(room1, room2)

    elif command == "exit":
        print("Exiting chat room tracker...")
        break

    else:
        print("Invalid command.")
