import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates = ["date"],index_col = "date")

# Clean data
lower_q = df["value"].quantile(0.025)
upper_q = df["value"].quantile(0.975)

df = df[(df["value"] >= lower_q) & (df["value"] <= upper_q)]

def draw_line_plot():
    # Draw line plot
    title = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    fig,ax = plt.subplots(figsize =(15,5))
    ax.plot(df.index,df["value"],color= "red",linewidth = 1)
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df.index.year
    df_bar["month"] = df.index.month_name()
    

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    months = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[months]
    
    # Draw bar plot 
    ax = df_bar.plot(kind = "bar",figsize=(15,10))
    fig = ax.figure
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title= "Months", loc = "upper left")
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    title1 = "Year-wise Box Plot (Trend)"
    title2 =  "Month-wise Box Plot (Seasonality)"
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots (using Seaborn)
    fig,(ax1,ax2) = plt.subplots(1,2,figsize = (20,10))
    sns.boxplot(
    data = df_box,
    x = "year",
    y = "value", 
    ax = ax1)
    ax1.set_title(title1)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    
    sns.boxplot(
    data = df_box,
    x = "month",
    y = "value",
    order = month_order,
    ax = ax2,
    )
    ax2.set_title(title2)
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
    



