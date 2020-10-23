import json
from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

with open('ohsumed.json', 'r') as f:
    ohsumed = json.load(f)

    print(ohsumed.keys())

    for k, v in take(10, ohsumed['texts'].items()):
        print('Key is: {}'.format(k))
        print(('Text is: {}'.format(v)))
        print('Annotations are: {}'.format(ohsumed['annotations'][k]))
        if k in ohsumed['training_labels']:
            print('Text is a training sample')
            print('Labels are: {}'.format(ohsumed['training_labels'][k]))
        else:
            print('Text is a testing sample')
            print('Labels are: {}'.format(ohsumed['testing_labels'][k]))

        print('_______________________________________________________')




