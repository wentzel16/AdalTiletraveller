#Tile Traveller board game first half

#Skilgreini x og y. x stendur fyrir fyrri tölu og y fyrir seinni tölu

x = 1
y = 1

while True:

    direction = (input("input a direction: "))
    
#North
    if direction == "N":
        if (x == 1 and y == 3) or (x == 2 and y == 3) or (x==3 and y==3) or (x==2 and y==2):
            print("Not a valid direction!")
        else:
            if y < 3:
                y += 1
                print(x,y)
                print("You can travel: (N)orth or (E)ast or (S)outh.")
        
#South
    if direction == "S":
        if (x == 1 and y == 1) or (x == 2 and y == 1) or (x == 3 and y == 1) or (x==2 and y == 3):
            print("Not a valid direction!")
        else:
            if y > 1:
                y-=1
                print(x,y)
                print("You can travel: (N)orth or (E)ast or (S)outh.")

#east
    if direction == "E":

        if (x == 2 and y == 2) or (x ==2 and y == 1) or (x == 1 and y ==1) or (x == 3 and y == 3) or (x == 3 and y == 3) or (x == 3 and y == 2) or (x == 3 and y ==1):

            print("Not a valid direction!")
            

        else:
            if x < 3: 
                x+=1
                print(x,y)
                print("You can travel: (N)orth or (E)ast or (S)outh.") 

#west
    if direction == "W":
        if (x == 1 and y == 1) or (x == 1 and y == 2) or (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2) or (x == 3 and y == 1):
            print("Not a valid direction!")
        else:
            if x > 1:
                x-=1
                print(x,y)
                print("You can travel: (N)orth or (E)ast or (S)outh.")


    
        








