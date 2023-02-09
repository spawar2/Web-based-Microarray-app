def has_a_histag(s):
    for i in range(0,len(s)-3):
        if s[i:i+4] == 'HHHH':
            return True
        else:
            return False

print(has_a_histag('dasdasdasdasHHHH'))

def has_s_a_sequence_of_three_as_in_it(s):
    for i in range(0,len(s)-3 ):
        if s[i:i+4] == 'AAAA':
            return True
        else:
            return False

print(has_s_a_sequence_of_three_as_in_it('dasdasdasdasAAAA')) 
print(has_s_a_sequence_of_three_as_in_it('dAAAasAdasdAAAasdasAA')) 
print(has_s_a_sequence_of_three_as_in_it('dasdAAAAAAAasdasdas')) 


s="TTCCGACTGACTTACGHHHHH"
import re
m = re.search('A{4,}',s)
if m > 4: print "H's is more than 4 times"
