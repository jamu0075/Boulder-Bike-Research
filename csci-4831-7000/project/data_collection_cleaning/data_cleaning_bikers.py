#!/usr/bin/env python3

import os
import pandas as pd
from data_scraper_bikers import get_data


# Collect raw data from Boulder using get_data()
df_thirtienth_walnut, df_colorado_thirtieth_WB, df_colorado_thirtieth_NB, df_colorado_thirtieth_SB, df_folsom_bouldercreek_SB, df_folsom_bouldercreek_NB, df_folsom_south_SB, df_folsom_south_NB, df_folsom_pine_SB, df_folsom_pine_NB, df_baseline_inca_WB, df_baseline_inca_EB = get_data()

# Some datasets have southbound data within the northbound set or vice versa.
# These are dropped for the sake of redundancy as well as inaccuracy.
df_colorado_thirtieth_NB.drop(columns='South_of_COLO_30th_Street_NB___Cyclists_SB', axis=1, inplace=True, errors='ignore')
df_colorado_thirtieth_SB.drop(columns='South_of_COLO_30th_Street_SB___Cyclists_NB', axis=1, inplace=True, errors='ignore')

##########################################
# Columns are renamed for consistancy.
##########################################
try:
    print('Renaming columns...')
    df_thirtienth_walnut.columns = ['date', 'nb', 'sb', 'total']
    df_colorado_thirtieth_WB.columns = ['date', 'wb', 'eb_pedestrains', 'wb_pedestrians', 'eb_sidewalk', 'wb_sidewalk', 'total']
    df_colorado_thirtieth_NB.columns = ['date', 'nb', 'total']
    df_colorado_thirtieth_SB.columns = ['date', 'sb', 'total']
    df_folsom_bouldercreek_SB.columns = ['date', 'sb', 'total']
    df_folsom_bouldercreek_NB.columns = ['date', 'nb', 'total']
    df_folsom_south_SB.columns=['date', 'sb', 'total']
    df_folsom_south_NB.columns=['date', 'nb', 'total']
    df_folsom_pine_SB.columns = ['date', 'sb', 'total']
    df_folsom_pine_NB.columns = ['date', 'nb', 'total']
    df_baseline_inca_WB.columns = ['date', 'wb', 'total']
    df_baseline_inca_EB.columns = ['date', 'eb', 'total']
except:
    print('An exception occurred while renaming columns.')

##########################################
# Merge dataframes on date for fewer dataframes/ease of understanding
# Print statements to confirm accurate merges.
##########################################

# 30th & Walnut - No changes

# Colorado & 30th
try:
    print('Merging Colorado & 30th sets...')
    df_colorado_thirtieth = df_colorado_thirtieth_NB.merge(df_colorado_thirtieth_SB.merge(df_colorado_thirtieth_WB, on='date'), on='date')
    
    try:
        print('Creating Colorado & 30th total column and dropping redundant columns...')
        df_colorado_thirtieth.drop(columns=['total','total_x', 'total_y'], inplace=True)
        df_colorado_thirtieth['total'] = df_colorado_thirtieth['nb'] + df_colorado_thirtieth['sb'] + df_colorado_thirtieth['wb']
        df_colorado_thirtieth['total_sidewalk'] = df_colorado_thirtieth['eb_sidewalk'] + df_colorado_thirtieth['wb_sidewalk']
    except:
        print('An exception occurred while creating Colorado & 30th total column and dropping redundant columns.')
except:
    print('An exception occurred while merging Colorado & 30th sets.')
              
# Folsom & BoulderCreek Path
try:  
    print('Merging Folsom & BoulderCreek sets...')
    df_folsom_bouldercreek = df_folsom_bouldercreek_NB.merge(df_folsom_bouldercreek_SB, on='date')
    
    try:
        print('Creating Folsom & BoulderCreek total column and dropping redundant columns...')
        df_folsom_bouldercreek.drop(columns=['total_x', 'total_y'], inplace=True)
        df_folsom_bouldercreek['total'] = df_folsom_bouldercreek['nb'] + df_folsom_bouldercreek['sb']
    except:
        print('An exception occurred while creating Folsom & BoulderCreek total column and dropping redundant columns.')
except:
    print('An exception occurred while merging Folsom & BoulderCreek sets.')
              
# Folsom & South St.
try:
    print('Merging Folsom & South St. sets...')
    df_folsom_south = df_folsom_south_NB.merge(df_folsom_south_SB, on='date')
    
    try:
        print('Creating Folsom & South St. total column and dropping redundant columns...')
        df_folsom_south.drop(columns=['total_x', 'total_y'], inplace=True)
        df_folsom_south['total'] = df_folsom_south['nb'] + df_folsom_south['sb']
    except:
        print('An exception occurred while creating Folsom & South St. total column and dropping redundant columns.')
except:
    print('An exception occurred while merging Folsom & South sets.')

# Folsom & Pine St.
try:
    print('Merging Folsom & Pine St. sets...')
    df_folsom_pine = df_folsom_pine_NB.merge(df_folsom_pine_SB, on='date')
    
    try:
        print('Creating Folsom & Pine St. total column and dropping redundant columns...')
        df_folsom_pine.drop(columns=['total_x', 'total_y'], inplace=True)
        df_folsom_pine['total'] = df_folsom_pine['nb'] + df_folsom_pine['sb']
    except:
        print('An exception occurred while creating Folsom & Pine St. total column and dropping redundant columns.')
except:
    print('An exception occurred while merging Folsom & Pine St. sets.')

# Baseline & Inca
try:
    print('Merging Baseline & Inca sets...')
    df_baseline_inca = df_baseline_inca_EB.merge(df_baseline_inca_WB, on='date')
    
    try:
        print('Creating Baseline & Inca total column and dropping redundant columns...')
        df_baseline_inca.drop(columns=['total_x', 'total_y'], inplace=True)
        df_baseline_inca['total'] = df_baseline_inca['wb'] + df_baseline_inca['eb']
    except:
        print('An exception occurred while creating Baseline & Inca total column and dropping redundant columns.')
except:
    print('An exception occurred while merging Baseline & Inca sets.')


##########################################
# Export the clean data to /data_cleaned
# Use OS for portability from: https://stackoverflow.com/questions/918154/relative-paths-in-python
##########################################

dirname = os.path.dirname(__file__)

def download_csv(df, file_name):
    try:
        print('Downloading {} to /data_cleaned...'.format(file_name))
        df.to_csv(os.path.join(dirname, '../data_cleaned/{}.csv'.format(file_name)), index=False)
    except:
        print('An exception occurred while downloading {}'.format(file_name))
           
download_csv(df_thirtienth_walnut, 'thirtienth_walnut')
download_csv(df_colorado_thirtieth, 'colorado_thirtieth')
download_csv(df_folsom_bouldercreek, 'folsom_bouldercreek')
download_csv(df_folsom_south, 'folsom_south')
download_csv(df_folsom_pine, 'folsom_pine')
download_csv(df_baseline_inca, 'baseline_inca')
