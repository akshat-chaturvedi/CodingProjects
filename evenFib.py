import numpy
import time

def evenFib(n):
    a = 1
    b = 2

    evenList = [2]

    d = 0

    while d < n:
        c = a+b
        d = c+b
        if d%2==0:
            evenList.append(d)

        a = b
        b = c

    return sum(evenList)

if __name__ == '__main__':
    startTime = time.time()
    print(evenFib(4e6))
    endTime = time.time()
    print(f"Time taken: {endTime-startTime:.5e} seconds")