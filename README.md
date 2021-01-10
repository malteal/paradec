# Paradec
Paradec is a python decorator making it easy to parallelize a function with multiple input with concurrent.futures.
## Installing

Recent release:
```shell
pip install paradec 1.0.0
```

To install the git codebase to add modifications:
```bash
git clone https://github.com/malteal/paradec.git
```
## Usage

```python
import concurrent.futures
import time
import numpy as np
from paradec import parallel
from itertools import product

@parallel
def func(a,b):
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
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
