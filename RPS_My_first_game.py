from random import randint
print("Rock Paper and Scissors")
print("Lets play the game")

ch = 5
for i in range(5):

    player = input("choose one from Rock(r),paper(p),Scissors(s)\n")
    if player=="r" or player=="p" or player=="s":
        break
    else:

        ch=ch-1
        print("whats that?? you got",ch,"chances more")
        if(ch==0):
            print("End of the game...")
            break
        continue

print(player,"vs",end=" ")



choosen=randint(1,3)

if choosen == 1:
    computer='r'
elif choosen == 2:
    computer='p'
else:
    computer='s'

print(computer)

if(player == computer):
    print("Draw!!")
elif((player=="r" and computer=="s") or (player=="p" and computer=="r") or (player=="s" and computer=="p") ):
    print("You Won!!")
elif((player=="s" and computer=="r") or (player=="r" and computer=="p") or (player=="p" and computer=="s") ):
    print("Computer  Won :{0")