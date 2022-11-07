import time
from pprint import pprint

from reader.bibles.ron_swanson import RonSwansonReader
from reader.bibles.bible import BibleReader

if __name__ == '__main__':
    reader = BibleReader()

    prev = time.time()
    pprint(reader.get("john", 3, 16))
    print(time.time() - prev)

    print("\n\n------------------\n\n")

    prev = time.time()
    pprint(reader.get("john", 3, 16))
    print(time.time() - prev)

    print()
    print("Ron Swanson")
    print()
    swanson = RonSwansonReader()
    pprint(swanson.get("brit"))
