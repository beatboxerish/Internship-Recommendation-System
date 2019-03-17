# making sure everything works properly

import clean
import recommendation
import scrape
import pandas as pd

df = scrape.scrape()
df.to_csv('../information_from_links_remove.csv')
print('cleaning the dataset')
df_clean = clean.clean_prep_data(df)
df_clean.to_csv('../df_clean_remove.csv')
print('creating similarity matrix')
sim = clean.return_sim(df_clean)
sim.to_csv('../sim_remove.csv')
print('Here are the top 5 recommendations')
recs = recommendation.make_recs(sim, df_clean, 500, 5)

print(recs)
