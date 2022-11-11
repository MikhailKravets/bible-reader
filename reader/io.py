import json

from dataclasses import asdict

from reader.models import Bible


class IO:

    def __init__(self, filepath: str):
        self.filepath = filepath

    def write(self, obj: Bible):
        with open(self.filepath, 'w') as f:
            json.dump(asdict(obj), f)

    def read(self) -> Bible:
        # TODO: read the Bible object from JSON-formatted file
        # TODO: either do it with the standard python utilies (preferred way)
        # TODO: or use https://pypi.org/project/dataclasses-json/ package
        #   for these exactly purposes
        pass
