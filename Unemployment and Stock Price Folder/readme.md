Readme for Analysis of Unemployment Rate and Initial Claims Data vs. Disney Stock

--- Table of Contents ---
1. Question
2. Hypothesis
3. Variables
4. Methodology
5. Findings
6. Summary
7. What's missing
-------------------------

1. Question: This section specifically looks at unemployment rate and initial claims data to see if there is a correlation with Disney stock price. The overall purpose of this investigation is to see what factors most impact Disney's market value. 

2. Hypothesis: The initial hypothesis investigated was that there would be a negative correlation between unemployment rate and initial claims, and Disney stock price. That is as unemployment rate and initial claims increase, the Disney stock price should decrease.

3. Variables and Data:  The variables used for this analysis are:
            - The monthly national unemployment rate 
            - The monthly initial claims count
            - The monthly close prices for Disney stock 
            Datasets for unemployment rate and initial claims were retrieved from FRED Economic data, 
            St. Louis Federal Reserve Bank.
            The dataset for Disney stock price was retrieved from GuruFocus.com. 

4. Methodology: 
4a. Disney Stock data cleaning process
- Renamed the columns and replaced the extra column names in the dataframe
- Make a data frame with just the date and close prices
- Convert the close price column to floats
- Format the date into Year-Month
- Group the data by YearMonth and average the close prices
- Sort values

4b. Unemployment rate data cleaning process
- Format the date into Year-Month
- Create a data frame with the new Year-Month column and unemployment rate column

4c. Initial claims data cleaning process
- Format the date into Year-Month
- Group the data by Year-Month instead of by week and sum the initial claims

Then, we joined the Disney stock data to the unemployment rate and initial claims data separately. We dropped any NA value columns in the process (as there were extra months of data in both the unemployment rate dataset and the initial claims data set.) We then reset the indices. 

5. Findings:
- We did line charts for unemployment rate and Disney stock price, as well as initial claims and Disney stock price. Each plot had two y-axis and the Year-Month along the x-axis. 
We also applied correlations and linear regressions. 
Our findings are as follows:
- As unemployment rate increases or decreases, the stock price reacts inversely. The correlation coefficient was found to be -0.36 as well. Thus, there is a low to moderate correlation between the two. 
- The number of monthly initial claims does not greatly influence Disney stock price. The correlation coefficient was found to be -0.02. 

6. Summary:
Thus, there is a low to moderate negative correlation found between unemployment rate and Disney stock price. The line graph and scatter plot reflects this as well. On the other hand, there was very little correlation found between initial claims and Disney stock price. This could partially be because they are in two vastly different scales, so they are difficult to compare, as initial claims are in the millions and mean stock price is in the tens and hundreds scale.

7. What's missing: 
There should be more data and analysis on how much inflation or attractiveness of the company (demand by investors) reflects the increase in stock price over the years. Finally, there may be a better way to correlate initial claims and Disney stock price after properly accounting for the different scales of the numbers. 

            





