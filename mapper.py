
# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:

  line = line.strip()
  # split the line into words, output data type list
  words = line.split()

  # with the count of 1 to the STDOUT
  for word in words:
    print('%s\t%s' % (word, 1))
