import time
from pprint import pprint

from reader.bibles import BibleReader

if __name__ == '__main__':
    reader = BibleReader()

    prev = time.time()
    pprint(reader.get("john", 3, 16))
    print(time.time() - prev)

    print("\n\n------------------\n\n")

    prev = time.time()
    pprint(reader.get("john", 3, 16))
    print(time.time() - prev)
