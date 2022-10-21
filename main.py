from pprint import pprint

from reader.bibles import BibleReader

if __name__ == '__main__':
    reader = BibleReader()
    pprint(reader.get("john", 3, 16))
