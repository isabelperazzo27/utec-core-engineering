#!/usr/bin/env python3
alphabet_str = ""
for i in range(97, 123):
    if chr(i) != 'e' and chr(i) != 'q':
        alphabet_str += chr(i)

print(alphabet_str)
