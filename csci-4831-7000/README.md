# Boulder Cyclist Research

During my final semester at CU in the fall of 2019, I had to oportunity to participate in a graduate level course in which I could independently research a topic of my interest. My passion for biking and love for Boulder provided a great project for me to explore my interests while expanding my knowledge through self-teaching. Specifically, I wanted to better understand cyclist trends in Boulder while gaining experience with time series data and forecasting future traffic. Ultimately this research proved my ability to learn on the fly and confirmed my love for data. End results were published as a technical report via CU and can be found [here](https://scholar.colorado.edu/concern/reports/3j333305f). My individual report can be found under the 'paper' directory as [Research_Paper.pdf](https://github.com/jamu0075/Boulder-Bike-Research/blob/master/csci-4831-7000/paper/Research_Paper.pdf).

All analysis for this project were compiled in Jupyter Notebooks for rapid ad-hoc development. Research tasks changed on a near daily basis and I wanted to be able to quickly compare and update analyses.

## Data Collection

Data was collected via web scraping and a manual download from NOAA. All data collection/cleaning processes can be found in project/data_collection_cleaning. Here you will find two cleaning scripts and one scraping script. data_cleaning_bikers.py is a script that runs data_scraper_bikes.py and then performs cleaning tasks outlined in the report. dat_cleaning_weather.py performs cleaning tasks also outlined in the report but requires a manual download. Instructions on how to download and prepare the file for ingestions can be found in the script header.

The biker data is updated every 15 minutes, each time the scraper script is run the most up to date data is retrieved. Weather data is updated on a semi-monthly basis and requires a manual download to update.

Both cleaning scripts download a csv to your machine for the scope of this project. However, the data could just as easily have been put into a database for more logical access. The focus of this research was the analysis and did not require frequent updates to the data.

After successfully running both cleaning scipts you should have all the csv's required to run the analysis notebooks.
