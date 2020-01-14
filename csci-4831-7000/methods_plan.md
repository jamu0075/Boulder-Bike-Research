I have consolidated 12 datasets into 6, grouping by intersection. The tables 13th & Walunt, Folsom & BoulderCreek, Folsom & South St, 
Folsom & Pine, and Baseline & Inca follow the same schema :
- date (Month-Day-Year Time)
- nb (Northbound)
- sb (Southbound)
- total (nb + sb)  

The table Colorado & 30th has additional information:
- date (Month-Day-Year Time)
- nb (Northbound)
- sb(Southbound)
- wb (Westbound)
- eb_sidewalk (Eastbound bicyclists on the sidewalk)
- wb_sidewalk (Westbound bicyclists on the sidewalk)
- total

Additionally I have reached out to NOAA for Boulder's weather data and am now just waiting to revieve the requested weather data. The expected
data contains the max/min temperature along with percipitation(rain/snow) in boulder every day, lining up with the cyclist data.  

EDA: To get a better understanding for how people bike, I would like to plot the number of bikers every hour for each day of the week. Furthermore
I would like to see how this week view looks over a longer period of time(month, year, or even years.) I will also look at which directions(if any)
is traveled the most, in addition to intsection popularity.

Hypothesis 1: Weather has a significant impact on bicylce trends. It is no surprise that cold weather or rainy days keep people off of their bikes.
However, I would like to know more specifically when people decide against biking. I will use multiple linear regression between cyclist population 
and weather data (temp/percipication) to see the relationship between the two. Is there a significant temperature at which people stop biking?

Hypthesis 2: Cyclist population is ever growing, with popularity increasing more than linearly. I will use linear regression to see how the number of 
cyclists is increasing of the years. With data sets starting in 2011 there will be enough data to see how this trend has changed over nearly a decade.  

Analyses will be performed with python scikit-learn and preprocessing with pandas.

