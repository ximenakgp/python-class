try:
    f = open('data/7-file_num.txt') # this line might raise an IOError
    my_number = int(f.read()) # this line might raise a ValueError
except IOError:
    print('cannot open file!')
except ValueError:
    print('not an integer!')
finally:
    f.close()
    print("the file was closed")
