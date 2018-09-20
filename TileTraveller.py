#Tile Traveller board game first half

#Skilgreini x og y. x stendur fyrir fyrri tölu og y fyrir seinni tölu

while True:

    direction = (input("input a direction: "))

    x = 1
    y = 1

    


#North
    if direction == "N".lower() and direction < 3:
        y+=1
        print(x,y)
        print("You can travel: (N)orth or (E)ast or (S)outh.")
#South
    if direction == "S".lower() and direction > 1:
        print(x,y)
        y-=1
        print("You can travel: (N)orth or (E)ast or (S)outh.")

#east
    if direction == "E".lower() and direction < 3:
        x+=1
        print("You can travel: (N)orth or (E)ast or (S)outh.") 

#west
    if direction == "W".lower() and direction > 1:
        x-=1
        print("You can travel: (N)orth or (E)ast or (S)outh.")








