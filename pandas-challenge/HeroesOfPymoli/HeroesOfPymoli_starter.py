
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[2]:


purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[3]:


total_players = len(purchase_data["SN"].unique())
tp = pd.DataFrame({"Total Players":[total_players]})
tp


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[4]:


# number of unique items
u_item = len(purchase_data["Item ID"].unique())

# average price
a_price = purchase_data["Price"].mean()

# number of purchases
n_purchases = len(purchase_data["Purchase ID"].unique())

# total revenue
total_revenue = purchase_data["Price"].sum()

# to print
pa = pd.DataFrame({"Number of Unique Items":[u_item],
                   "Average Price":[a_price],
                   "Number of Purchases":[n_purchases],
                   "Total Revenue":[total_revenue]                  
                  })
pa["Total Revenue"] = pa["Total Revenue"].map("${:.2f}".format)
pa["Average Price"] = pa["Average Price"].map("{:.2f}".format)
pa


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[5]:


# total of Male
male = purchase_data.loc[purchase_data["Gender"]=="Male", :]
male = len(male["SN"].unique())
# total of Female
female = purchase_data.loc[purchase_data["Gender"]=="Female", :]
female = len(female["SN"].unique())
# total of Other / Non-Disclosed
other = purchase_data.loc[purchase_data["Gender"]=="Other / Non-Disclosed", :]
other = len(other["SN"].unique())
# to print
gender = pd.DataFrame({"Total Count":[male, female, other],
                       "Percentage of Players":[male/total_players, female/total_players, other/total_players],
                  })
## set index
index = pd.Index(['Male','Female', 'Other / Non-Disclosed'])
gender = gender.set_index(index)
gender["Percentage of Players"] = gender["Percentage of Players"]*100
gender["Percentage of Players"] = gender["Percentage of Players"].map("{:.2f}%".format)
gender
# any better way to transfer to %


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[6]:


# groupby approach
group_gender = purchase_data.groupby(["Gender"])
# Purchase Count
p_id = group_gender["Purchase ID"].count()
# Average Purchase Price
ave_p = group_gender["Price"].mean()
# Total Purchase Value
total_p = group_gender["Price"].sum()
# Avg Total Purchase per Person
ave_p = total_p/gender["Total Count"]

# to print
purchasing_analysis = pd.DataFrame({"Purchase Count":p_id,
                                    "Average Purchase Price":ave_p,
                                    "Total Purchase Value":total_p,
                                    "Avg Total Purchase per Person":ave_p})
purchasing_analysis["Average Purchase Price"] = purchasing_analysis["Average Purchase Price"].map("${:.2f}".format)
purchasing_analysis["Total Purchase Value"] = purchasing_analysis["Total Purchase Value"].map("${:.2f}".format)
purchasing_analysis["Avg Total Purchase per Person"] = purchasing_analysis["Avg Total Purchase per Person"].map("${:.2f}".format)
purchasing_analysis


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[24]:


# Bins are 0, 10, 15, 20, 25, 30, 35, 40,100  
bins = [0, 9, 14, 19, 24, 29, 34, 39, 100 ]
# Create the names for the four bins
group_names = ["<10", "10-14", "15-19", "20-24", "25-29","30-34","35-39","40+"]
purchase_data["age_group"] = pd.cut(purchase_data["Age"], bins, labels=group_names, include_lowest=True)
# Creating a group based off of the bins
purchase_age_group = purchase_data.groupby("age_group")
# Total Count
total_count = purchase_age_group["SN"].nunique()
# Percentage of Players
percent_player = total_count/total_players*100
# to print
age_d = pd.DataFrame({"Total Count":total_count,
                      "Percentage of Players":percent_player})
age_d["Percentage of Players"] = age_d["Percentage of Players"].map("{:.2f}%".format)
age_d


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[26]:


# Purchase Count
purchase_count = purchase_age_group["Purchase ID"].count()
# Average Purchase Price
ave_p_age = purchase_age_group["Price"].mean()
#Total Purchase Value
total_p_age = purchase_age_group["Price"].sum()
#Avg Total Purchase per Person
ave_p_p_age = total_p_age/age_d["Total Count"]

# to print

purchasing_analysis_age = pd.DataFrame({"Purchase Count":purchase_count,
                                    "Average Purchase Price":ave_p_age,
                                    "Total Purchase Value":total_p_age,
                                    "Avg Total Purchase per Person":ave_p_p_age})
purchasing_analysis_age["Average Purchase Price"] = purchasing_analysis_age["Average Purchase Price"].map("${:.2f}".format)
purchasing_analysis_age["Total Purchase Value"] = purchasing_analysis_age["Total Purchase Value"].map("${:.2f}".format)
purchasing_analysis_age["Avg Total Purchase per Person"] = purchasing_analysis_age["Avg Total Purchase per Person"].map("${:.2f}".format)
purchasing_analysis_age


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[35]:


# group by SN purchase_data
spender = purchase_data.groupby(["SN"])
# Purchase Count
purchase_count = spender["Purchase ID"].count()
# Average Purchase Price
ave_p = spender["Price"].mean()
# Total Purchase Value
total_p = spender["Price"].sum()

# to print
purchasing_analysis_spender = pd.DataFrame({"Purchase Count":purchase_count,
                                    "Average Purchase Price":ave_p,
                                    "Total Purchase Value":total_p})
top_spender = purchasing_analysis_spender.sort_values("Total Purchase Value", ascending=False)
top_spender["Average Purchase Price"] = top_spender["Average Purchase Price"].map("${:.2f}".format)
top_spender["Total Purchase Value"] = top_spender["Total Purchase Value"].map("${:.2f}".format)

top_spender.head() 


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[47]:


# group by Item ID
pop_item = purchase_data.groupby(["Item ID","Item Name"])
# Purchase Count
p_count = pop_item["Purchase ID"].count()
# Item Price
price = pop_item["Price"].mean()
# Total Purchase Value
total_p = pop_item["Price"].sum()

#to print

item = pd.DataFrame({"Purchase Count":p_count,
                    "Item Price":price,
                     "Total Purchase Value":total_p})
pop_item_analysis = item.sort_values("Purchase Count", ascending=False)
pop_item_analysis["Item Price"] = pop_item_analysis["Item Price"].map("${:.2f}".format)
pop_item_analysis["Total Purchase Value"] = pop_item_analysis["Total Purchase Value"].map("${:.2f}".format)

pop_item_analysis.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[48]:


profit_item= item.sort_values("Total Purchase Value", ascending=False)
profit_item["Item Price"] = profit_item["Item Price"].map("${:.2f}".format)
profit_item["Total Purchase Value"] = profit_item["Total Purchase Value"].map("${:.2f}".format)

profit_item.head()

