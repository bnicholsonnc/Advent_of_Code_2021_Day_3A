#
# Benjamin Nicholson
# Advent of Code 2021
# Day 3 Part 1
#

def read_file(name):
    li = []
    file = open(name, 'r')
    for line in file:
        entry = line.rstrip()
        li.append(entry)
    file.close()
    return li


def main():
    gr = ''
    er = ''
    numbers = read_file('practice.txt')

    for pos in range(len(numbers)):
        try:
            one = 0
            zero = 0
            for line in numbers:
                if line[pos] == '1':
                    one += 1
                else:
                    zero += 1
            if one > zero:
                gr += '1'
                er += '0'
            else:
                gr += '0'
                er += '1'
        except IndexError:
            break
    print(f'Gamma Rate: {int(gr, 2)}')
    print(f'Epsilon Rate: {int(er, 2)}')
    print(f'Power consumption: {int(gr, 2) * int(er, 2)}')




main()
