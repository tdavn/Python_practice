'''
This code aims to remove space and digits
from the text, and export a fasta sequence
'''
import re

# Input sequence
origin_seq = input('Paste the sequence: ')
remove_char = [' ', '\t', '\n']
for chr in remove_char:
    origin_seq = origin_seq.replace(chr, '').upper() # remove space. Tabs need checking
final_seq = re.sub('\d', '', origin_seq) # remove digits
print(final_seq)