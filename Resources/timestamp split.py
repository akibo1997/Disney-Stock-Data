import pandas as pd

file = "DisneyHistoricalStockPriceDataTab.csv"

df = pd.read_csv(file)

#df = pd.DataFrame({"timestamp": ["5/2/2018 "],"Second": ["g_h","i_j","k_l"]})
print(df)

df[["Third","Fourth"]] = df.timestamp.str.split(expand=True)

print(df)