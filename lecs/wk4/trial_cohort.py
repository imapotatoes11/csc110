#import data for 392 subjects in a cancer research trial
from sample_patient_data import *


# You just imported 24 variables into your Python program. The variable
# names and explanations are listed below in the data dictionary.
# ---------------------------------------------------------------------------
# Data dictionary
# ---------------------------------------------------------------------------
# ids<str>.                   Unique patient ID.
#
# initial_diagnosis_date<str> Date of initial disease diagnosis.
# first_line_start_date<str>  Start date of first-line (1L) treatment.
#
# first_line_end_date<str>    End date of 1L treatment. Blank = still ongoing or
#                               unknown.
#
# regimen[lst[lst[str]]]      Drug(s) making up the patient's 1L regimen. list of
#                             lists of strings, one drug name per string.
#
# sub_line_start_date<str>    Start date of the NEXT line of therapy after 1L, if
#                             the patient received one. Blank = no further line.
#
# n_lots<int>                 Total number of lines of therapy (lots) the patient
#                             has received, including 1L.
#
# age_at_diagnosis<int>       Patient age in years at initial diagnosis.
#
# sex<str>                    'male' or 'female'.
#
# ipi_score<int>              International Prognostic Index score (IPI) at diagnosis
#                             (higher = worse prognosis).
#
# ipi_assessed<str>           Date the IPI score was assessed.
#
# grade<str>                  FL histologic grade ('grade_1', 'grade_2', 'grade_3',
#                             'grade_3a', or 'low'). Blank = not recorded.
#
# grade_date<str>             Date grade was assessed.
#
# disease_stage<str>          Ann Arbor stage at diagnosis ('iii', 'iv', or
#                             'discrepant_information' where records conflict).
#                             Blank = not recorded.
#
# stage_date<str>             Date disease stage was assessed.
#
# date_of_death<str>          Date of death, if the patient has died. Blank =
#                             no death recorded (patient alive or lost to
#                             follow-up).
#
# pd_date<str>                Date of disease progression, if progression was
#                             observed. Blank = no progression recorded.
#
# last_known_alive_date<str>  Most recent date the patient was confirmed alive.
#
# cr<str>                     'complete_response' if the patient achieved a
#                             complete response to 1L treatment. Blank = did not
#                             achieve CR (or not recorded).
#
# cr_date<str>                Date complete response was achieved.
#
# os<float>                   Overall survival: months from first_line_start_date
#                             to death, or to last_known_alive_date if censored.
#
# os_censor_flag<int>         0 = death observed (event). 1 = censored (patient
#                             was alive/lost to follow-up at last observation).
#
# pfs<float>                  Progression-free survival: months from
#                             first_line_start_date to progression or death, or
#                             to last known follow-up if censored.
#
# pfs_censor_flag<int>        0 = progression or death observed (event). 1 =
#                             censored (event-free at last observation).
# ---------------------------------------------------------------------------

# Context: Every clinical trial defines its subject pool with a precise list of 
# inclusion and exclusion criteria — conditions a patient must meet, and 
# conditions that disqualify them — so that the resulting cohort is narrow 
# enough to draw reliable conclusions from.

# ToDo: Construct a set of subjects suitable for a clinical trial that you are planning.
# To acheive this, you must implement the following inclusion/exclusion (I/E) criteiria
# using tools that you've learned in this course up until this point. 
#
# Inclusion Criteria:
#   - Higher baseline risk (IPI >= 3)
#   - Received a bendamustine-containing first-line regimen
#   - Was diagnosed on or after January 1, 2018
#
# Exclusion Criteria:
#   - Subjects who received more than one total lines of therapy
#   - Subjects who do not stage 3 or 4. 

ls = []
for i in range(len(ids)):
    if ipi_score[i] >= 3 and "bendamustine" in regimen[i][0] and int(initial_diagnosis_date[i][-4:]) >= 2018 and \
        not (sub_line_start_date[i] and disease_stage[i]):
        ls.append(i)
print(ls, len(ls))


print([i for i in range(len(ids)) if ipi_score[i] >= 3 and "bendamustine" in regimen[i][0] and int(initial_diagnosis_date[i][-4:]) >= 2018 and not (sub_line_start_date[i] and disease_stage[i])])

"""
# prof solution
# style 1
cohort = []
for i in range(len(ids)):
    selected = True
    if int(initial_diagnosis_date[i][-4:]) < 2018:
        selected = False
    ...

# Style 2, comprehensions
legal_date = {ids[i] for i in range(len(ids)) \
    if (initial_diangnosis_date[i][-4:]) >= 2018}
...
cohort = legal_date.intersection(...)
"""
