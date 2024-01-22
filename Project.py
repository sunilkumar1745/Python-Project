print("Welcome to python quiz game")
score=0
print("What is the highest mountain in the world?")
print("1.Mount Kilimanjaro\n2.Mount Everest\n3.Mount McKinley\n4.Mount Fuji")
ans=int(input("Your choice-enter option number : "))
if(ans==2):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("What is the chemical symbol for gold?")
print("1.Au\n2.Ag\n3.Fe\n4.Cu")
ans=int(input("Your choice-enter option number : "))
if(ans==1):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("Who wrote the play 'Hamlet'?")
print("1.William Shakespeare\n2.Jane Austen\n3.Charles Dickens\n4.Mark Twain")
ans=int(input("Your choice-enter option number : "))
if(ans==1):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("Your score is : ",score," out of 3")