# Crime Prediction in San Francisco

![time-lapse-video-San-Francisco](C:\Users\Work\Documents\Crime-Prediction-in-San-Francisco\images\time-lapse-video-San-Francisco.jpg)

## Introduction


## Libraries
* Python 3
* Scikit-learn 0.22.1
* NumPy 1.17.5
* Pandas 0.25.3
* Matplotlib 3.1.2
* Seaborn 0.9.0
* SciPy 1.4.1



## Dataset Overview

- **`San Francisco Crime Classification Dataset`** - This dataset contains the reported crimes that occurred in San Francisco from *01/01/2003* to *05/13/2015*. It has *878,049* records.
  - **`Date & Time`** - Timestamp of the crime incident
  - **`Category`** - Category of the crime incident
  - **`Description`** - Detailed description of the crime incident
  - **`Day of the Week`** - The day of the week
  - **`Police Department District`** - Name of the Police Department District
  - **`Resolution`** - How the crime incident was resolved
  - **`Address`** - The approximate street address of the crime incident
  - **`X`** - Longitude
  - **`Y`** - Latitude

Source: https://www.kaggle.com/c/sf-crime/data



**`San Francisco Weather Dataset`** - Scraped weather data for every day in the *San Francisco Crime Classification Dataset*. It contains 4516 records.

- **`date`** - Date of recorded data
- **`avg_temp`** - Average temperature *(Celsius)*
- **`precipitation`** - Precipitation *(mm)*
- **`wind_speed`** - Wind speed *(km/h)*
- **`visibility`** - Visibility *(km)*
- **`moon_illumination, %`** - Moon phase and illumination *(Name of phase, %)*

Source: Scraped from https://wunderground.com/



## Exploratory Data Analysis

##### Crimes by Year

![crimes per year](C:\Users\Work\Documents\Crime-Prediction-in-San-Francisco\images\crimes per year.png)

##### Crimes by Day of the Week

![crimes by day of the week](C:\Users\Work\Documents\Crime-Prediction-in-San-Francisco\images\crimes by day of the week.png)

##### Crimes by Hour

![crimes per hour](C:\Users\Work\Documents\Crime-Prediction-in-San-Francisco\images\crimes per hour.png)



##### Crimes by Category

![crimes by category](C:\Users\Work\Documents\Crime-Prediction-in-San-Francisco\images\crimes by category.png)



##### Crimes by Police Department District - Bar Chart

![crimes by police department](C:\Users\Work\Documents\Crime-Prediction-in-San-Francisco\images\crimes by police department.png)

##### Crimes by Police Department District - Map

![labeled cumulative](C:\Users\Work\Documents\Crime-Prediction-in-San-Francisco\images\labeled cumulative.png)

The plot above is a visual representation of the crime count for each Police Department District in San Francisco where the darker colors denote a greater crime count.



**Legend:**

1. *Richmond*
2. *Taraval*
3. *Park*
4. *Ingleside*
5. *Northern*
6. *Mission*
7. *Central*
8. *Southern*
9. *Bayview*



##### Crimes Resolutions

![crime resolutions](C:\Users\Work\Documents\Crime-Prediction-in-San-Francisco\images\crime resolutions.png)

##### Yearly Average Temperature

![yearly temperature](C:\Users\Work\Documents\Crime-Prediction-in-San-Francisco\images\yearly temperature.png)





## Machine Learning Model



## Limitations and Issues

- Not all crimes can be predicted
- Racial profiling
- Neighborhood bias
- Crime displacement
- Privacy and constitutional concerns



## Conclusions