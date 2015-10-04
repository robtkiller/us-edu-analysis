# us-edu-analysis
Python analysis of US public education spending. 


![Example Output](https://cloud.githubusercontent.com/assets/13774149/10270141/0d280094-6ab7-11e5-8a09-e0b03214a0cd.gif)

*Elementary and Secondary Ed Spending 2004-2013*

**Summary**

The above choropleth can be replicated using this repo.  The python script included utilizes [pandas](http://pandas.pydata.org/) to summarize Elementary and Secondary School financial data(see below) provided by the NCES and US Census Bureau.  School spending is aggregated by county/statistical area and presented in the output SVG file on a **$ per Student** basis.  Dark red areas indicate the lowest spending per student while dark green indicates areas of highest spending.

**Data Sources**


[Nation Center For Education Statistics - Common Core of Data](http://nces.ed.gov/ccd/f33agency.asp)

[US Census Bureau Public Elementary–Secondary Education Finance Data](http://www.census.gov/govs/school/)
