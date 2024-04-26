# TODO: Complete the get_ruler function
def get_ruler(kingdom):
    ruler = ''
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    last_letter = kingdom[len(kingdom) - 1]
    if last_letter in vowels:
        ruler = "Alice"
    elif last_letter not in vowels and last_letter != "y":
        ruler = "Bob"
    else:
        ruler = "Nobody"
    return ruler


def main():
    # Get the number of test cases
    T = int(input())
    for t in range(T):
        # Get the kingdom
        kingdom = input()
        print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))


if __name__ == '__main__':
    main()


