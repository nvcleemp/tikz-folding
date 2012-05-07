for i in range(26):
    print '\\tikzoption{face %d}{\\def\\tikz@lib@fold@face@%s{#1}}' % (i+1, chr(ord('A')+i)) 

for j in range(3):
    for i in range(26):
        if 27+j*26+i<=92:
            print '\\tikzoption{face %d}{\\def\\tikz@lib@fold@face@%s%s{#1}}' % (27+j*26+i, chr(ord('A')+j), chr(ord('A')+i)) 

for i in range(26):
    print '\\let\\tikz@lib@fold@face@%s=\\pgfutil@empty' % (chr(ord('A')+i)) 

for j in range(3):
    for i in range(26):
        if 27+j*26+i<=92:
            print '\\let\\tikz@lib@fold@face@%s%s=\\pgfutil@empty' % (chr(ord('A')+j), chr(ord('A')+i)) 

for i in range(92):
    print '	face %d={\\node{%d};},' % (i+1,i+1)
