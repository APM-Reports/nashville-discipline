import os
import pandas as pd

'''
This file takes the staff roster and the cleaned discipline file and matches the race/gender of the roster file name to the discipline df
'''

def get_race(df):
    name = df.clean_name
    slices = staff_roster_df[
        staff_roster_df.clean_name == name
    ]
    race_list = slices.clean_race_ethnicity.unique()

    if len(race_list) == 1:
        return race_list[0]

    if len(race_list) > 1:
        if 'multiracial' in race_list:
            return 'multiracial'
        else:
            return 'unknown'

def get_gender(df):
    name = df.clean_name
    slices = staff_roster_df[
        staff_roster_df.clean_name == name
    ]

    gender = slices.gender.value_counts().index[0]

    return gender


if __name__ == '__main__':
    cwd = os.getcwd()
    data_dir = os.path.join(cwd, 'data')
    source_dir = os.path.join(data_dir,'source')
    manual_dir = os.path.join(data_dir, 'manual')
    processed_dir = os.path.join(data_dir, 'processed')

    staff_roster_csv = os.path.join(processed_dir, 'staff_roster_cleaned.csv')
    staff_roster_df = pd.read_csv(staff_roster_csv)

    cleaned_discipline_data_with_crosswalk_csv = os.path.join(
        processed_dir,
        'cleaned_discipline_data_with_crosswalk.csv'
    )
    cleaned_discipline_data_with_crosswalk_df = pd.read_csv(
        cleaned_discipline_data_with_crosswalk_csv
    )

    # we have to have a flat staff roster. Get only the names
    flat_staff_roster = staff_roster_df.groupby(
        ['clean_name']
    ).size().reset_index().rename(columns={0:'count'})

    # add race, correcting for the difficulties in adding multiracial as a category
    flat_staff_roster['clean_race_ethnicity'] = flat_staff_roster.apply(
        get_race,
        axis=1
    )

    # add gender, correcting for the people with more than one gender listed.
    flat_staff_roster['gender'] = flat_staff_roster.apply(
        get_gender,
        axis=1
    )

    discipline_final = cleaned_discipline_data_with_crosswalk_df.merge(
        flat_staff_roster[['clean_name', 'gender', 'clean_race_ethnicity']],
        how='left',
        left_on='roster_name_match',
        right_on='clean_name'
    )

    discipline_final.to_csv(
        os.path.join(processed_dir, 'cleaned_discipline_final.csv'),
        index=False
    )
