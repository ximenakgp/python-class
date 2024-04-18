try:
    f = open('data/7-file_num.txt')
    try:
        my_number = int(f.read())
    except ValueError:
        print('not an integer!')
    finally:
        f.close()
        print("the file was closed")
except IOError:
    print('cannot open file')
