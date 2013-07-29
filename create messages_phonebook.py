import os
import re
import sys

vcf_file = sys.argv[1]

def parse_file(infile):
    card = ''
    for line in infile:
        if line.startswith('BEGIN:VCARD') and card.endswith('END:VCARD\r\n'):
            yield card
            card = ''
        card += line
    yield card

iphone_count = 0
messages_phonebook = []
with open(vcf_file,'rb') as infile:
    for i, card in enumerate(parse_file(infile)):
        num_match = re.search(r'(?<=TEL;type=IPHONE)(.*?:)(.*)', card)
        if num_match:
            iphone_count += 1
            name = re.search(r'(?<=FN:)(.*)\r\n', card).group(1)
            number = re.sub(r'\D','', num_match.group(2))
            messages_phonebook.append((name, number))
            with open(os.getenv("HOME") + '/Desktop/messages_phonebook.txt','ab') as w:
                w.write('\n{}, {}'.format(name, number))

with open(os.getenv("HOME") + '/Desktop/messages_phonebook.txt','rb') as r:
    names_sorted = (name.strip() for name in sorted(r.read().splitlines() ) if name.strip() != '' )
with open(os.getenv("HOME") + '/Desktop/messages_phonebook.txt','wb') as w:
    w.writelines('\n'.join(names_sorted))
