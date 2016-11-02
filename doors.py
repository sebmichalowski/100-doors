doors = [False]*100


def flip_the_doors():
    '''flips the doors 100 times function'''
    for i in range(1, 101):
        for item in range(i-1, len(doors), i):
            doors[item] = not doors[item]


def print_open_doors():
    '''Print function'''
    print('The following doors are open: ', end='')
    for item in range(len(doors)):
        if doors[item]:
            print('{}'.format(item+1), end=' ')


def main():
    flip_the_doors()
    print_open_doors()


if __name__ == "__main__":
    main()
