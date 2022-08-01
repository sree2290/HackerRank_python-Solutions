def mutate_string(string, position, character):
    l = string = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
