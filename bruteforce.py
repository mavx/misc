from __future__ import print_function
import time
import itertools

TARGET = 'password'
ALPHABET = [x for x in 'abcdefghijklmnopqrstuvwxyz']

def main():
    base = ['']
    n = 0
    for item in base:
        for l in ALPHABET:
            n += 1
            new = item + l
            # print(n, new)
            if new == TARGET:
                print('Found it!', n, new)
                return new
            base.append(new) # Append at the end of iterable list

def second():
    for length in range(10):
        for n, letters in enumerate(itertools.permutations(ALPHABET, length)):
            new = ''.join(letters)
            # print(new)
            if new == TARGET:
                print('Found it!', n, new)
                return new

if __name__ == '__main__':
    # start = time.time()
    # r = main()
    # print('Main Runtime: {:.2f}s'.format(time.time() - start))

    start = time.time()
    r = second()
    print('2nd Runtime: {:.2f}s'.format(time.time() - start))
