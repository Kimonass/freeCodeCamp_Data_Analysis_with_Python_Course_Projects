import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import the data from medical_examination.csv  file
df = pd.read_csv("/workspace/boilerplate-medical-data-visualizer/medical_examination.csv")

#Create the overweight column
df['overweight'] = (df["weight"]/(df["height"]/100)**2).apply(lambda x:1 if x>25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df["cholesterol"]=(df["cholesterol"]).apply(lambda x:1 if x>1 else 0)
df["gluc"]=(df["gluc"]).apply(lambda x:1 if x>1 else 0)


def draw_cat_plot():

    """Convert the data into long format and create a chart that 
    shows the value counts of the categorical features using seaborn's catplot(). 
    The dataset will be split by Cardio so there is one chart for each cardio value."""

    df_cat = pd.melt(df,id_vars=["cardio"],value_vars=["active","alco","cholesterol","gluc","overweight","smoke"])

    #Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature.
    df_cat = pd.DataFrame(df_cat.groupby(["cardio","variable","value"])["value"].count()).rename(columns={"value":"total"})
    
    #create a chart that shows the value counts of the categorical features
    fig = sns.catplot(x="variable", y='total', hue='value',col='cardio', data=df_cat, kind='bar')
    fig.set_axis_labels('variable', 'total')


    fig.savefig('catplot.png')
    return fig


#Draw the Correlation Heat Map
def draw_heat_map():
    
    # Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data
    df_heat = df.copy()
    df_heat=df_heat[df_heat["ap_lo"]<=df_heat["ap_hi"]]
    df_heat=df_heat[df_heat["height"]>=df_heat["height"].quantile(0.025)]
    df_heat=df_heat[df_heat["height"]<=df_heat["height"].quantile(0.975)]
    df_heat=df_heat[df_heat["weight"]>=df_heat["weight"].quantile(0.025)]
    df_heat=df_heat[df_heat["weight"]<=df_heat["weight"].quantile(0.975)]


    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the  figure
    fig, ax = plt.subplots(figsize=(20, 10))

    # Plot the correlation matrix heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=0.1, square=True, cbar_kws={"shrink": .5})


    # Save the heatmap as png
    fig.savefig('heatmap.png')
    return fig
