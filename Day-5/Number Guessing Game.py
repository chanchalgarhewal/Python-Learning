num=int(input("Enter a number:"))
secret_number=7
if num==secret_number:
    print("Correct Guess!")
elif num< secret_number:
     print("Too Low!")
else:
     print("Too high!")
