import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

'''For 2004-2012 Data'''
df = pd.read_csv('data/edu/SDF091a.txt',sep='\t',dtype={'CONUM':object})
df = df.groupby(by=['CONUM'])[['TCURELSC','V33']].sum()
df = pd.DataFrame(df['TCURELSC'].div(df.V33, axis='index'))

'''For 2013 Data'''
#df = df.groupby(by=['CONUM'])[['TCURSPND','ENROLL']].sum()
#df['TCURSPND']= df['TCURSPND']*1000
#df = pd.DataFrame(df['TCURSPND'].div(df.ENROLL, axis='index'))

'''Output DataFrame to List of Tuples'''
data = list(df.itertuples(index=True))

'''Create Dictionary of FIPS and Data'''
spend = {}
for row in data:
	try:
		fips = row[0]
		rate = float(row[1])
		spend[fips]=rate
	except:
		pass

'''Open base map and rebuild with shading'''
svg = open('svg/map.svg', 'r').read()

soup = BeautifulSoup(svg ,'xml', selfClosingTags=['defs','sodipodi:namedview'])
paths = soup.findAll('path')
colors = ["#245B00", "#7FB35D", "#ECE0A7", "#CBBA69", "#ECB7A7", "#892E14"]

path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'

for p in paths:
	if p['id'] not in ["State_Lines","separator"]:
		try:
			rate = spend[p['id']]
		except:
			continue

		if rate > 30000:
			color_class = 0
		elif rate > 17000:
			color_class = 1
		elif rate > 14000:
			color_class = 2
		elif rate > 11000:
			color_class = 3
		elif rate > 8000:
			color_class = 4
		else:
			color_class = 5
	
		color = colors[color_class]
		p['style'] = path_style + color

'''Output SVG data'''
print(soup.prettify())

