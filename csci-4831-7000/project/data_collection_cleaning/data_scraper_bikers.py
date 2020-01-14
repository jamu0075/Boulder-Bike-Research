#!/usr/bin/env python3

import pandas as pd
from io import StringIO
import requests

# A script to fetch the most up to date data from the city of Boulder via:
# https://bouldercolorado.gov/open-data/bicycle-traffic-counts
#
# The data consists of the number of bikers seen in the bike lane every
# 15 minutes and their direction. The intersections included are:
# 13th & Walnut, Colorado & 30th, Folsom & Boulder Creek, Folsom & South St.
# Folsom & Pine and Baseline & Inca.
#
# Outside of the multi-use paths(Which at the time, no data is available) these
# are some of the most heavily trafficed areas.
#
# Note: HTTP 403 Error bypass from: https://datascience.stackexchange.com/questions/49751/read-csv-file-directly-from-url-how-to-fix-a-403-forbidden-error

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def get_data():
    
    ########################################
    # 13th & Walnut
    ########################################
    try:
        print('Fetching 13th & Walnut...')
        url1 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_13th_Walnut.csv"
        text1 = requests.get(url1, headers=headers).text
        
        try:
            print('Reading 13th & Walnut...')
            df_thirtienth_walnut = pd.read_csv(StringIO(text1))
        except:
            print('An exception occurred while reading 13th & Walnut.')
    except:
        print('An exception occurred while fetching 13th & Walnut.')
        
    ########################################
    # Colorado & 30th Westbound
    ########################################
    try:
        print('Fetching Colorado & 30th Westbound...')
        url2 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_Colorado_WB_Just_West_of_30th.csv"
        text2 = requests.get(url2, headers=headers).text
        
        try:
            print('Reading Colorado & 30th Westbound...')
            df_colorado_thirtieth_WB = pd.read_csv(StringIO(text2))
        except:
            print('An exception occurred while reading Colorado & 30th. Westbound')
    except:
        print('An exception occurred while fetching Colorado & 30th. Westbound')
        
    ########################################
    # Colorado & 30th Northbound
    ########################################
    try:
        print('Fetching Colorado & 30th Northbound...')
        url3 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_30th_NB_South_of_COLO.csv"
        text3 = requests.get(url3, headers=headers).text
        
        try:
            print('Reading Colorado & 30th Northbound...')
            df_colorado_thirtieth_NB = pd.read_csv(StringIO(text3))
        except:
            print('An excpetion occurred while reading Colorado & 30th Northbound.')
    except:
        print('An exception occurred while fetching Colorado & 30th Northbound.')
        
    ########################################
    # Colorado & 30th Southbound
    ########################################
    try:
        print('Fetching Colorado & 30th Soundbound...')
        url4 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_30th_SB_South_of_COLO.csv"
        text4 = requests.get(url4, headers=headers).text
        
        try:
            print('Reading Colorado & 30th Southbound...')
            df_colorado_thirtieth_SB = pd.read_csv(StringIO(text4))
        except:
            print('An exception occurred while reading Colorado & 30th Southbound.')
    except:
        print('An exception occurred while fetching Colorado & 30th Southbound.')

    ########################################
    # Folsom & Boulder Creek Southbound
    ########################################
    try:
        print('Fetching Folsom & BoulderCreek Southbound...')
        url5 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_Folsom%20SB%20@%20Boulder%20Creek.csv"
        text5 = requests.get(url5, headers=headers).text
        
        try:
            print('Reading Folsom & BoulderCreek Southbound...')
            df_folsom_bouldercreek_SB = pd.read_csv(StringIO(text5))
        except:
            print('An exception occurred while reading Folsom & BoulderCreek Southbound.')
    except:
        print('An error occurred while fetching Folsom & BoulderCreek Southbound.')
        
    ########################################
    # Folsom & Boulder Creek Northbound
    ########################################
    try:
        print('Fetching Folsom & BoulderCreek Northbound...')
        url6 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_Folsom%20NB%20@%20Boulder%20Creek.csv"
        text6 = requests.get(url6, headers=headers).text
        
        try:
            print('Reading Folsom & BoulderCreek Northbound.')
            df_folsom_bouldercreek_NB = pd.read_csv(StringIO(text6))
        except:
            print('An exception occurred while reading Folsom & BoulderCreek Northbound.')
    except:
        print('An exception occurred while fetching Folsom & BoulderCreek Northbound.')
        
    ########################################
    # Folsom & South St. Southbound
    ########################################
    try:
        print('Fetching Folsom & South St. Southbound...')
        url7 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_Folsom%20@%20South%20St.%20-%20SB.csv"
        text7 = requests.get(url7, headers=headers).text
        
        try:
            print('Reading Folsom & South St. Southbound...')
            df_folsom_south_SB = pd.read_csv(StringIO(text7))
        except:
            print('An exception occurred while reading Folsom & South St. Southbound.')
    except:
        print('An exception occurred while fetching Folsom & South St. Southbound.')
        
    ########################################
    # Folsom & South St. Northbound
    ########################################
    try:
        print('Fetching Folsom & South St. Northbound...')
        url8 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_Folsom%20@%20South%20St.%20-%20NB.csv"
        text8 = requests.get(url8, headers=headers).text

        try:
            print('Reading Folsom & South St. Northbound...')
            df_folsom_south_NB = pd.read_csv(StringIO(text8))
        except:
            print('An exception occurred while reading Folsom & South St. Northbound.')
    except:
        print('An exception occurred while fetching Folsom & South. St. Northbound.')
        
    ########################################
    # Folsom & Pine Southbound
    ########################################
    try:
        print('Fetching Folsom & Pine Southbound...')
        url9 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_Folsom%20@%20Pine%20-%20SB.csv"
        text9 = requests.get(url9, headers=headers).text
        
        try:
            print('Reading Folsom & Pine Southbound...')
            df_folsom_pine_SB = pd.read_csv(StringIO(text9))
        except:
            print('An exception occurred while reading Folsom & Pine Southbound.')
    except:
        print('An exception occurred while fetching Folsom & Pine Southbound.')
        
    ########################################
    # Folsom & Pine Northbound
    ########################################
    try:
        print('Fetching Folsom & Pine Northbound...')
        url10 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_Folsom%20@%20Pine%20-%20NB.csv"
        text10 = requests.get(url10, headers=headers).text
        
        try:
            print('Reading Folsom & Pine Northbound...')
            df_folsom_pine_NB = pd.read_csv(StringIO(text10))
        except:
            print('An exception occurred while reading Folsom & Pine Northbound.')
    except:
        print('An exception occurred while fetching Folsom & Pine Northbound.')
        
    ########################################
    # Baseline & Inca Westbound
    ########################################
    try:
        print('Fetching Baseline & Inca Westbound...')
        url11 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_Baseline%20WB%20@%20Inca.csv"
        text11 = requests.get(url11, headers=headers).text
        
        try:
            print('Reading Baseline & Inca Westbound...')
            df_baseline_inca_WB = pd.read_csv(StringIO(text11))
        except:
            print('An exception occurred while reading Baseline & Inca Westbound.')
    except:
        print('An exception occurred while fetching Baseline & Inca Westbound.')
        
    ########################################
    # Baseline & Inca Eastbound
    ########################################
    try:
        print('Fetching Baseline & Inca Eastbound...')
        url12 = "http://www-static.bouldercolorado.gov/docs/opendata/bike_counters_Baseline%20EB%20@%20Inca.csv"
        text12 = requests.get(url12, headers=headers).text
        
        try:
            print('Reading Baseline & Inca Eastbound...')
            df_baseline_inca_EB = pd.read_csv(StringIO(text12))
        except:
            print('An exception occurred while reading Inca & Baseline Eastbound.')
    except:
        print('An exception occurred while fetching Baseline & Inca Eastbound.')

    return(
    df_thirtienth_walnut,
    df_colorado_thirtieth_WB,
    df_colorado_thirtieth_NB,
    df_colorado_thirtieth_SB,
    df_folsom_bouldercreek_SB,
    df_folsom_bouldercreek_NB,
    df_folsom_south_SB,
    df_folsom_south_NB,
    df_folsom_pine_SB,
    df_folsom_pine_NB,
    df_baseline_inca_WB,
    df_baseline_inca_EB
    )
