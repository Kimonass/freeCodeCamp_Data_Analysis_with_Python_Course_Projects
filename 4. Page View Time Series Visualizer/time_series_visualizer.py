import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Import data 
df = pd.read_csv('/workspace/boilerplate-page-view-time-series-visualizer/fcc-forum-pageviews.csv/content/fcc-forum-pageviews.csv',index_col='date', parse_dates=True)

# Clean data
df=df[df['value']>=df['value'].quantile(0.025)]
df=df[df['value']<=df['value'].quantile(0.975)]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    df.plot(ax=ax, color=['red'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.legend().set_visible(False)


    # Save image and return fig 
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df.index.year
    df_bar['Months'] = df.index.month
    df_bar = df_bar.groupby(['Year','Months']).mean().reset_index()
    df_bar=df_bar.pivot(index='Year', columns='Months', values='Average Page Views')
    df_bar.columns=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    ax = df_bar.plot(kind='bar', figsize=(8, 6))
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Save image and return fig 
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots 
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots 
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Year-wise Box Plot (Trend)
    sns.boxplot(x="Year", y='Page Views', data=df_box, ax=axes[0], hue='Year')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].legend_.remove() 
    
    # Month-wise Box Plot (Seasonality)
    sns.boxplot(x="Month", y='Page Views', data=df_box, ax=axes[1], hue='Month',order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    

    # Save image and return fig 
    fig.savefig('box_plot.png')
    return fig
