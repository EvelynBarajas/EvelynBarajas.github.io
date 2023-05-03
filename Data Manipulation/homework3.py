import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


smallpox = pd.read_csv('smallpox.csv', header=0)
print(smallpox)

smallpox.head()
smallpox.index
smallpox.columns

smallpox_base = smallpox[['Admin1ISO', 
    'PeriodStartDate', 'PeriodEndDate', 'CountValue']]
print(smallpox_base)

smallpox_base['Year'] = pd.to_datetime(smallpox_base.PeriodEndDate,
    format= '%Y-%m-%d')
smallpox_base.columns

smallpox_base['Year'] = smallpox_base['Year'].dt.strftime('%Y')
print(smallpox_base)

smallpox_base = smallpox_base[['Admin1ISO', 'CountValue', 'Year']]

smallpox_base.dtypes
#Year object to int
smallpox_base[['Year']] = smallpox_base[['Year']].apply(pd.to_numeric)

smallpox_base.isnull()

# 1. What year were smallpox infections the worst? To receive full credit
    #you must summarize the data, graph the data, and save the figure 
    #for submission with your homework.
    
    # 1930 was the year with the most smallpox infections
smallpox_years = smallpox_base.groupby('Year')['CountValue'].sum()
print(smallpox_years)

smallpox_years.plot.line(x="Year", y="CountValue")
plt.xlabel("Year")
plt.ylabel("Infections(count)")
plt.title("Smallpox Infection by Year")
plt.show()

#2.What states had the worst infections rates? To receive full credit
    #you must summarize the data, graph the data, and save the figure 
    #for submission with your homework.

    # 1. Indiana
    # 2. Ohio
    # 3. Iowa
    # 4. Washington
    # 5. California
smallpox_state = smallpox_base.groupby('Admin1ISO')['CountValue'].sum()
print(smallpox_state)

smallpox_state.plot.bar(x="Admin1ISO", y="CountValue")
plt.xlabel("State")
plt.ylabel("Infections (count)")
plt.title("Smallpox Infections by State")
plt.show()

#3. After vaccine introduction, did infection rates drop significantly? 
    #How many years after vaccine introduction before we can see a change
    #in infection rates?

    # The smallpox vaccine was introduced in the U.S in 1855. The data shows that
    # after the vaccine was a requirement, the number of cases were low, during the 1880s
    # and 1900. The number of cases began to rise around 1900, but were still relatively low.
    # After 1910 the number of cases began rising until reaching a peak in 1920 of about
    # 30,000 cases. After this year the infections began to drop once again before reaching a new
    # highest peak in 1930 of about 50,200 cases. The number of infections dropped again and have
    # continued to be low after 1940.

smallpox_years.plot.line(x="Year", y="CountValue")
plt.xlabel("Year")
plt.ylabel("Infections(count)")
plt.title("Smallpox Infection by Year")
plt.vlines(x=1855)
plt.show()
