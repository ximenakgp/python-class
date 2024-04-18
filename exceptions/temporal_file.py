import os
t = open('data/temp.txt', 'w')
t.write('8')
t.close()
try:
    f = open('data/temp.txt')
    my_number = int(f.read())
    print(my_number + 5)
    os.remove('data/temp.txt') # delete the temp file
except IOError as ex:
    print("sorry, couldn't find the file: " + ex.strerror)
    os.remove('data/temp.txt') # delete the temp file
except ValueError as ex:
    print("sorry, couldn't parse the number: " +  ex.args[0])
    os.remove('data/temp.txt') # delete the temp file
