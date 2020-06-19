import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import sys

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['STZhongsong']    # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False           # 解决保存图像是负号'-'显示为方块的问题


excelFile1=r'PRO1\\s202005.xlsx'
df1=pd.DataFrame(pd.read_excel(excelFile1))
df1['时间差'] = pd.to_datetime(df1['解决时间'],format ='%Y%m%d', errors = 'coerce')-pd.to_datetime(df1['创建时间'],format ='%Y%m%d', errors = 'coerce')
print(df1['解决时间'])
excelFile2=r'PRO1\\w202005.xlsx'
df2=pd.DataFrame(pd.read_excel(excelFile2))
groupnum1 = df1.groupby(['解决日期']).size()
groupnum2 = df2.groupby(['解决日期']).size()
groupnum1.plot(x='解决日期',y='处理量',color='green',title='批量每月按处理人员统计',linewidth=3.0,linestyle='-')
groupnum2.plot(x='解决日期',y='处理量',color='red',title='批量每月按处理人员统计',linewidth=3.0,linestyle='-')

plt.show()

