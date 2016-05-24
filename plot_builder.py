# -*- coding: utf-8 -*-

from pandas import Series
from os import listdir
from os.path import isfile, join
import io


word = u'ливия '
DIR = 'counts' #path
files = [f for f in listdir(DIR) if isfile(join(DIR, f))]

dateList = []
countList = []


for l in files:
	l = l[0:-4]
	dt = l.split("_")
	try:
		with io.open("counts/" + dt[0] + "_" + dt[1] + "_"+dt[2]+".txt", encoding='utf-8') as file:
			for line in file:
				if word in line:
					dateList.append(dt[0]+'-'+dt[1]+'-'+dt[2])
					countList.append(int(line.split(" ")[1][0:-1]))			
					break
	except:
		print("exept")


ts = Series(countList, dateList)
ts.plot(grid='on',kind='bar');