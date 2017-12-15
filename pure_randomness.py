import numpy as np
import time

def random_array():
    return np.random.rand(1, 5)

def around(array):
    return [int(x * 10000) / 10000 for x in array]

def main():
    target = around((random_array() * 5)[0])
    start = time.time()
    n = 0

    print('Finding target: ', target)
    while 1:
        n += 1
        if n % 10000 == 0:
            print('{}th iteration: {:.2f}s elapsed.'.format(n, time.time() - start))
            print('Last array:', score)

        score = around(sum(random_array() for _ in range(5))[0])
        if target == score:
            print('Found it!', score)
            break
    
    print('Runtime: {:.2f}s'.format(time.time() - start))

if __name__ == '__main__':
    main()
