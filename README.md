# Crime Prediction in San Francisco

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/time-lapse-video-San-Francisco.jpg?raw=true)

## Introduction


## Libraries
* Scikit-learn 0.22.1
* NumPy 1.17.5
* Pandas 0.25.3
* Matplotlib 3.1.2
* Seaborn 0.9.0
* SciPy 1.4.1



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



**`San Francisco 49ers Game Schedule`** - Collected data for San Francisco 49ers game between seasons *2003* and *2014*. The schedule for *Season 2015* was not include because it starts in Fall and the *San Francisco Crime Classification Dataset* ends in *05/13/2015*. It contains xx records.

- **`Date`** - Date of game
- **`Output`** - Whether the 49ers won or lost the game ("W", "L")
- **`Home`** - Whether the 49ers played home or away (1 = Home, 0 = Away)

Source: Collected from https://www.pro-football-reference.com/



## Exploratory Data Analysis

#### Crimes by Year

![crimes per year](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/crimes%20per%20year.png?raw=true)

#### Crimes by Day of the Week

![crimes by day of the week](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/crimes%20by%20day%20of%20the%20week.png?raw=true)

#### Crimes by Hour

![crimes per hour](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/crimes%20per%20hour.png?raw=true)



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



#### **Mean Daily Crimes vs. Mean Daily Temperature**

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/daily%20crimes%20vs%20temperature.png?raw=true)



####  Mean Daily Crimes vs. Day of Month

![](https://github.com/fescobar96/Crime-Prediction-in-San-Francisco/blob/master/images/daily%20crimes%20vs%20day%20of%20month.png?raw=true)





## Machine Learning Model



## Limitations and Issues

- Not all crimes can be predicted
- Racial profiling
- Neighborhood bias
- Crime displacement
- Privacy and constitutional concerns



## Conclusions