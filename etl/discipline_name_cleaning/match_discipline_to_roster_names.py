import os
import json
import pandas as pd

'''
This file matches the names in the discipline file to the names in the roster using the discipline-roster crosswalk, then merges the race/gender data we have from the roster to the discipline file.

Output should be a discipline file ready for matching the race/gender from the roster
'''

def import_crosswalk_json(path):
    '''
    Takes the path to the json crosswalk, which is a list of dicts

    I think it needs to be turned into a straight dictionary of names to matches.
    '''
    all_names = {}
    with open(path, 'r') as j:
        data = json.loads(j.read())
        # for every dict in the list of dicts
        for item in data:
            # this takes the key and value and adds each key:value to the all_names dict.
            # this changes the data structure from list of dicts to just a dict
            for key, value in item.items():
                all_names[key] = value
    return all_names

def prep_discipline_data(path):
    '''
    Take the discipline data and prepare it for matching with the crosswalk data
    '''
    incident_df = pd.read_excel(
        path,
        parse_dates = ['FINAL DISP DATE']
    )

    incident_df['full_name'] = incident_df['EMPLOYEE FIRST NAME'] + ' ' + incident_df['EMPLOYEE LAST NAME']
    incident_df['clean_name'] = incident_df['full_name'].str.strip().str.lower()
    incident_df['clean_name'] = incident_df['clean_name'].fillna(value='no name')

    return incident_df

if __name__ == '__main__':
    cwd = os.getcwd()
    data_dir = os.path.join(cwd, 'data')
    source_dir = os.path.join(data_dir,'source')
    manual_dir = os.path.join(data_dir, 'manual')
    processed_dir = os.path.join(data_dir, 'processed')

    incident_xlsx = os.path.join(source_dir, '2010-2020.xlsx')
    crosswalk_path = os.path.join(
        manual_dir,
        'discipline_incident_name_cleaning.json'
    )

    crosswalk = import_crosswalk_json(crosswalk_path)
    incident_df = prep_discipline_data(incident_xlsx)

    incident_df['roster_name_match'] = incident_df.apply(
        # crosswalk is a dict, with the clean names as keys and roster names as values
        lambda x: crosswalk[x.clean_name],
        axis =1
    )
    incident_df.to_csv(
        os.path.join(processed_dir, 'cleaned_discipline_data_with_crosswalk.csv'),
        index=False
    )
