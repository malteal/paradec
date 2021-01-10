import concurrent.futures
import time
import numpy as np
from paradec import parallel
from itertools import product

@parallel
def func(a,b=0.5):
    print(f'Sleep for {a*b}')
    time.sleep(a*b)
    return a**b

if __name__ == '__main__':
    a=np.linspace(0,4, 5)
    b=np.linspace(0, 1, 2)
    args = product(a,b)
    res=[]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(func, args)
    for i in results:
        res.append(i)