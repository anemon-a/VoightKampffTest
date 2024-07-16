import json
from vk_test.voight_kampff_test import VoightKampffTest

if __name__ == "__main__":
    """Entry point to the program"""
    test = VoightKampffTest("question.json")
    test.run_test()
