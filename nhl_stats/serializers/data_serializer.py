import json


class DataSerializer:

    def __init__(self):
        pass

    def serialize(self, json_data) -> dict:
        serialized_data = json.loads(json_data.text)

        return serialized_data

