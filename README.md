#   SeriesBCRP
This repository contains a package to work with time series from BCRP for daily, monthly, quarterly and annually. The data is provided 
by API from BCRP, so in some cases we can find evidents outliers that need to be treated, specially in daily series. This outliers are commonly avoid in the data from web page of BCRP. 

A good example of this is "PD04649MD" code ("Posición de cambio"). If you look this series in webpage, the december 23 and 24, 2000, you can't find the data, but the API gives "24989.173" for both dates, that are outliers and need to be cleaned. Anyway, they are excepcional cases of daily series and it will be evident when you plot the time series. 

## Modules:
### 1. Data Module
#### 1.1. Import Data Module
You can import this module using "from seriesbcrp2 import data"
##### 1.2. Functions of Data Module
Data module contain the next functions:
A. bcrp function: This function call a data frame according the code of the serie and period of analysis.
Remember that quarterly codes finish with "Q" and monthly codes finish with "M". It's important to call the period in the correct way. 
See this examples to understand better:

-If you want the daily data of "Posición de cambio" serie from January 1, 2000 to December 31, 2020, you have to write data.bcrp("PD04649MD", "/2000-1-1/2019-12-31").

-If you want the PBI data serie from 2000 to 2021 by months, you have to use: "data.bcrp("PN01770AM", "/2000-1/2019-12"), where 
"PN01770AM" is the code for monthly serie of PBI and "/2000-1/2019-12" the choosen period.

-If you want the previous PBI series, but quarterly, you have to use: data.bcrp("PN39029BQ", "/2000-1/2019-3"), where "2000-1" means first quarter of 2000 and "2019-3" means third quarter of 2019. In this case, BCRP only offers data from 2018, so the result will be according this. 

- If you want the annual data of "Activos externos netos de corto plazo" from 2005 to 2020, you have to use data.bcrp("PM06069MA", "/2005/2019")

B. The "graph" function: This function allows to create a graph only with code and period inputs (similar to bcrp function).
You can choose the title and axis names according a required input.

C. The "boxplot" function: This function allows to create a boxplot only with code and period inputs (similar to bcrp function).
You can choose the title name according a required input.

D. The "histogram" function: This function allows to create a histogram only with code and period inputs (similar to bcrp function).
You can choose the title name according a required input.

E. The hep_code function: This function show you the link to codes of series of BCRP.
