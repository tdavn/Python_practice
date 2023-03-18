strings = input("Enter:")
def sort_words(string):
    original_string = string.split()
    sorted_string= string.lower()
    sorted_string = sorted_string.split()
    sorted_string2 = string.lower()
    sorted_string2 = sorted_string2.split()
    conversion = zip(sorted_string, original_string)
    sorted_string2.sort()
    sorted_string2 = tuple(sorted_string2)
    dict_string = dict(conversion)
    final_list = []
    for i in sorted_string2:
        final_list.append(dict_string[i])   
    print(dict_string)
    print(final_list)
sort_words(strings)