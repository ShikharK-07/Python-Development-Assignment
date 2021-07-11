import pandas as pd
import numpy as np
import json

df = pd.read_json('data.json', lines=True)
df_new = df.rename(columns={"a": "address", "liid": "profile_url",
                            "linkedin": "linkedin_id", "n": "name", "t": "mob_number", "e": "email"})

# data_main.csv
df_1 = df_new.drop(['mob_number', 'email'], axis=1)
df_1.to_csv('data_main.csv', index=False)

#  data_email.csv
df_2 = df_new.drop(['address', 'profile_url', 'name', 'mob_number'], axis=1)
df_2.to_csv('data_email.csv', index=False)

# data_number.csv
df_3 = df_new.drop(['address', 'profile_url', 'name', 'email'], axis=1)
df_3.to_csv('data_number.csv', index=False)
