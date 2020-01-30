# Crime Prediction in San Francisco

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/time-lapse-video-San-Francisco.jpg?raw=true)



## Table of Contents

[TOC]

## Introduction

San Francisco's economy is continuously improving, but its wealth seems to be heavily undistributed; situation that has driven the crime rates higher than the nation average.


## Libraries
* BeautifulSoup 4.6.3

* Branca 0.3.1

* Folium 0.8.3

* GeoPandas 0.6.2

* Matplotlib 3.1.2

* NumPy 1.17.5

* Pandas 0.25.3

* Requests 2.21.0

* Scikit-learn 0.22.1

* SciPy 1.4.1

* Seaborn 0.9.0

* Shapely 1.6.4

* XGBoost 0.90

  



## Data Overview

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



**`San Francisco Weather Dataset`** - Scraped weather data for every day in the *San Francisco Crime Classification Dataset*. It contains *4516* records.

- **`date`** - Date of recorded data
- **`avg_temp`** - Average temperature *(Celsius)*
- **`precipitation`** - Precipitation *(mm)*
- **`wind_speed`** - Wind speed *(km/h)*
- **`visibility`** - Visibility *(km)*
- **`moon_illumination, %`** - Moon phase and illumination *(Name of phase, %)*

Source: Scraped from https://wunderground.com/



**`San Francisco 49ers Game Schedule`** - Collected data for San Francisco 49ers game between seasons *2003* and *2014*. The schedule for *Season 2015* was not include because it starts in Fall and the *San Francisco Crime Classification Dataset* ends in *05/13/2015*. It contains 200 records.

- **`Date`** - Date of game
- **`Output`** - Whether the 49ers won or lost the game ("W", "L")
- **`Home`** - Whether the 49ers played home or away (1 = Home, 0 = Away)

Source: Collected from https://www.pro-football-reference.com/



## Exploratory Data Analysis

#### Crimes per Year

![crimes per year](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/crimes%20per%20year.png?raw=true)

The plot above represents the cumulative crimes per year. It is important to mention that the San Francisco Crime Classification Dataset only included crime records up to May 13, 2015; this is why the yearly crime rate seems to suddenly improved in 2015, when in reality we are just missing data for most of that year.



#### Crimes by Day of the Week

![crimes by day of the week](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/crimes%20by%20day%20of%20the%20week.png?raw=true)

Crimes rates vary between days of the week, being Friday the day in which most crimes are committed on average while Sunday has the lowest crime rates of all days of the week. Please note that although the variations of crime rates between different days of the week seems to be relatively small, the day of the week plays an important role in improving our model's accuracy.



#### Average Crimes per Hour

![crimes per hour](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/crimes%20per%20hour.png?raw=true)

The hour of the day also plays an important role when trying to predict crimes rates. You can appreciate how 4:00am - 5:00am have the lowest crime rates. As we increase the hour, the crime rates increase on average until we reach 5:00pm. After 6:00pm, crime rates tend to decrease until 4:00am where the cycle repeats. Although the hour of the day is relevant to the predictions of the model, I decided not to use it as a feature because the dataset would suffer a significant reduction due to the fact that many hours of the day lack crime records. Additionally, having the crime records in a daily is consistent with the weather and football datasets.



#### Crimes by Category

![crimes by category](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/crimes%20by%20category.png?raw=true)



#### Crimes by Police Department District - Bar Chart

![crimes by police department](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/crimes%20by%20police%20department.png?raw=true)

#### Crimes by Police Department District - Map

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/Cumulative%20Crime%20Map%20labeled.png?raw=true)

The plot above is a visual representation of the crime count for each Police Department District in San Francisco where the darker colors denote a greater crime count.



#### Crimes Resolutions

![crime resolutions](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/crime%20resolutions.png?raw=true)

#### Correlation Matrix

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/correlation%20matrix.png?raw=true)



#### Mean Daily Crimes vs. Mean Daily Temperature

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/daily%20crimes%20vs%20temperature.png?raw=true)



####  Mean Daily Crimes vs. Day of Month

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/daily%20crimes%20vs%20day%20of%20month.png?raw=true)

#### Comparison of Crime Between NFL Game Day and Regular Day

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/game%20day%20vs%20regular%20day.png?raw=true)

#### Comparison of Crime Between NFL Home Game and Away Game

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/home%20game%20vs%20away%20game.png?raw=true)



#### Comparison of Crime Between NFL Win and Loss

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/nfl%20win%20vs%20loss.png?raw=true)



## Machine Learning

- xgboost regressor

#### Model

#### Hyperparameter Optimization

talk about hyperparameter optimization using gridsearchcv

| Parameters       | List of Values                       |
| ---------------- | ------------------------------------ |
| learning_rate    | [0.05, 0.10, 0.15, 0.20, 0.25, 0.30] |
| max_depth        | [3, 4, 5, 6, 8, 10, 12, 15]          |
| min_child_weight | [1, 3, 5, 7]                         |
| gamma            | [0, 0.1, 0.2, 0.3, 0.4]              |
| colsample_bytree | [0.3, 0.4, 0.5, 0.7]                 |

#### Score



- training score
- test score
- MAE



## Limitations and Issues

- Not all crimes can be predicted
- Racial profiling
- Neighborhood bias
- Crime displacement
- Privacy and constitutional concerns



## Conclusions