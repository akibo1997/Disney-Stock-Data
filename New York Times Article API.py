import requests
import pandas as pd
import time
import matplotlib as plot

api_key = "LlxA0nsstWEGpNP3AKHW9gZo2XIrdWSF"

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"

query = "disney"

pages = []
url_list = []
category = []

for x in range(1,2):
    x = str(x)
    pages.append(x)

for page in pages:
    query_url = url + "q=" + query + "&begin_date=1990101&end_date=20191231&page=" + page + "&api-key=" + api_key
    print(query_url)

    articles = requests.get(query_url).json()
    

    # The "response" property in articles contains the actual articles
    # list comprehension.
    articles_list = articles["response"]["docs"]

    
    for article in articles_list:
        print(article["web_url"])
        url_list.append(article["web_url"])
        category.append(article["news_desk"])

    len(article["web_url"])
    # time.sleep(15)

data_list = list(zip(url_list, category))
df = pd.DataFrame(data_list, columns = ["URL","Category"])


df[["1","2","3","4","5","6","7","8","9"]] = df.URL.str.split("/",expand=True)

df.to_csv(r"Documents\Bootcamp\Disney-Stock-Data\Project Files Clean\NYT_Article_Pull.csv", index=False,)