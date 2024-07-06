import json
from test import Voight_Kampff_Test

if __name__ == "__main__":
    with open("database.json") as f:
        data = json.load(f)
    test = Voight_Kampff_Test(data)
    test.perform_test()
