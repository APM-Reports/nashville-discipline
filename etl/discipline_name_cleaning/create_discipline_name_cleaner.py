import os
import json
import pandas as pd
from fuzzywuzzy import fuzz, process


def console_matcher(incident_names, roster_names, destination_file):
    '''
    This is an attempt at a command line matching program to help match names between the roster and the list of discipline incidents.

    Takes the list of unique roster names that have been tokenized and cleaned and the unique list of names from the discipline file.

    For each name in the discipline file, take the matching name from the roster. Save to json file.
    '''

    automatic_name_matches = []
    manual_name_matches = []

    max_operations = len(incident_names) # max number of times we are going to have to run processing
    current_operation = 0 # We will iterate on every pass

    while current_operation <= max_operations - 1:
        # results: list of 5 tuples with the matching name and the match-score
        # for each tuple [0] is the name and [1] is the score
        results = process.extract(
            incident_names[current_operation],
            roster_names,
            scorer=fuzz.token_sort_ratio,
            limit=5
        )

        # if the score of the best result is better than 90, automatically add the matching dict to the list of matches
        if results[0][1] >= 90:
            automatic_name_matches.append(
                {incident_names[current_operation]: results[0][0]}
            )

        else:
            print(incident_names[current_operation])
            print(results)

            # set valid_response to false
            valid_response = False
            # while valid response is false, we'll try and get a valid response
            while not valid_response:
                # there are 5 tuples and a no response
                valid_responses = ['0','1','2','3','4','n']
                print('enter the index of the best match, n if no match:')
                user_input = input()

                if user_input in valid_responses:
                    valid_response = True

            if user_input == 'n':
                manual_name_matches.append(
                    {incident_names[current_operation]: 'no match'}
                )
            else:
                user_input_int = int(user_input)
                manual_name_matches.append(
                    {incident_names[current_operation]: results[user_input_int][0]}
                )

            print(f'names matched: {current_operation}')
            print(f'total names: {max_operations}')

        current_operation = current_operation + 1

    print('finished!')
    print('saving...')
    all_matches = automatic_name_matches + manual_name_matches
    with open(destination_file, 'w') as f:
        json.dump(all_matches, f)



if __name__ == '__main__':
    cwd = os.getcwd()
    data_dir = os.path.join(cwd, 'data')
    source_dir = os.path.join(data_dir,'source')
    manual_dir = os.path.join(data_dir, 'manual')
    processed_dir = os.path.join(data_dir, 'processed')

    cleaning_json = os.path.join(
        manual_dir,
        'discipline_incident_name_cleaning.json'
    )

    # the discipline data that is one-row-per-incident
    incident_xlsx = os.path.join(source_dir, '2010-2020.xlsx')
    incident_df = pd.read_excel(
        incident_xlsx,
        parse_dates = ['FINAL DISP DATE']
    )

    incident_df['full_name'] = incident_df['EMPLOYEE FIRST NAME'] + ' ' + incident_df['EMPLOYEE LAST NAME']
    incident_df['clean_name'] = incident_df['full_name'].str.strip().str.lower()

    # import cleaned staff roster names
    staff_roster_csv = os.path.join(processed_dir, 'staff_roster_cleaned.csv')
    staff_roster_df = pd.read_csv(staff_roster_csv)

    # create the list of unique names to match with
    incident_names = incident_df.clean_name.dropna().unique()
    roster_names = staff_roster_df.clean_name.dropna().unique()

    console_matcher(
        incident_names,
        roster_names,
        cleaning_json
    )
