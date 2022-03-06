#!/usr/bin/python

import argparse
import json
from exceptions import TranslationException

class Country:

    def __init__(self, translation):
        self.translation = translation

    def get_data(self):
        translationKeys = list()
        translationData = []
        with open("countries.json") as jsonFile:
            jsonData = json.load(jsonFile)
            for x in jsonData:
                tKeys = x['translations']
                translationKeys.extend(tKeys.keys())
                translationData.append(tKeys)
        translationKeys = list(set(translationKeys))
        if (self.translation not in translationKeys):
            raise TranslationException(self.translation)
        for d in translationData:
            if(self.translation in d):
                print(d[self.translation]['official'])


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Get all countries name for the specific translation keyword.')
        parser.add_argument('translations', metavar='translations', type=str, help='Translation keywords e.g. cym, deu, fra')
        args = parser.parse_args()
        c = Country(args.translations)
        c.get_data()
    except TranslationException as te:
        print(te)
    finally:
        print()
        print('...Completed...')
