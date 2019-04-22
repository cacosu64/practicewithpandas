import pandas as pd
import matplotlib.pyplot as plt

wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
wine_reviews.head()
