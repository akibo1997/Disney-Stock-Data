import requests
import pandas as pd
import time
import matplotlib as plot

# API Key
api_key = "LlxA0nsstWEGpNP3AKHW9gZo2XIrdWSF"

# URL for NYT Article Search API request
url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"

# Our search query
query = "disney"

# Empty lists for use in loops.
pages = []
url_list = []

# For loop to determine how many pages to query.
for x in range(1,51):
    x = str(x)
    pages.append(x)

# For loop to run multiple queries and pull more than 10 articles.
for page in pages:
    query_url = url + "q=" + query + "&begin_date=1980101&page=" + page + "&api-key=" + api_key

    articles = requests.get(query_url).json()
    
    # Creating a list to pull the needed data from API.
    articles_list = articles["response"]["docs"]

    # For loop to pull specifically URL and Category into lists to be used for DataFrame.
    for article in articles_list:
        # Print just to show script is still running.
        print(article["web_url"])
        url_list.append(article["web_url"])

    # Print page number
    print(f"{page} of 50")
    
    # Add delay to ensure script does not get blocked.
    time.sleep(15)

# Turn into dataframe.
df = pd.DataFrame(url_list, columns = ["URL"])

# Split URL to make it easier to extract date later.
df[["1","2","3","4","5","6","7","8","9"]] = df.URL.str.split("/",expand=True)

# Turn DataFrame into CSV file
df.to_csv(r"Documents\Bootcamp\Disney-Stock-Data\Project Files Clean\NYT_Article_Pull.csv", index=False,)