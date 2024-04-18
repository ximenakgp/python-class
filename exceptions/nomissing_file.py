try:
    f = open('data/7-file_num.txt')
    my_number = int(f.read())
    print(my_number + 5)
except IOError:
    print("sorry, couldn't find the file")
