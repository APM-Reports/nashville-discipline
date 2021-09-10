# Nashville Discipline

Allegations of retalitation abound at the Nashville Police.

*Created by Will Craft (<wcraft@apmreports.org>)*

*Reporter: Will Craft (<wcraft@apmreports.org>)*

## Project goal
In 2020, a video of a high ranking officer with the Metro Nashville Police Department harassing a woman went viral. As the video spread through social media, other women began to come forwards with their own stories of being harassed by police. Many of the women worked at the department themselves, and described how the department failed to hold their abusers accountable.

WPLN and APM Reports heard from over a dozen sources at the department who described a two-tiered discipline system. They alleged that white officers in the good graces of the department were treated leniently, while women and employees of color were often held to a much higher standard. We wanted to know if this was isolated to a few of the most high-profile cases that emerged after the department’s own MeToo movement, or if there was a broader pattern in the disciplinary system.

We gathered 10 years of discipline data from the department, available here, in order to analyze how the department treats employees of different races and genders.

## Project notes

### Data sources

* `cleaned_discipline_final.csv`
  * This is the spreadsheet used in the analysis of discipline at the MNPD. It is the result of a series of automated and manual data cleaning present in `etl/discipline_name_cleaning`. Details on the pipeline are in `etl/discipline_name_cleaning/README.md`

* `2010-2020.xlsx`
  * this is a spreadsheet of the discipline brought against every officer from 2010 to 2020. It includes the allegation, the date of the final disposition, and the outcome of the invesitgation into the alleged misconduct.

* `staff_roster_up_to_date`
  * this is a staff roster containing standardized names for officers at the department, their start date, and their demographic information.

#### Data not used
* `Report 6-14-21 Data Request.xls`
  * this spreadsheet is a list of all discipline issued against officers. This is a dataset that is one row per charge, not per incident, which makes analysis very difficult.


## Technical
### Project setup instructions
After cloning the repo, run `pipenv install` to install dependencies. If you are rebuilding the cleaning process, read details on the etl pipeline in `etl/discipline_name_cleaning`.

Fact-checking documents and notebooks can be found in `analysis/archive`
