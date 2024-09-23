# https://www.kaggle.com/c/titanic/overview
# https://towardsdatascience.com/machine-learning-with-python-classification-complete-tutorial-d2c99dc524ec
# This program illustrates some data visualization and preliminary analysis you can do with pandas
# and the statsmodels package
# This code is from the kaggle website and the data science web site
# %%
import pandas as pd
import numpy as np  ## for plotting
import matplotlib.pyplot as plt
import seaborn as sns   ## for statistical tests
import statsmodels.formula.api as smf
# import statsmodels.api as sm  ## for machine learning

# %%
def utils_recognize_type(dtf, col, max_cat=20):
    '''
    Recognize whether a column is numerical or categorical.
    '''
    if (dtf[col].dtype == "O") | (dtf[col].nunique() < max_cat):
        return "cat"
    else:
        return "num"


# %%
# Begin main program
# set up the dataframe, dtf, that looks like a spreadsheet

dtf = pd.read_csv('myData/titanic.csv')

dtf = dtf.set_index("Passengerid")
dtf = dtf.rename(columns={"survived":"Y"})

# %%
# Display a heat map that shows the data type of each column
# and white cells for the missing data

dic_cols = {col:utils_recognize_type(dtf, col, max_cat=20) for col in dtf.columns}
heatmap = dtf.isnull()
for k,v in dic_cols.items():
 if v == "num":
   heatmap[k] = heatmap[k].apply(lambda x: 0.5 if x is False else 1)
 else:
   heatmap[k] = heatmap[k].apply(lambda x: 0 if x is False else 1)
   
sns.heatmap(heatmap, cbar=False).set_title('Dataset Overview')
plt.show()
print("\033[1;37;40m Categorical ", "\033[1;30;41m Numeric ", "\033[1;30;47m NaN ")

x = "age"
y = "Y"

# %%
# Display a bar chart for the number of passengers who survived/died

ax = dtf[y].value_counts().sort_values().plot(kind="barh")
totals= []
for i in ax.patches:
    totals.append(i.get_width())
total = sum(totals)
for i in ax.patches:
     ax.text(i.get_width()+.3, i.get_y()+.20,
     str(round((i.get_width()/total)*100, 2))+'%', fontsize=10, color='black')
ax.grid(axis="x")
plt.suptitle("Survived?", fontsize=20)
plt.show()

# %%
# Display a histogram of age

fig, ax = plt.subplots(nrows=1, ncols=2,  sharex='none', sharey='none')
fig.suptitle("Age", fontsize=20)

### distribution
ax[0].title.set_text('Distribution')
variable = dtf[x].fillna(dtf[x].mean())
breaks = np.quantile(variable, q=np.linspace(0, 1, 11))
variable = variable[ (variable > breaks[0]) & (variable <
                    breaks[10]) ]
sns.histplot(variable, kde=True, stat="density", linewidth=0 , ax=ax[0])
des = dtf[x].describe()
ax[0].axvline(des["25%"], ls='--')
ax[0].axvline(des["mean"], ls='--')
ax[0].axvline(des["75%"], ls='--')
ax[0].grid(True)
des = round(des, 2).apply(lambda x: str(x))
box = '\n'.join(("min: "+des["min"], "25%: "+des["25%"], "mean: "+des["mean"], "75%: "+des["75%"], "max: "+des["max"]))
ax[0].text(0.95, 0.95, box, transform=ax[0].transAxes, fontsize=10, va='top', ha="right", bbox=dict(boxstyle='round', facecolor='white', alpha=1))

### boxplot
ax[1].title.set_text('Outliers (log scale)')
tmp_dtf = pd.DataFrame(dtf[x])
tmp_dtf[x] = np.log(tmp_dtf[x])
tmp_dtf.boxplot(column=x, ax=ax[1])
plt.show()


# %%
