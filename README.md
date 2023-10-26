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
   - [Project 1: Exploratory Data Analysis for California Housin](#Project-1-Exploratory-Data-Analysis-for-California-Housin)
   - [Project 2: ](#Project-2)
   - [Project 3: ](#Project-3)
5. [Technologies Used In Portfolio](#Technologies-Used-In-Portfolio)
6. [Future Potential Projects](#Future-Potential-Projects)
   - [Project 1: English Premier League Match Predictions & Player Statistics](#Project-1-English-Premier-League-Match-Predictions-&-Player-Statistics)
   - [Project 2: Road Lane Line Detection](#Project-1-Road-Lane-Line-Detection)
   - [Project 3: Visualizing Climate Change](#Project-2-Visualizing-Climate-Change)
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

# [Project 1: Exploratory Data Analysis for California Housin](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/tree/main/Exploratory%20Data%20Analysis%20for%20California%20Housin)
## Description:
In this project, I conducted an in-depth Exploratory Data Analysis (EDA) of the California Housing dataset, aiming to gain insights into housing trends in various cities in California. The primary objective of this analysis is to provide valuable information to potential homebuyers, real estate professionals, and policymakers. By uncovering key patterns and trends in the data, this analysis can assist in making informed decisions regarding housing investments and urban planning.

## Data Sets: 
I used the ['California_Housing_Cities.csv'](https://github.com/DanielGiedraitis/Data-Science-Machine-Learning-Portfolio/tree/main/Exploratory%20Data%20Analysis%20for%20California%20Housin) dataset, which contains information on various features related to housing in California cities. The dataset consists of 20640 rows and 17 columns, including features like median house value, median income, population, and distance to important locations like the coast, Los Angeles, San Diego, San Jose, and San Francisco.

The dataset was obtained from [Kaggle](https://www.kaggle.com/datasets/abdallahsamman/california-housing-with-name-of-counties/data) and is relevant to the problem as it provides comprehensive information about housing in California cities.

## Data Processing Techniques:
Data preprocessing is a crucial step in any data analysis project. In this project, I performed several data processing tasks, including:
- Removal of the 'Id' column, which was irrelevant for the analysis.
- Handling of missing values by identifying and replacing empty strings with NaN values.
- Calculated new features to better understand the dataset.

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
- Python for data manipulation and analysis
- Pandas for data handling
- NumPy for numerical operations
- Matplotlib and Seaborn for data visualisation
- Statsmodels for statistical analysis
- Plotly Express for interactive visualisations

## Techniques and Models:
In this project, I primarily focused on descriptive statistics and data visualisation techniques. I used histograms, box plots, and QQ plots to understand the distribution and summary statistics of key features like median house value, median income, and median age. Scatter plots were used to explore relationships between median income and median house value in different cities.

## Visualisations:
I used various data visualisations to enhance our understanding of the California housing dataset. They provide a clear visual representation of the data distribution, relationships, and summary statistics. These visualisations include:
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

### Project 2:


### Project 3:

<br>

## Technologies Used In Portfolio
- **Programming Languages**: Python, SQL, Java, C++.
- **Platforms**: Jupyter Notebook, Anaconda, Posit, Alteryx.
- **Frameworks and Libraries**: Pandas (for data manipulation and analysis), NumPy (for numerical operations), Matplotlib (for basic data visualisation), Seaborn (for advanced data visualisation), Statsmodels (for statistical analysis), Plotly Express (for interactive visualisations).
- **Databases**: Redis, PostgreSQL, MySQL, MongoDB.


## Future Potential Projects


### Project 1: English Premier League Match Predictions & Player Statistics


### Project 2: Visualizing Climate Change


### Project 3: Road Lane Line Detection 

<br>

## References



 

