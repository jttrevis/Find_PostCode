import re

adress = input("Enter your full Adress: ")



std = re.compile("[A-Z]{2}[0-9][ ]?[0-9][A-Z]{2}")
srch = std.search(adress)

if srch:
    post_code = srch.group()
    print(post_code)