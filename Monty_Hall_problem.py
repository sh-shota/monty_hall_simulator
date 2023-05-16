#!/usr/bin/python3
import random
import tbdump

k = 100000
fs_count = 0
re_count = 0
SIZE = 100 + 1

for l in range(k):    
    a = {i:'' for i in range(1, SIZE)}

    # make hit
    hit = random.randrange(1, SIZE)
    a[hit] += 'hit '

    # first choice
    fs_choice = random.randrange(1, SIZE)
    a[fs_choice] += 'fs_choice '
    
    # open false door
    end_size = 1
    if hit == fs_choice:
        end_size = 2
    left = [i for i,j in a.items() if j == '']
    while len(left) >= end_size:
        open_choice = random.randrange(0, len(left))
        a[left.pop(open_choice)] += 'open'

    # rechoice door
    re_choice = [i for i,j in a.items() if 'fs_choice' not in j and 'open' not in j]
    a[re_choice[0]] += 're_choice '


    # count accurency
    if 'hit' in a[fs_choice]:
        fs_count += 1

    if 'hit' in a[re_choice[0]]:
        re_count += 1

print(f'choice : {fs_count/k*100}%, re_choice : {re_count/k*100}%')