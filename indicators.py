i = input("String to convert: ")

d = { '0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine' }

for c in i:
    if c.isnumeric():
        output = ":" + d[c] + ": "
    elif c.isalpha():
        output = ":regional_indicator_" + c.lower() + ": "
    else:
        output = c
    print(output, end="")