import main

class bcolors:
  BLUE = '\033[94m'
  RED = '\033[91m'
  GREEN = '\033[92m'


x = 1


if x == 1:
  main.hello()
else:
  print(bcolors.RED + "goodbye world ):")