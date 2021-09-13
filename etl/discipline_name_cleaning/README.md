Name Cleaning and Discipline Data Matching
-------------

We want to clean and standardize two sets of names:

1) The names of officers from the discipline incident spreadsheet. There are misspellings and duplicates in there that we can probably clean pretty well.

2) The all-staff roster.  

The end-result is a set of discipline incidents with the race/ethnicity of the officer.

# The final datasets
* staff_roster_cleaned.csv: the full roster for each year. One row is one officer and one year. So an officer that worked at the MNPD for 5 years would be in the data 5 times.
  * name - the officer's full name
  * job_desc - a specific job title, like Lieutenant, or Captain or Police Officer 2.
  * dept_desc - shortform job title, all rows in roster are Police  	
  * gender - Officer gender. Only M and F
  * race_ethnicity - Officer race/ethnicity. Multiracial was added seemingly in 2018 so we set the officer's race to multiracial if they listed their race as multiracial post-2018
  * date_started - the date the officer started. Will be consistent for each officer. 	
  * year - the roster year. We have the roster for each year from 2010 to 2021. 	
  * clean_name - the cleaned name used to match the data to discipline incidents.
  * clean_race_ethnicity - standardized race/ethnicity. Use this column to analyze race and ethnicity, not race_ethnicity.

* discipline_final.csv: the discipline data for the MNPD. One row is one discipline incident. If an officer was disciplined 5 times, there would be 5 rows representing those 5 incidents.
  * CONTROL # - unique ID for the discipline incident
  * FINAL DISP DATE - the date of the disposition for the discipline incident. This is basically the date of the discipline. 	
  * FINAL DISPOSITION - the disposition of the discipline incident, like whether it was unfounded or if the officer was exonerated. 	
  * FINAL # DAYS - The number of days the officer was suspended 	
  * EMPLOYEE LAST NAME - officer last name
  * EMPLOYEE FIRST NAME - officer first name
  * ALLEGATION - the allegation made against the officer 	
  * COMP SEX - the gender of the complaining officer
  * COMP RACE - the race of the complaining officer 	
  * full_name - the full name of the disciplined officer
  * clean_name_x - cleaned and standardized name from the discipline data
  * roster_name_match - the name from the roster that most closely matches the name from the discipline data.
  * clean_name_y - same as roster_name_match but an artifact of the joining process 	
  * gender - gender of the officer
  * clean_race_ethnicity - standardized race/ethnicity. Use this column to analyze race and ethnicity, not race_ethnicity.


# Cleaning steps

* `combine_roster_sheets.py` combines all the sheets in the roster spreadsheet, adds a year column, and saves the file as csv titled `staff_roster_cleaned.csv`

* `create_discipline_name_cleaner.py` takes the unique set of names from the staff roster and runs a matching process to match the bad names from discipline file to the canonical names from the staff roster. This will solicit command line input from the user. 

* After the semi-automated process of matching names, manually correct the following errors in the matching process. This needs to be edited in a text editor because there was no process for correcting mistakes during the name matching.
  * david harper: no match
  * david lang: david lang maximillian
  * jonathan sharp: ii jonathan sharp william
  * azchary huber: a huber zachary
  * joshua thiel: joshua lawrence melvin thiel
  * michael swoner: ernest m swoner
  * robert deberry: deberry j jr robert
  * robert johnson: anthony iii johnson robert
  * sara lober: kaitlin lober sara taylor
  * william boler: boler charlton william
  * no name: no match

* `match_discipline_to_roster_names.py` runs the crosswalk of discipline name to roster name

* `match_race_gender_to_discipline.py` merges the roster data to the discipline data
