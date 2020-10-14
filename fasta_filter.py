'''
This code aims to remove space and digits
from the text, and export a fasta sequence
'''
import re
''' 
This code fragment is the first trial!

# Input sequence
origin_seq = input('Paste the sequence: ')
remove_char = [' ', '\t', '\n']
for chr in remove_char:
    origin_seq = origin_seq.replace(chr, '') # remove space
final_seq = re.sub('\d', '', origin_seq).upper() # remove digits
print(final_seq)
'''

# A new code.
sample_filter = re.compile(r'\d|\s')
message = input('Enter a text: ')
output_mes = sample_filter.sub('', message).upper()
print(output_mes)