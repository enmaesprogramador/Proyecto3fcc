import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_clean_data():
    
    data = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"])
    
    
    data.set_index("date", inplace=True)
    
    
    lower_limit = data["value"].quantile(0.025)
    upper_limit = data["value"].quantile(0.975)
    cleaned_data = data[(data["value"] >= lower_limit) & (data["value"] <= upper_limit)]
    
    return cleaned_data


def draw_line_plot():
    data = load_and_clean_data()
    
    
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["value"], color="r", linewidth=1)
    
    
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    
    
    plt.savefig("line_plot.png")
    

def draw_bar_plot():
    data = load_and_clean_data()
    
    
    data["year"] = data.index.year
    data["month"] = data.index.strftime("%B")
    
    
    pivot_data = data.pivot_table(values="value", index="year", columns="month", aggfunc="mean", 
                                  order=["January", "February", "March", "April", "May", "June", "July", 
                                         "August", "September", "October", "November", "December"])
    
    plt.figure(figsize=(12, 6))
    ax = sns.heatmap(pivot_data, cmap="YlGnBu", annot=True, fmt="g")
    
    
    plt.title("Average Page Views per Year by Month")
    plt.xlabel("Years")
    plt.ylabel("Months")
    
    # Guardar la imagen
    fig = ax.get_figure()
    fig.savefig("bar_plot.png")
    

def draw_box_plot():
    data = load_and_clean_data()
    
    
    data["year"] = data.index.year
    data["month"] = data.index.strftime("%b")
    
   
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
  
    sns.boxplot(x="year", y="value", data=data, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    
    sns.boxplot(x="month", y="value", data=data, order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", 
                                                       "Aug", "Sep", "Oct", "Nov", "Dec"], ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    
    plt.tight_layout()
    plt.savefig("box_plot.png")
    

if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()