import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234


123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat 
pat 
bat
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
sentence = 'Start a sentence and then bring it to an end'
# pattern =re.compile(r'[1-5]')
# pattern =re.compile(r'[^b]at')
# pattern =re.compile(r'Mr?s?(rs)?\.?\s[A-Z]\w*')
# pattern =re.compile(r'M(r|s|rs)?\.?\s[A-Z]\w*')
# pattern =re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z]+.com')
pattern =re.compile(r'(http|https)(://)(www)?(\.)?([a-zA-Z0-9_.+-]+)\.(com|gov)')




matchers=pattern.finditer(text_to_search)


# with open("C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\learn python\\Data_Science_in_Python\\learn regex(24-1-22)\\data.txt","r")as f:
#     filedata=f.read()
#     matchers=pattern.finditer(filedata)
#     for match in matchers:
#         print(match)

for match in matchers:
    print(match.groups())

# print(text_to_search[1:4])

