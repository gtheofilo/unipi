import os
print "+---------------------------------------------------+"
print "|Introduction to Computer Science - Exercise One (3)|"
print "+---------------------------------------------------+\n"
print "Type the elements of the list one by one. If you want"
print "to stop, type STOP/stop.\n"

importedList = []
counter = 1

while True:
  element = raw_input("Element No. {}: ".format(counter))
  if (element.upper() == "STOP"):
      os.system('cls' if os.name == 'nt' else 'clear')
      break
  else:
      if (element.isdigit()):
          importedList.append(int(element))
      else:
          importedList.append(element)
          counter = counter + 1

print "Given list:", importedList
zeroes = importedList.count(0)
for i in range(0, zeroes):
    importedList.remove(0)
    importedList.append(0)
print "New list:", importedList,counter
a = input()
