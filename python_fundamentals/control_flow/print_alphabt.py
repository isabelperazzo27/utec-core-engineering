#!/usr/bin/env python3
for i in range(97, 123):
    if chr(i) != 'e' and chr(i) != 'q':
        print("{:c}".format(i), end="\n" if i == 122 else "")
