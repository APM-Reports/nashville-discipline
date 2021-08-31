import os
import json
import pandas as pd
from fuzzywuzzy import fuzz, process


def response_gather_test():

    valid_response = False
    #user_input = ''
    # while valid response is false, we'll try and get a valid response
    while not valid_response:
        # there are 5 tuples and a no response
        valid_responses = ['0','1','2','3','4','n']
        print('enter the index of the best match, n if no match:')
        user_input = input()

        if user_input in valid_responses:
            print('valid response!')
            valid_response = True
        else:
            print('invalid response')

    print(f'correct response: {user_input}')




if __name__ == '__main__':
    response_gather_test()
