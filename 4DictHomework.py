# 1.3 Dictionaries homework
#
# Using data from Eurostat, create a list of tuples representing the “Self-perceived health by
# country and sex, age group >16, for people living in cities” for 2017-2018. Have at least
# 30 values in your dataset.
#
# The dataset will have the following structure:
# [(country, year, sex, health_index), ... ]
# Example:
# [(‘France’, 2017, M, 12), …]
#
# - one dict that groups all data by year for Germany
#     germany = {2017: [sex, health_index]}
#
# - one dict that grups all data by country and year, by using year in the
# key together with the country name
#     health_index = {‘France_2017’: [year, sex, health_index]}
#
# - starting from the previous health_index dict, display only the data where the health_index >5
# - starting from the previous health_index dict, display only the data where the health_index >5 and sex is ‘F’
# - starting from the previous health_index dict, create a for loop to print the health_index

dataset = [
    ('France', 2017, 'M',  12),
    ('Germany', 2017, 'M',  12),
    ('France', 2017, 'F',  13),
    ('France', 2017, 'M',  11),
    ('Albany', 2017, 'F',  1),
    ('Albany', 2017, 'M',  2),
    ('Austria', 2017, 'F',  3),
    ('Austria', 2017, 'M',  4),
    ('Belarus', 2017, 'M',  5),
    ('France', 2017, 'M',  10),
    ('Spain', 2017, 'F',  11),
    ('Spain', 2017, 'F',  19),
    ('Spain', 2017, 'M',  9),
    ('France', 2017, 'F',  1),
    ('Poland', 2017, 'M',  2),
    ('Portugal', 2018, 'M',  4),
    ('Poland', 2018, 'F',  6),
    ('Poland', 2018, 'M',  1),
    ('France', 2018, 'M',  2),
    ('Romania', 2018, 'F',  2),
    ('Romania', 2018, 'M',  3),
    ('Russia', 2018, 'M',  12),
    ('Serbia', 2018, 'F',  14),
    ('Kosovo', 2018, 'F',  15),
    ('Italy', 2018, 'M',  16),
    ('Italy', 2018, 'F',  17),
    ('Italy', 2018, 'F',  18),
    ('France', 2018, 'F',  19),
    ('Germany', 2018, 'M',  0),
    ('Germany', 2018, 'M',  1),
    ('France', 2018, 'F',  2),
    ('Turkey', 2018, 'M',  3),
    ('Malta', 2018, 'F',  1),
    ('France', 2018, 'M',  5)
]

# Using only comprehensions, create the following dicts:
# - two dicts that group all data by country for each year
#     health_index_2017 = {‘France’: [sex, health_index]}
#     health_index_2018 = {‘France’: [sex, health_index]}

# dict1 = { for }

