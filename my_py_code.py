import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker
from datetime import datetime

# Load and prepare the data from path
file_path = "C:\\Users\\MAZ YAFAI\\Desktop\\maaz\\cricketers.csv"  # file path
cricket_data = pd.read_csv(file_path)
cricket_data['Date_Of_Birth'] = pd.to_datetime(cricket_data['Date_Of_Birth'], errors='coerce')
cricket_data['Year_Of_Birth'] = cricket_data['Date_Of_Birth'].dt.year
average_debut_age = 22
cricket_data['Approx_Debut_Year'] = cricket_data['Year_Of_Birth'] + average_debut_age

# Function for  Line Chart
def plot_debut_year_line_chart_by_country_pro(data, start_year, end_year, top_n_countries=3):
    plt.figure(figsize=(14, 8))
    filtered_data = data[(data['Approx_Debut_Year'] >= start_year) & (data['Approx_Debut_Year'] <= end_year)]
    top_countries = filtered_data['Country'].value_counts().head(top_n_countries).index
    palette = sns.color_palette("husl", n_colors=top_n_countries)
    for i, country in enumerate(top_countries):
        country_data = filtered_data[filtered_data['Country'] == country]
        debut_year_counts = country_data['Approx_Debut_Year'].value_counts().sort_index()
        sns.lineplot(x=debut_year_counts.index, y=debut_year_counts.values, label=country, color=palette[i], linewidth=2.5)
    plt.title(f'Number of Players Debuting per Year by Country (Top {top_n_countries} Countries, {start_year}-{end_year})', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Number of Players', fontsize=14)
    plt.legend(title='Country', title_fontsize='13', fontsize='12')
    plt.grid(True, linestyle='--')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    sns.despine()
    plt.show()

# Function for Pie Chart
def plot_country_distribution_pie_chart(data):
    country_counts = data['Country'].value_counts().head(10)
    plt.figure(figsize=(10, 8))
    plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("tab10"))
    plt.title('Distribution of Players by Country (Top 10 Countries)', fontsize=14)
    plt.show()

# Function for Bar Chart
def plot_average_matches_by_country_bar_chart(data):
    average_matches = data[['Country', 'Test', 'ODI', 'T20']].groupby('Country').mean()
    average_matches['Total'] = average_matches.sum(axis=1)
    sorted_averages = average_matches.sort_values(by='Total', ascending=False).head(10)
    plt.figure(figsize=(12, 8))
    sorted_averages[['Test', 'ODI', 'T20']].plot(kind='bar', stacked=True)
    plt.title('Average Number of Matches Played by Country (Top 10)', fontsize=14)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Average Matches Played', fontsize=12)
    plt.show()

# Function for Box Plot
def plot_matches_comparison_boxplot(data):
    plt.figure(figsize=(10, 6))
    ax = sns.boxplot(data=data[['Test', 'ODI', 'T20']].fillna(0), orient='v', palette='Set2')
    plt.title('Comparison of Matches Played (Test, ODI, T20)', fontsize=14)
    plt.xlabel('Match Type', fontsize=12)
    plt.ylabel('Number of Matches Played', fontsize=12)
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.show()

# Generating each plot
plot_debut_year_line_chart_by_country_pro(cricket_data, 2010, 2020, top_n_countries=3)
plot_country_distribution_pie_chart(cricket_data)
plot_average_matches_by_country_bar_chart(cricket_data)
plot_matches_comparison_boxplot(cricket_data)
