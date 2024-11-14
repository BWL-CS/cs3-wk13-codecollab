import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
'''
Data from Wikipedia: top followed TikTok accounts
Followers is in millions
Likes is in billions
'''

# https://seaborn.pydata.org/generated/seaborn.axes_style.html
custom_parameters = {'axes.facecolor': '#cfcfcf'}
sns.set_theme(style='ticks', palette='deep', font_scale=0.75, rc=custom_parameters)

df = pd.read_csv('TikTokData.csv')
print("\n DataFrame: \n", df)
print("\n DataFrame Info: \n", df.info())
print("\n Summary Statistics: \n", df.describe())
avg_views_by_genre = df.groupby('Genre')['Likes_Billions'].mean()
print("\n Average Likes by Genre:\n", avg_views_by_genre)

# 1. Bar plot for Followers
plt.figure(figsize=(10, 6))
sns.barplot(x='Followers_Millions', y='Creator', hue='Creator', data=df)
plt.title('Followers per Creator')
plt.savefig('followers_bar_plot.png', bbox_inches='tight')
plt.close()

# 2. Scatter plot for Followers vs Likes
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Followers_Millions', y='Likes_Billions', hue='Creator', data=df)
plt.legend([],[], frameon=False)
plt.title('Followers vs Likes')
plt.savefig('followers_vs_likes_scatter_plot.png', bbox_inches='tight')
plt.close()

# 3. LM plot
plt.figure(figsize=(10, 6))
sns.lmplot(x='Followers_Millions', y='Likes_Billions', data=df, legend=False)
plt.title('Linear Model of Followers vs Likes')
plt.savefig('linear_regression_plot.png', bbox_inches='tight')
plt.close()

# 4. Count plot
plt.figure(figsize=(10, 6))
sns.countplot(x='Genre', data=df)
plt.title('Number of Top Creators per Genre')
plt.savefig('genre_count_plot.png', bbox_inches='tight')
plt.close()

# 5. Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Genre', y='Likes_Billions', data=df)
plt.title('Likes Distribution per Genre')
plt.savefig('likes_box_plot.png', bbox_inches='tight')
plt.close()
