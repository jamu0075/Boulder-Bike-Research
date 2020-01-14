#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os

##########################################
# A complete text file was imported from: https://www.esrl.noaa.gov/psd/boulder/data/boulderdaily.complete
# Using the shell, whitespace was converted to commas: sed -e 's/\s\+/,/g' boulderdaily.complete > boulderdaily.txt
# The new file has an empty space first column, drop the first column of commas using:
# cat boulderdaily.txt | sed 's/,//' > boulderdaily_clean.txt
# The text file can now be easily read into a dataframe.
##########################################

print('Creating Dataframe...')

df = pd.read_csv('boulderdaily_clean.txt', sep=",", header=None)
df.columns = ['year', 'month', 'day', 'tmax', 'tmin', 'precip', 'snow', 'snowcover']

print('Dataframe Created...')

# Drop unused data and reindex
print('Slicing Dataframe...')

df = df.loc[df[(df['year'] == 2011)].index[0]:, :]
df.drop(df.tail(1).index, inplace=True)
df.reset_index(drop=True, inplace=True)

print('Dataframe Sliced...')

# Combine year, month, date to a single datetime column
df['year'] = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce')

df.drop(columns=['month', 'day'], inplace=True)
df.rename(columns={'year': 'date'}, inplace=True)

# print(df.iloc[265:285])

##########################################
# Export the clean data to /data_cleaned
# Use OS for portability from: https://stackoverflow.com/questions/22872952/set-file-path-for-to-csv-in-pandas
##########################################

print('Exporting Clean Dataframe...')

path = r'/home/jacob/Dropbox/Fall2019/csci-4831-7000/project/data_cleaned/'
df.to_csv(os.path.join(path, r'weather_daily.csv'), index=False)

print('Exported!')
