#%%
import pandas as pd
import random
from faker import Faker

#%%
# Initializing the Faker
fake = Faker()

# Setting the number of campaigns to generate
num_campaigns = 10000

# Defining marketing channels
channels = ["Email", "Social Media", "TV", "Radio", "Search Engine"]


data = []

for _ in range(num_campaigns):
    campaign_name = fake.company()
    channel = random.choice(channels)
    spend = round(random.uniform(500, 50000), 2)
    
    # Logical relationship between spend and impressions
    impressions = int(spend * random.uniform(20, 50))
    
    # Clicks are a percentage of impressions
    ctr = random.uniform(0.01, 0.1)  
    clicks = int(impressions * ctr)
    
    # Conversions are a percentage of clicks
    conversion_rate = random.uniform(0.05, 0.2)  
    conversions = int(clicks * conversion_rate)
    
    # Revenue is based on conversions
    revenue_per_conversion = round(random.uniform(10, 50), 2)
    revenue = round(conversions * revenue_per_conversion, 2)
    
    start_date = fake.date_between(start_date="-3y", end_date="today")
    end_date = fake.date_between(start_date=start_date, end_date="+30d")
    

    if channel == "Email":
        spend = round(random.uniform(200, 1000), 2)
        impressions = int(spend * random.uniform(30, 60))
        ctr = random.uniform(0.05, 0.15)
        conversion_rate = random.uniform(0.1, 0.3)
    elif channel == "Social Media":
        spend = round(random.uniform(500, 3000), 2)
        impressions = int(spend * random.uniform(40, 80))
        ctr = random.uniform(0.03, 0.1)
        conversion_rate = random.uniform(0.05, 0.2)
    elif channel in ["TV", "Radio"]:
        spend = round(random.uniform(1000, 5000), 2)
        impressions = int(spend * random.uniform(50, 100))
        ctr = random.uniform(0.01, 0.05)
        conversion_rate = random.uniform(0.02, 0.1)
    else:  # Search Engine
        spend = round(random.uniform(1000, 4000), 2)
        impressions = int(spend * random.uniform(40, 70))
        ctr = random.uniform(0.04, 0.12)
        conversion_rate = random.uniform(0.1, 0.25)
    
    clicks = int(impressions * ctr)
    conversions = int(clicks * conversion_rate)
    revenue_per_conversion = round(random.uniform(10, 100), 2)
    revenue = round(conversions * revenue_per_conversion, 2)
    
# Introducing some Noise to avoid overly perfect correlation.

    spend = round(spend * random.uniform(0.9, 1.1), 2) 
    impressions = int(impressions * random.uniform(0.8, 1.2))
    clicks = int(clicks * random.uniform(0.8, 1.2))
    conversions = int(conversions * random.uniform(0.85, 1.15))
    revenue = round(revenue * random.uniform(0.9, 1.1), 2)

# Adding outliers to simulate real-world anomalies, such as exceptionally successful or failed campaigns.

    if random.random() < 0.05:  
        spend = round(spend * random.uniform(2, 5), 2)  
        revenue = round(revenue * random.uniform(0.1, 0.5), 2)  

# Including Region and Campaign type.

    campaign_type = random.choice(["Awareness", "Conversion", "Retargeting"])
    region = random.choice(["North America","South America", "Europe", "Asia","India"])
    data.append([campaign_name, channel, spend, impressions, clicks, conversions, revenue, start_date, end_date, campaign_type, region])

# %%
columns = [
    "Campaign_Name", "Channel", "Spend", "Impressions", "Clicks", 
    "Conversions", "Revenue", "Start_Date", "End_Date", "Campaign_Type", "Region"
]
df = pd.DataFrame(data, columns=columns)

# %%
df.head()
# %%
df.info()
# %%
df.to_csv("synthetic_campaign_data.csv", index=False)
print(df.head())
# %%
