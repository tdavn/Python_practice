'''
This code aims to remove space and digits
from the text, and export a fasta sequence
'''
import re

# Input sequence
origin_seq = input('Paste the sequence: ')
intermediate_seq = origin_seq.replace(' ', '').upper() # remove space. Tabs need checking
final_seq = re.sub('\d', '', intermediate_seq) # remove digits
print(final_seq)