def encodetobase7(value):
    output = []
    codes = ['o', 'a', 't', 'l', 's', 'i', 'n']
    while value > 0:
        output.append(codes[value % 7])
        value = value // 7
    output.reverse()
    print((''.join(output)))


encodetobase7(7792875)  # outputs atlassian
