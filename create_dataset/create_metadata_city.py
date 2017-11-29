import pandas as pd
import os
import matplotlib.pyplot as plt

metadata_df = pd.read_csv(os.path.expanduser("~/git/work/metadata/metadata.csv",index_col=0)
store = pd.HDFStore(os.path.expanduser("~/all.h5")

from collections import Counter
counter_dict = {}
for city in ["San Diego", "Boulder", "Austin", "Houston", "Dallas"]:
    print city
    only_city_df = metadata_df[metadata_df['city'] == city]
    counter_dict[city] = Counter()
    for building in only_city_df.index:
        try:
            counter_dict[city].update(store['/%d' %building].resample("1M")['use'].index)
        except:
            pass
    counter_dict[city] = pd.Series(counter_dict[city])


stream_counter_dict = {}
for city in ["San Diego", "Boulder", "Austin", "Houston", "Dallas"]:
#for city in ["Austin"]:
    print city
    only_city_df = metadata_df[metadata_df['city'] == city]
    stream_counter_dict[city] = Counter()
    for building in only_city_df.index:
        try:
            stream_counter_dict[city].update(store['/%d' %building].columns)
        except:
            pass

streams_df = pd.DataFrame(stream_counter_dict)

columns_to_use = {
    'survey_2011_all_participants.csv': [
        'males',
        'females',
        'age_under_5',
        'age_6_to_12',
        'age_13_to_18',
        'age_19_to_24',
        'age_25_to_34',
        'age_35_to_49',
        'age_50_to64',
        'age_over_65',
        'highest_education',
        'income_range',
        ],
    'survey_2013.csv': [
        'number_floors',
        'house_num_rooms',
        'house_square_feet',
        'sex_males',
        'sex_females',
        'residents_under_5',
        'residents_6_to_12',
        'residents_13_to_18',
        'residents_19_to_24',
        'residents_25_to_34',
        'residents_35_to_49',
        'residents_50_to_64',
        'residents_older_65',
        'education_level',
        'total_annual_income',
        ],
    'audits_2011.csv': ['no_bedrooms', 'year_built'],
    'audits_2013_main.csv': ['Number_of_Floors__c',
                             'Number_of_Bedrooms__c',
                             'Construction_Year__c'],
    'dataport-metadata.csv':['house_construction_year',
                             'total_square_footage']
    }

import seaborn as sns
sns.heatmap(streams_df.dropna().drop("use"), annot=True)
plt.savefig("../results/large_dataset_cities_streams.pdf", bbox_inches="tight")
plt.savefig("../results/large_dataset_cities_streams.png", bbox_inches="tight")
