#!/usr/bin/env python

import sys
import re

script, name, phonebook_file = sys.argv

match = re.search(r'^\d{7}$|^\d{10}$|^(\d{3}\-)?\d{3}-\d{4}$|(^.+?@.+?\..+?$)', name)

# The input was a phone number or email, go with it.
if match:
    print name
    exit(0)

else:
    name = name.lower()
    with open(phonebook_file, 'r') as f:
        contacts_list = [ tuple(
            line.lower().strip().split(', ') )
            for line in f if len(line) > 1]

    for contact, number in contacts_list:
        if name == contact:
            print number
            exit(0)
        else:
            pass

# Returns the original name if no match was found.
    print name
