description = ('Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 '
])
raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 '])
]


# ': ' means that we don’t have data for that year.

# Instructions: For the implementation it is required:
# • function that prepares the dataset
# This function will take the raw dataset as an argument This function will return a dict
# with the following structure
# {
# 'Romania': [
# {
# 'year': '2019',
# 'coverage': 84
# }, {
# 'year': '2018',
# 'coverage': 67
# },
# ...,
# {
# 'year': '2011',
# 'coverage': 72
# }
# ],
# 'Germany': [
# {
# 'year': '2019',
# 'coverage': 94
# }, {
# 'year': '2018',
# 'coverage': 87
# },
# ...,
# {
# 'year': '2011',
# 'coverage': 82
# }
# ]
# }

# print(type(description))
# print(type(raw_data))
#
# print(description[1])
# print(raw_data[1][0])
# for item in zip(description[1], raw_data[0][1]):
#     if item[1] != ": ":
#         print(item)
# print(len(raw_data))


def raw_data_to_dict(description2, raw_data2):
    dict_to_return = {
        country: [{
            'year': year,
            'coverage': coverage
        }]
        for i in range(len(raw_data2))
        for country in [raw_data2[i][0]]
        for year, coverage in zip(description2[1], raw_data2[i][1])
        if coverage != ": "
    }
    return dict_to_return


print(" First requirement ______________________")
resultDict = raw_data_to_dict(description, raw_data)
for key, value in resultDict.items():
    print(key, ' : ', value)
# print(type(resultDict))
print('\n')

# • function to retrieve data for each year
# This function will take the dataset and year as an argument.
# This function will return any type that you choose.
# get_year_data(dataset, "2019")
# >>> {'2019': [('Romania', 84), ('Germany', 95), ..., ('Latvia', 85)]}
print(" Second requirement ______________________")


# for key, value in resultDict.items():
#     if '2019' in str(value):
#         for key2, value2 in value[0].items():
#             if key2 == 'coverage':
#                 print(key, value2)

# resDict = {}
# for key, value in resultDict.items():
#     countryVar = key
#     countryDict = value[0]
#     yearVar = countryDict['year']
#     coverageVar = countryDict['coverage']
#     print(countryVar, yearVar, coverageVar)


def get_year_data_to_dict(result_dict2, year_param):
    tuples_list = [(country2, coverage2)
                   for country2, value3 in result_dict2.items()
                   if year_param in str(value3)
                   for secondKey, coverage2 in value[0].items()
                   if secondKey == 'coverage'
                   ]
    dict_to_return = {year_param: tuples_list}
    return dict_to_return


resultDict3 = get_year_data_to_dict(resultDict, '2019')
# print(resultDict3)
for key, value in resultDict3.items():
    print(key, ' : ', value)
print('\n')

# • function to retrieve data for each country
# This function will take the dataset and country as an argument.
# This function will return any type that you choose.
# get_country_data(dataset, "Romania")
# >>> {'Romania': [('2019', 84), ('2018', 86), ..., ('2011', 72)]}
print(" Third requirement ______________________")


def get_country_data_to_dict(dataset, country_param):
    tuples_list = [value3
                   for country, value3 in dataset.items()
                   if country_param == country
                   for value3 in value3[0].values()
                   ]
    dict_to_return = {country_param: tuples_list}
    return dict_to_return


resultDict3 = get_country_data_to_dict(resultDict, 'RO')
for key, value in resultDict3.items():
    print(key, ' : ', value)

print('\n')

# • function to perform average from an iterable(of year data or country data)
# This function will take an iterable as an argument.
# This function will return a float.
# country_data = get_country_data(dataset, "Romania")
# perform_average(country_data['Romania'])
# >>> 79.4
print(" Last requirement ______________________")

def get_country_data_to_average(dataset, country_param):
    tuples_list = [average
                   for country, value3 in dataset.items()
                   if country_param == country
                   for key, value in value3[0].items()
                   if key == 'coverage'
                   ]
    dict_to_return = {country_param: tuples_list}
    return dict_to_return


resultDict3 = get_country_data_to_dict(resultDict, 'RO')
for key, value in resultDict3.items():
    print(key, ' : ', value)