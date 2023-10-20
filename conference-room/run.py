from models import DataStore, User, Building, Floor, Meeting, read_data

new_line    = "\n"
tab         = "\t"
space       = " "
colon       = ":"

ds: DataStore = None

def get_item(arr, index, default):
    return arr[index] if index < len(arr) else default

if __name__ == "__main__":
    ds = read_data()

    print(f"{new_line}Conference Room Management System{new_line}")
    username = input("Enter username: ")
    
    if not ds.has_user(username):
        print("user does not exists")
        username = None
    
    while True and username:
        arg = input("> ")
        
        if arg in ["h", "help"]:
            with open("README.md") as file_help: print(file_help.read())
        elif arg in ["d", "dump"]:
            print(ds)
        elif arg in ["e", "exit"]:
            break
        
        elif arg == "add":
            command = input(f"{tab}> ").split(space)
            
            if command[0] == "building":
                if len(command) < 2:
                    print("invalid number of arguments")
                else:
                    building_name = command[1]
                    time_slot = get_item(command, 2, [10,20])
                    #add_building(building_name, time_slot)
    """
    if username not in user_data:
        print("user does not exists!!!")
        username = None

    while True and username:
        arg = input("> ")

        if arg == "h" or arg == "help":
            with open("help") as file_help:
                print(file_help.read())
        elif arg == "d" or arg == "dump":
            old_debug, debug = debug, True
            echo(building_data, pretty=True)
            echo(meeting_data, pretty=True)
            debug = old_debug
        elif arg == "e" or arg == "exit":
            break
        elif arg == "add":
            command = input(f"{tab}> ").split(space)
            if command[0] == "building":
                if len(command) < 2:
                    print("invalid numbers of arguments")
                else:
                   building_name = command[1]
                   time_slot = get_item(command, 2, [10,20])
                   add_building(building_name, time_slot)
            elif command[0] == "floor":
                if len(command) < 3:
                    print("invalid numbers of arguments")
                else:
                    building_name = command[1]
                    floor_name = command[2]
                    add_floor(building_name, floor_name)
    """