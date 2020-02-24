from datetime import datetime as dt
import pandas as pd
import re

date = []
bid = []
ask = []
time_format = "%Y-%m-%d %H:%M:%S"

with open("2020-01-22_pro_EURGBP.txt", "r") as prices:
    next(prices)
    for line in prices:
        date_string = re.findall("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)[0]
        date_parsed = dt.strptime(date_string, time_format)
        date.append(date_parsed)
        split = line.split()
        bid.append(split[2])
        ask.append(split[3])
df = pd.DataFrame({"Bid": bid, "Ask": ask}, dtype="float64", index=date)


mean = df.resample("30S").mean()
first = df.resample("30S").first()
final = pd.merge(mean, first, left_index=True, right_index=True)
final = final.rename(
    columns={
        "Bid_x": "Average Bid",
        "Ask_x": "Average Ask",
        "Bid_y": "First Bid",
        "Ask_y": "First Ask",
    }
)

final.to_csv("ticks.csv")
