# itertools.permutations() generates permutations 
# for an iterable. Time to brute-force those passwords ;-)

import itertools

for p in itertools.permutations('ABCD'):
     print(p)

'''
Expected output:
('A', 'B', 'C', 'D')
('A', 'B', 'D', 'C')
('A', 'C', 'B', 'D')
('A', 'C', 'D', 'B')
('A', 'D', 'B', 'C')
('A', 'D', 'C', 'B')
('B', 'A', 'C', 'D')
('B', 'A', 'D', 'C')
('B', 'C', 'A', 'D')
('B', 'C', 'D', 'A')
('B', 'D', 'A', 'C')
('B', 'D', 'C', 'A')
('C', 'A', 'B', 'D')
('C', 'A', 'D', 'B')
('C', 'B', 'A', 'D')
('C', 'B', 'D', 'A')
('C', 'D', 'A', 'B')
('C', 'D', 'B', 'A')
('D', 'A', 'B', 'C')
('D', 'A', 'C', 'B')
('D', 'B', 'A', 'C')
('D', 'B', 'C', 'A')
('D', 'C', 'A', 'B')
('D', 'C', 'B', 'A')
'''
