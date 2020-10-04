# This is a converter hex to string and vice versa

def strngtohx(strng):
    # From string to hex
    hxCnt = strng.encode().hex()
    print('Output hex: \n', hxCnt)


def hxtostrng(hx):
    # From a hex code to String
    txtCnt = bytes.fromhex(hx).decode('utf-8')
    print('Output: \n', txtCnt)


try:
    while True:
        opt = input('Convert to hex, type h. To string, type s. Otherwise, type q to quit. ')
        if opt == 'h' or opt == 's':
            break
        if opt == 'q':
            raise Exception('You want to quit!')
        else:
            print('Invalid format. Please try again!')

    inpt = input('Enter input: ')
    print('Input: \n' + inpt)
    if opt == 'h':
        strngtohx(inpt)

    if opt == 's':
        hxtostrng(inpt)

except Exception as byebye:
    print(byebye)
