str = input()


def palidrome(str1):
    final_str = ""

    for i in str1:
        if i != " ":
            final_str = final_str + i

# or final_str = str1.replace(' ', '')
# or final_str = ''.join(str1.split(' ')) (tách str1 từ dấu ' 'vào 1 list, nối lại các str trong list = dấu '')

    length = len(final_str)

    for i in range(0, length):
        if final_str[i] != final_str[length - i - 1]:
            return False

# or if final_str == final_str[:: -1] (:: là slicing, -1 cắt đọc từ hướng ngược lại)

    return True

print(palidrome(str))


