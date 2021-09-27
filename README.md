# Nashville Discipline

Allegations of retalitation abound at the Nashville Police.

*Created by Will Craft (<wcraft@apmreports.org>)*

*Reporters: Will Craft (<wcraft@apmreports.org>), José Martínez (<martinez307jose@gmail.com>), Sam Max (<smax@wpln.org>)*

## Project goal
TK TK RE-WRITE COMING 

## Project notes

### Data sources

* `cleaned_discipline_final.csv`
  * This is the spreadsheet used in the analysis of discipline at the MNPD. Each row represents an allegation of misconduct at the department. The cleaned version is the result of a series of automated and manual steps present in `etl/discipline_name_cleaning`. Details on the pipeline are in [`etl/discipline_name_cleaning/README.md`](https://github.com/APM-Reports/nashville-discipline/tree/master/etl/discipline_name_cleaning). The final columns for the cleaned discipline file are:
    * CONTROL # - internal department reference number
    * FINAL DISP DATE - date of the final disposition
    * FINAL DISPOSITION - outcome of any investigation into the alleged misconduct
    * FINAL # DAYS - if the outcome was a suspension, the number of days
    * EMPLOYEE LAST NAME - last name of the officer
    * EMPLOYEE FIRST NAME - first name of the officer
    * ALLEGATION - the allegation
    * COMP SEX - gender of the complaintant
    * COMP RACE - race of the complaintant
    * full_name - full name of the officer
    * clean_name_x - a cleaned version of the officer's full name, for use in the semi-automated matching process
    * roster_name_match - the officer's name as it appears in the staff roster
    * clean_name_y - a cleaned version of the officer's full name, this is an artifact of the semi-automated matching process
    * gender - officer gender
    * clean_race_ethnicity - officer race/ethnicity. Multiracial wasn't used as a designation until 2018 in the staff roster so all officers who identified as multiracial after 2018 were assigned multiracial for discipline prior to 2018.

* `2010-2020.xlsx`
  * this is a spreadsheet of the discipline brought against every officer from 2010 to 2020. It includes the allegation, the date of the final disposition, and the outcome of the investigation into the alleged misconduct. It is one row per allegation.

* `staff_roster_up_to_date.xlsx`
  * this is a staff roster containing standardized names for officers at the department, their start date, and their demographic information. Each tab in the spreadsheet is one year, and each row in each tab is one officer.

#### Data not used
* `Report 6-14-21 Data Request.xls`
  * this spreadsheet is a list of all discipline issued against officers. This is a dataset that is one row per charge, not per incident, which makes analysis very difficult.


## Technical
### Project setup instructions
After cloning the repo, run `pipenv install` to install dependencies. If you are rebuilding the cleaning process, read details on the etl pipeline in `etl/discipline_name_cleaning`.

Fact-checking documents and notebooks can be found in `analysis/archive`
