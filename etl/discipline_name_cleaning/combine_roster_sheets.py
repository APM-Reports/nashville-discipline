import os
import pandas as pd

def strip_text(df):
    name = df['name']
    name = name.lower().replace(',',' ').replace("'"," ").replace("."," ").replace('(', ' ').replace(')',' ').strip()
    clean_name = " ".join(sorted(name.split())) # this splits the name into words, alphebetizes and rejoins

    return clean_name

def clean_race_ethnicity(df):
    race = df.race_ethnicity

    if pd.isna(race):
        return pd.NA
    else:
        race = race.strip().lower()
        race_ethnicity_cleaner = {
            'white (not of hispanic origin)': 'white',
            'black': 'black',
            'asian or pacific islander': 'asian/pacific islander',
            'hispanic': 'hispanic',
            'american indian/alaskan native': 'native american',
            'unknown': 'unknown',
            'black': 'black',
            'hispanic': 'hispanic',
            'asian or pacific islander': 'asian/pacific islander',
            'unknown': 'unknown',
            'two or more races': 'multiracial',
            'asian': 'asian/pacific islander',
            'hawaiian or pacific islander': 'asian/pacific islander',
            'white': 'white',
            'american indian or alaskan native': 'native american',
            'black or african american': 'black',
            'hispanic or latino of any race': 'hispanic',
            'two or more races': 'multiracial',
            'asian': 'asian/pacific islander',
            'native hawaiian or other pacific': 'asian/pacific islander',
        }

    return race_ethnicity_cleaner[race]


if __name__ == '__main__':
    cwd = os.getcwd()
    data_dir = os.path.join(cwd, 'data')
    source_dir = os.path.join(data_dir, 'source')
    processed_dir = os.path.join(data_dir, 'processed')

    roster_xlsx = os.path.join(source_dir, 'staff_roster_up_to_date.xlsx')
    roster_destination = os.path.join(
        processed_dir,
        'staff_roster_cleaned.csv'
    )

    roster_df = pd.read_excel(
        roster_xlsx,
        sheet_name=None
    )

    column_cleaning = {
        '2015': {
            'Class . Description': 'Class # Description'
        },
        '2020': {
            'Job Title': 'Class # Description',
            'US Ethnic Origin': 'Ethnic Code Description',
            'Date First Hired': 'Date Started',
            'Current Dept Desc': 'Current Dept Description',

        },
        '2021': {
            'Job Title': 'Class # Description',
            'Adjusted Service Date': 'Date Started',
            'US Ethnic Origin': 'Ethnic Code Description',
            'Current Dept Desc': 'Current Dept Description'
        },
        'all': {
            'Alpha Name': 'name',
            'Class # Description': 'job_desc',
            'Current Dept Description': 'dept_desc',
            'Gender': 'gender',
            'Ethnic Code Description': 'race_ethnicity',
            'Date Started': 'date_started'
        }
    }

    # Trying a thing to save updated version of the sheet dataframes
    # inplace-editing of dataframes in the roster_df was tricky
    roster_dicts = []
    # cleaning the dataframes requires work. Standardize the column names
    for key, df in roster_df.items():
        df['year'] =  key
        if key in ['2015','2020','2021']:

            df = df.rename(
                columns = column_cleaning[key]
            )

        df = df.rename(
            columns = column_cleaning['all']
        )
        roster_dicts.append(df)

    # join the list of dicts together
    roster_df_cleaned = pd.concat(
        roster_dicts,
        ignore_index=True
    )

    # clean the names
    roster_df_cleaned['clean_name'] = roster_df_cleaned.apply(
            strip_text,
            axis=1
        )

    # clean the race/ethnicity columns
    roster_df_cleaned['clean_race_ethnicity']  = roster_df_cleaned.apply(
        clean_race_ethnicity,
        axis=1
    )

    roster_df_cleaned.to_csv(
        roster_destination,
        index=False
    )
