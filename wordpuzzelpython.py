import random
print("Word Puzzle Game")
score=0
l=["father","break","country","green","aeroplane"]
l.sort(reverse=False)
i=0
while i<=4:
    a=list(l[i])
    random.shuffle(a)
    print("Arrange the letters to form a valid word:")
    print("".join(a))
    str=input()
    if l[1]==str:
          print()
          print("Correct")
          score+=1
    else:
        print("Wrong")
        score-=1
    i+=1
print("Net Score is ",score)
