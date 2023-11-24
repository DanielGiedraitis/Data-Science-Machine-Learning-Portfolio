# Data Science & Machine Learning Portfolio

---

Welcome to my data science and machine learning portfolio, showcasing a collection of both ongoing and completed projects. This portfolio includes links to current projects in my portfolio as well as examples of my hands on experience in the different fields of Data Science and Machine Learning.

## Table of Contents

1. [About me](#About-Me)
   - [Profile](#Profile)
   - [Education](#Education)
   - [Experience](#Experience)
   - [Technologies](#Technologies)
2. [Introduction](#Introduction)
3. [Background](#Background)
4. [Portfolio Contents](#Portfolio-Contents)
   - [Project 1: Exploratory Data Analysis for California Housing](#Project-1-Exploratory-Data-Analysis-for-California-Housing)
   - [Project 2: New York Motor Vehicle Collisions](#Project-2-New-York-Motor-Vehicle-Collisions)
5. [Technologies Used In Portfolio](#Technologies-Used-In-Portfolio)
6. [Future Potential Projects](#Future-Potential-Projects)
   - [Project 1: English Premier League Match Predictions & Player Statistics](#Project-1-English-Premier-League-Match-Predictions-&-Player-Statistics)
   - [Project 2: Road Lane Line Detection](#Project-1-Road-Lane-Line-Detection)
   - [Project 3: Visualising Climate Change](#Project-2-Visualising-Climate-Change)
8. [References](#References)


# About me  
   ## Profile
   - **Name:** Daniel Giedraitis
   - **Email:** daniel.giedraitis@gmail.com
   - **Other Projects:** https://github.com/DanielGiedraitis
   - **LinkedIn:** https://www.linkedin.com/in/daniel-giedraitis

   ## Education 
   - Bachelor of Science in Software Development, [South East Technological University](https://www.setu.ie/)
      
   ## Experience
   - Internship at The Department of Agriculture, Food & the Marine from March 2023 to August 2023

   ## Technologies
   - Java, C++, Angular, Python, Java Swing, HTML, CSS, PHP, JavaScript, Arduino, EASY68K, and SQL.

     
# Introduction
In a world increasingly driven by data, the ability to harness the power of data to solve complex problems and make informed decisions has become very important. This portfolio represents my journey through the fascinating realm of data science and machine learning. Through a series of carefully crafted projects, I aim to showcase not only my technical proficiency but also my passion for addressing real world challenges using data driven solutions.


# Background
The utility and significance of my portfolio come from its ability to demonstrate my expertise in data science and machine learning to future employers and collaborators. Data science has become the cornerstone of innovation across industries, from healthcare and finance to marketing and e-commerce. Machine learning, a subset of artificial intelligence, has revolutionized predictive modeling, enabling accurate forecasting, pattern recognition, and automation.

<br>

# Portfolio Contents

# [Project 1: Exploratory Data Analysis for California Housing](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/tree/main/Exploratory%20Data%20Analysis%20for%20California%20Housin)
## Description:
In this project, I conducted an in-depth Exploratory Data Analysis (EDA) of the California Housing dataset, aiming to gain insights into housing trends in various cities in California. The primary objective of this analysis is to provide valuable information to potential homebuyers, real estate professionals, and policymakers. By uncovering key patterns and trends in the data, this analysis can assist in making informed decisions regarding housing investments and urban planning.

## Data Sets: 
I used the ['California_Housing_Cities.csv'](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/tree/main/Exploratory%20Data%20Analysis%20for%20California%20Housin) dataset, which contains information on various features related to housing in California cities. The dataset consists of 20640 rows and 17 columns, including features like median house value, median income, population, and distance to important locations like the coast, Los Angeles, San Diego, San Jose, and San Francisco.

The dataset was obtained from [Kaggle](https://www.kaggle.com/datasets/abdallahsamman/california-housing-with-name-of-counties/data) and is relevant to the problem as it provides comprehensive information about housing in California cities.

**Dataset details:**
1. Unique identifier for each data point in the dataset.
2. Median House Value: Median value of houses in a block (in US Dollars) [$]
3. Median Income: Median income of households in a block (in tens of thousands of US Dollars) [10k$]
4. Median Age: Median age of houses in a block (in years)
5. Total Rooms: Total number of rooms in a block
6. Total Bedrooms: Total number of bedrooms in a block
7. Population: Total number of residents in a block
8. Households: Total number of households in a block
9. Latitude: Indicates how far north a house is (higher value means farther north) [°]
10. Longitude: Indicates how far west a house is (higher value means farther west) [°]
11. Distance to Coast: Distance to the nearest coastal point [m]
12. Distance to Los Angeles: Distance to the center of Los Angeles [m]
13. Distance to San Diego: Distance to the center of San Diego [m]
14. Distance to San Jose: Distance to the center of San Jose [m]
15. Distance to San Francisco: Distance to the center of San Francisco [m]
16. Relative location of the block in relation to the ocean, providing insights into the proximity of the housing block to the coast.
17. The county in which the household resides.


## Data Processing Techniques:
Data preprocessing is a crucial step in any data analysis project. In this project, I performed several data processing tasks, including:
- **Removal of Irrelevant Columns:** Removal of the 'Id' column, which had no relevance for the analysis.
- **Handling Missing Values:** Addressing missing data by identifying and replacing empty strings with NaN values.
- **Feature Engineering:** Calculating new features to gain deeper insights into the dataset.

## Code Samples:

### Data Preprocessing section:
This code displays the first five rows of the "Data" DataFrame. It provides a quick look at the dataset to see what the data looks like at the beginning.

![head](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/581700e9-2288-4977-8f14-58638a817450)

This displays the last five rows of the "Data" DataFrame, showing the data's end.

![tail](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/37f9cb6c-e10d-4340-b646-67135e8db46a)

Data.info() provides an overview of the dataset's information, including the number of non-null entries, data types of each column, and memory usage. It's useful for understanding the data's structure and identifying any missing values.

![info](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/17a97e8c-1a19-4480-8e71-32097d7c4355)

The following code drops the 'Id' column from the California Houses dataset. This step is performed to remove unnecessary columns that may not contribute to the model's prediction.

![drop](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/5df769c2-dc00-4302-892f-a8d811057afa)

Data.describe() generates summary statistics for numerical columns in the dataset. It includes statistics such as mean, standard deviation, minimum, maximum, and quartiles. This summary provides an initial understanding of the distribution of numerical data.

![latitude](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/7d998961-ffa4-444e-b5a2-10c37664dcba)

The code block below provides some exploratory data analysis. It prints the number of data points in the dataset, checks for duplicates, and identifies missing values in the DataFrame. It also replaces empty values with NaN and rechecks the missing values after replacement.

![missing data](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/273c6e91-3f54-4827-aba4-6dec8677f31f)

Heatmap to visualise missing data:

![visualisation](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/39111626-69e7-4ec3-b095-cef37505394f)


## Tools and Technologies:
- [Python](https://www.python.org/) for data manipulation and analysis
- [Pandas]((https://pandas.pydata.org/) for data handling
- [NumPy](https://numpy.org/) for numerical operations
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for data visualisation
- [Statsmodels](https://www.statsmodels.org/stable/index.html) for statistical analysis
- [Plotly Express](https://plotly.com/python/plotly-express/) for interactive visualisations

## Techniques and Models:
In this project, I primarily focused on descriptive statistics and data visualisation techniques. I used histograms, box plots, and QQ plots to understand the distribution and summary statistics of key features like median house value, median income, and median age. Scatter plots were used to explore relationships between median income and median house value in different cities.

## Visualisations:
I used various data visualisations to enhance my understanding of the California housing dataset. They provide a clear visual representation of the data distribution, relationships, and summary statistics. These visualisations include:
1. **Histograms:** Utilized to visualise the distribution of key variables, including Median House Value, Median Income, Median Age, Total Rooms, Total Bedrooms, Population, and Households. Histograms provide insights into the data's central tendencies and spread, allowing for a better understanding of the data's characteristics.
2. **Count Plot:** Used to display the distribution of the 'ocean_proximity' variable. This count plot helps to visualise the frequency of different categories within the variable, which helps to understand the makeup of the categorical data.
3. **Scatter Plot:** Created to illustrate the relationship between Median Income and Median House Value. Scatter plots reveal potential patterns or correlations between two continuous variables, helping identify trends in the data.
4. **Heatmap:** I used a heatmap to visualise missing data in the dataset. The heatmap provides a color-coded grid that helps us quickly identify areas with missing values. This is crucial for understanding the completeness of the dataset.
5. **Box Plots:** Used to visualise the distribution of Median House Value, Median Income, Median Age, Total Rooms, Total Bedrooms, Population, and Households. Box plots provide a summary of the data's central tendencies, spread, and the presence of outliers, facilitating comparisons across variables.
6. **QQ Plots:** I used QQ plots to check if the distributions of Median House Value and Median Income were close to a normal (bell-shaped) distribution. These plots helped us detect any deviations from the typical bell curve shape, which can be important for certain statistical analyses.

## Data Visualisation: Visualising Key Housing Metrics
Summary statistics for the column Median House Value:

![MedianHouse](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/6c54021d-e70e-4c3f-bdfb-fb4443a9c7ee)

Visually test if Median House Value is normally distributed using a QQ plot:

![MedianHouse2](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/0cea3653-ed69-41ad-b671-751df9dbbfe5)

Summary statistics for the column Median Income:

![income](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/08839a69-3040-4bb5-8b8f-359c0880429a)

Median Age of a house within a block:

![age](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/ab753553-560a-4f4d-831a-cf96d5281db8)

Number of Rooms per Block:

![rooms](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/93795510-f40b-41ff-9bdc-dd26c640ac16)

Number of Bedrooms per Block:

![bedrooms](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/793aa08e-b5cf-43bd-9f81-c74e5cff1318)

Total number of people residing within a block:

![population](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/3c4b9a26-e5e8-4bc2-ae12-b48a3cdbc710)

Total number of househoulds within a block:

![households](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/3aab65e6-f7e5-45fd-a89c-1be336d0e68d)

Distribution of cities in California:

![cities](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/5e2e47c4-ac6c-4d5d-a19c-50b1acc2838c)

Distribution of ocean proximity in California:

![proximity](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/f437a158-ad9c-4451-9d46-cdf4587bac97)

Scatterplot on Median Income Vs Median House Value:

![vs](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/c9ce6ed6-d50b-49c5-826f-0efc06c45199)

---

<br>

## Inclusion and utilisation of online sources/links/blogs/data sources:
**Dataset:** [Kaggle](https://www.kaggle.com/datasets/abdallahsamman/california-housing-with-name-of-counties/data)

**Blog:** [Medium](https://towardsdatascience.com/create-a-model-to-predict-house-prices-using-python-d34fe8fad88f)

## Ethics and Regulations:
I have taken ethical considerations into account in this project. The dataset does not contain sensitive personal information, and I have not performed any advanced machine learning techniques that could potentially lead to bias or unfairness. I ensured the privacy of data by not disclosing any personally identifiable information.

Regarding regulations, I followed standard data handling practices and complied with relevant data protection regulations such as GDPR.

## Opportunities and Challenges:
**Opportunities:**
- Through this project, I gained valuable insights into the factors influencing housing prices in California cities.
- The use of various data visualisation techniques helped me communicate my findings effectively.
- Exploring the California housing market dataset presented an opportunity to work on a real-world problem, strengthening my practical data science knowledge.

**Challenges:**
- Data preprocessing, including handling missing values, was necessary to ensure data quality.
- Selecting the most appropriate visualisation techniques for each feature was a challenge but resulted in informative visualisations.
- Managing the balance between data accuracy and privacy was a challenge, especially when dealing with geographic data.

<br>

---

# [Project 2: New York Motor Vehicle Collisions]()
## Description:
In this project, I undertook a comprehensive Exploratory Data Analysis (EDA) focused on motor vehicle collisions in New York. The goal was to delve into the extensive dataset related to vehicular incidents, aiming to extract meaningful insights into collision patterns across different areas of New York. The primary aim of this analysis is to offer valuable information for drivers, law enforcement, and urban planners. By identifying key patterns and trends within the data, this analysis aims to contribute to informed decision-making regarding road safety measures, traffic management, and overall improvement in the city's transportation infrastructure.

## Data Sets: 
I used the ['Motor_Vehicle_Collisions_-_Crashes.csv']() dataset, which contains information on various features related to New York Motor Vehicle Collisions. The dataset consists of 2,010,526 rows and 29 columns, including features like crash date, crash time, location, number of persons injured, number of persons killed, types of vehicles etc...

The dataset was obtained from [NYC Data](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95) and is relevant to the problem as it provides comprehensive information about New York Motor Vehicle Collisions.

**Dataset details:**
1. CRASH DATE: Occurrence date of collision Date & Time.
2. CRASH TIME: Occurrence time of collision.
3. CRASH MONTH Occurrence month of collision.
4. CRASH HOUR: Occurrence hour of collision.
5. CRASH WEEK: Occurrence week of collision.
6. CRASH SEASON: Occurrence season of collision.
7. NUMBER OF PERSONS INJURED: Number of persons injured.
8. NUMBER OF PERSONS KILLED: Number of persons killed.
9. NUMBER OF PEDESTRIANS INJURED: Number of pedestrians injured.
10. NUMBER OF PEDESTRIANS KILLED: Number of pedestrians killed.
11. NUMBER OF CYCLIST INJURED: Number of cyclists injured.
12. NUMBER OF CYCLIST KILLED: Number of cyclists killed.
13. NUMBER OF MOTORIST INJURED: Number of vehicle occupants injured.
14. NUMBER OF MOTORIST KILLED: Number of vehicle occupants killed.
15. CONTRIBUTING FACTOR VEHICLE 1: Factors contributing to the collision for designated vehicle.
16. VEHICLE TYPE CODE 1: Type of vehicle based on the selected vehicle category (ATV, bicycle, car/suv, ebike, escooter, truck/bus, motorcycle, other).


## Data Processing Techniques:
Data preprocessing is a crucial step in any data analysis project. In this project, I performed several data processing tasks, including:
- **Removal of Irrelevant Columns:** Removed coloumns which had no relevance for the analysis.
- **Data Standardization:** Standardized the format of the "VEHICLE TYPE CODE 1" column by merging similar vehicle categories. This step improved consistency and streamlined the analysis of collision data involving various vehicle types.
- **Temporal Feature Extraction:** Extracted temporal features such as "CRASH YEAR," "CRASH MONTH," "CRASH MONTH NAME," "CRASH HOUR," and "CRASH WEEK" from the "CRASH DATE." This facilitated the analysis of collision trends over different time intervals.
- **Creation of Additional Features:** Introduced a new feature, "CRASH SEASON," based on the "CRASH MONTH," providing a categorical representation of collisions in different seasons. This additional feature enhances the ability to explore seasonal variations in                                              collision patterns.
- **Data Retention:** A subset of relevant columns was retained for further analysis, focusing on key variables related to collisions, including temporal information, casualties, contributing factors, and vehicle types.
- **Duplicate Removal:** Identified and removed duplicate entries to ensure data consistency and prevent skewing of analytical results.
- **Categorical Data Handling:** Processed categorical variables, including replacing specific vehicle categories with more general terms. This not only standardized the dataset but also facilitated a clearer understanding of the types of vehicles involved in                                           collisions.
- **Exploratory Data Analysis (EDA):** Conducted an initial EDA to gain insights into the distribution of key variables, identify outliers, and understand the overall structure of the dataset.
- **Visualization Data Preparation:** Structured the data in a format suitable for visualization, aggregating information for specific analyses such as yearly trends, hourly distributions, and seasonal patterns.

## Code Samples:

## Tools and Technologies:
- [Python](https://www.python.org/) for data manipulation and analysis
- [Pandas](https://pandas.pydata.org/) for data handling
- [NumPy](https://numpy.org/) for numerical operations
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for data visualisation

## Techniques and Models:


## Visualisations:
The analysis involved various data visualisations to gain insights into motor vehicle collisions in New York. The visualisations include:

1. **Yearly Collision Trends:** A bar plot depicting the number of collisions each year from 2012 to 2022, providing an overview of the overall trend.

2. **Hourly Collision Distribution:** A bar plot illustrating the distribution of collisions throughout the day, highlighting peak hours and potential patterns.

3. **Yearly and Weekly Collision Patterns:** A grouped bar plot displaying the number of collisions for each year, categorized by days of the week. This visualisation helps identify weekly patterns over the years.

4. **Seasonal Analysis:** A bar plot showcasing the number of collisions for each season, providing insights into how collision rates vary across different seasons.

5. **Yearly and Seasonal Comparison:** A grouped bar plot comparing collision counts across years, categorized by seasons. This visualisation allows for a deeper understanding of seasonal trends over the years.

6. **Top 5 Vehicle Types:** A bar plot highlighting the top five vehicle types involved in collisions over the years.

7. **Top 3 Contributing Factors:** A grouped bar plot comparing the top three contributing factors to collisions each year.

8. **Yearly Casualty Comparison:** Two bar plots comparing the number of persons injured and killed, providing insights into the overall impact of collisions over the years.

9. **Hourly Casualty Distribution:** Multiple bar plots illustrating the distribution of casualties (injured and killed) across different hours of the day, categorized by pedestrian, cyclist, and motorist involvement.

10. **Pedestrians Injured and Pedestrians Killed:** Bar plots displaying the number of pedestrians injured and killed during collisions, providing insights into pedestrian safety trends.

11. **Cyclists Injured and Cyclists Killed:** Bar plots illustrating the number of cyclists injured and killed during collisions, aiding in understanding the risks associated with cycling.

12. **Motorists Injured and Motorists Killed:** Bar plots showcasing the number of motorists injured and killed during collisions, contributing to a comprehensive analysis of overall road safety.

These visualisations collectively offer a comprehensive understanding of motor vehicle collisions in New York, highlighting temporal patterns, contributing factors, and the impact on casualties across different categories.

## Data Visualisation: Visualising Key Road Collision Metrics
Number Of Road Collisions Over The Years: 2012 - 2022

![Image1](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/8005f6ef-f633-403d-907f-c7687117c57d)

---

Number Of Collisions During Different Hours Of The Day:

![Image2](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/86a57b26-ed54-495d-913d-a503d0a1590f)

---

Number Of Road Collisions During Different Years And Days Of Week:

![Image3](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/9fdfb03f-92d9-4239-91c2-af4167ffb416)

---

Number Of Road Collisons During Each Season Of The Year:

![Image4](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/ac3b35ec-e87f-41fc-b1dc-8a0b2a8f2988)

---

Number Road Collisons Over Years and Seasons:

![Image5](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/9bafc177-d538-4a67-95d1-b1705f9d31f4)

---

Top 5 Vehicle Types Causing Road Collisons Over Years:

![Image6](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/46592f34-82aa-4b00-9a84-aa4e72b1c39b)

---

Comparison Of The Top 3 Factors Causing Road Collisons:

![Image7](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/84a071af-16a6-42cb-90b4-5f8afba48eeb)

---

Number Of Collisions During Differrent Days OF The Week:

![Image8](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/95258c0f-40cc-43cb-8546-98d8b3dcdc55)

---

Persons Injured and Persons Killed Over Years:

![Image9](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/594bac2b-5e68-4f74-915c-33a457b995a6)

---

Pedestrians Injured and Pedestrians Killed:

![Image10](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/8f3049a8-a1e8-4cf2-abc5-4e94ef2bddb6)

---

Cyclists Injured and Cyclists Killed:

![Image11](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/879cffa2-a4c0-49cc-b4e3-e3545d1df736)

---

Motorists Injured and Motorists Killed

![Image12](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/assets/91562130/5a602acb-139f-40e8-bd1c-43299001904e)

---

<br>

## Inclusion and utilisation of online sources/links/blogs/data sources:
**Dataset:** [NYC Data](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95)

## Ethics and Regulations:
I have taken ethical considerations into account in this project. The dataset does not contain sensitive personal information, and I have not performed any advanced machine learning techniques that could potentially lead to bias or unfairness. I ensured the privacy of data by not disclosing any personally identifiable information.

Regarding regulations, I followed standard data handling practices and complied with relevant data protection regulations such as GDPR.

## Opportunities and Challenges:
**Opportunities:**
- Through this project, I gained valuable insights into the factors influencing motor vehicle collisions in New York.
- The use of various data visualization techniques helped me communicate my findings effectively.
- Exploring the New York motor vehicle collisions dataset presented an opportunity to work on a real-world problem, strengthening my practical data science knowledge.

**Challenges:**
- Data preprocessing, including handling missing values, was necessary to ensure data quality.
- Selecting the most appropriate visualisation techniques for each feature was a challenge but resulted in informative visualisations.
- Managing the balance between data accuracy and privacy was a challenge, especially when dealing with geographic data.
  
<br>

---

## Technologies Used In Portfolio
- **Programming Languages**: [Python](https://www.python.org/), [Java](https://dev.java/), [C++](https://cplusplus.com/).
- **Platforms**: [Jupyter Notebook](https://jupyter.org/), [Anaconda](https://www.anaconda.com/), [Posit](https://posit.co/).
- **Frameworks and Libraries**: [Pandas](https://pandas.pydata.org/) (for data manipulation and analysis), [NumPy](https://numpy.org/) (for numerical operations), [Matplotlib](https://matplotlib.org/) (for basic data visualisation), [Seaborn](https://seaborn.pydata.org/) (for advanced data visualisation), [Statsmodels](https://www.statsmodels.org/stable/index.html) (for statistical analysis), [Plotly Express](https://plotly.com/python/plotly-express/) (for interactive visualisations).
- **Databases**: [Redis](https://redis.com/), [MySQL](https://www.mysql.com/), [MongoDB](https://www.mongodb.com/).


## Future Potential Projects


### Project 1: English Premier League Match Predictions & Player Statistics


### Project 2: Visualising Climate Change


### Project 3: Road Lane Line Detection 

<br>

## References



 

