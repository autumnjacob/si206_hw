import re

sum = 0
open_file = open("si206_actualdata_hw5", "r")
for line in open_file:
    a = re.findall('[0-9]+', line)
    for item in a:
        sum += int(item)
print (sum)
  