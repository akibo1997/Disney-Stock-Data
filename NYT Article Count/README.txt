Readme for Analysis of New York Time article count of disney related articles vs Disney stock.

            .-"""-.
           /       \
           \       /
    .-"""-.-`.-.-.<  _
   /      _,-\ ()()_/:)
   \     / ,  `     `|
    '-..-| \-.,___,  /
          \ `-.__/  /
         / `-.__.-\`
        / /|    ___\
       ( ( |.-"`   `'\
        \ \/    {}{}  |
         \|           /
          \        , /
          ( __`;-;'__`)
          `//'`   `||`
         _//       ||
 .-"-._,(__)     .(__).-""-.
/          \    /           \
\          /    \           /
 `'-------`      `--------'`


--- Table of Contents ---
1. Question
2. Hypothesis
3. Variables
4. Methodology
5. Findings
6. Summary
7. What's missing
-------------------------

--- 1. Question ---

Does the release of new Disney related articles from NYT results in a reaction in Disney stock price?

----------------

--- 2. Hypothesis ---

The stock price will react to Disney related news. The more articles that are written in a week, the larger the change.

---------------------

--- 3. Variables ---

The variables we will need for this analysis are:
	- The daily open and close stock prices for Disney stock since 1980.
	- The count of articles that mention Disney from NYT since 1980.

--------------------

--- 4. Methodology ---

4a. Disney data
The raw disney stock price data provided the open and close price for every weekday from 1980 to present. 
Using the date and a dayofweek function, a column was created to bin the data into weeks using Monday as the start of the week.

disney_df["Day of Week"] = disney_df["date"].dt.dayofweek
disney_df["Week"] = disney_df["date"] -  pd.to_timedelta(disney_df["Day of Week"], unit='d')

However, this still left the close price of the week in a different row from the open price of the week since those are different days.
Using the shift function, the close price column was pushed down to match the open and close in the same week.
Subtract the open from close and the result is the weekly change.

4b. NYT data
Used the NYT Article Search API to pull relevant articles from 1980 to present. Following the documentation, each request only pulls 10 articles, so a loop was needed to create multiple pulls.
Once the request was made, each article URL was appended to a master list and exported into CSV for manipulation.

With the csv file, the URL was broken out by "/" to get the publish date thats embedded in the URL. However, one issue that arrose was due to the quantity of pages being pulled, there were a few URLs that did not follow the usual structure.
These URLs were removed by looking at the regular "Year" column and removing any rows that had longer than a 4 character string. To check the remaining URLs were correct, a pull of the unique values in the "Year" column was done.
The next steps were similar to those of the disney data by creating dates and binning the rows into weeks.

A groupby count function will tell us how many URL's were binned into each week, that count column will be our "Count of Articles" column we need.

4c. Merge
The two datasets were now cleaned and ready to go. A merge was done on the "Week" to create a unified dataset.

----------------------

--- 5. Findings ---

The findings show a slight relationship between the two numbers. Using a line chart we can see occurences of the "Count of Articles" spiking along with positive or negative change with the stock price.
In the scatter plot, the dots closer to the left and right sides represent large changes to the stock price. If our hypothesis was correct, the higher up the dots go, the further the dots should lean to either side.
We see a large group of dots that are low and to the center, while the dots closer to the sides are higher up as well.

-------------------

--- 6. Summary ---

While this analysis gives a quick look into the relationship between the two numbers, it in no way provides a conclusive answer to the correlation between the two. 
Other questions to ask might be: Is the relationship opposite the hypothesis, perhaps a drastic change in stock price is what prompted the news. Are there outside factors that have nothing to do with Disney that caused stock price changes?
This analysis would be better suited as a tool to track what was happening in the news to provide context to stock price changes. If someone wanted to know more about the stock price change in August 2015, they could use this tool to first identify if there was news at the time, and then what those articles were.

------------------

--- 7. What's missing ---

Other blog sites that are more relevant to financial news could be a better analysis and provide a wider range of article counts.
Good news vs bad news.
Was the article directly or indirectly discussing the Walt Disney Company.
...and more factors around how NYT writes articles.

-------------------------
