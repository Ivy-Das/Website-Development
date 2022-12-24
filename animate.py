input = input("Enter: ")
input = input.lower()
finder = input("What do you want to find: ")
finder = finder.lower()
sec = input.split(" ")
breaker = [a for a in finder if a in sec]
if finder in sec:
  print("yes")
else:
  print("no")