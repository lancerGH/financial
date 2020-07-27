'''
1、检验CAPM理论是否能解释中国股票市场的投资组合。
作业提示：给定的置信水平alpha在（0,1）之间，一般取alpha=0.1,0.05,0.01.
如果不能拒绝alpha为零，且beta显著不为零，则CAPM适用于中国股票市场的资产组合定价。否则不适合。
2、中国明星基金的业绩具有持续性吗？基于CAPM的实证研究。
作业提示：基金收益可分为alpha收益和beta收益两部分。alpha收益体现基金经理的选股、择时能力。
3、利用CAPM对中国基金经理的投资能力进行实证研究，并给出基金的排名。
作业提示：和题2相同，可以分为alpha收益和beta收益两部分，利用alpha收益综合beta收益来排名。
'''
'''
第1题思路：
    先假设H0中国股票市场的投资组合符合CAPM理论，显著性水平alpha=0.05；
    收集某支基金的历史收益作为样本Y，把上证指数历史收益作为样本X
    用最小二乘法一元线性回归成 Y=alpha + beta * X +epsilon形式的r = rf + beta * （rm-rf），得出rf和beta值
    在CAMP理论中rf是无风险利率，现实中可能是1%之类；但是因为采取上证指数历史收益作为样本，此处的rf对应的其实是
上证指数历史收益的期望值，也就是说0，所以老师说越接近0越符合，越偏离0越不符合。
    用此处的rf值带入样本X中，把上证指数历史收益的均值0，方差用来计算z=（rf-mu）/(sigma/sqrt(n))，和显著性水平比较检验。
判断是否拒绝H0。
第2题思路：
    以某支基金的历史收益作为样本Y，把上证指数历史收益作为样本X；
    以最小二乘法的方式计算alpha收益和beta收益两部分；
第3题思路：
    按照alpha收益和beta收益的经济学解释，来对基金进行排名；
'''
import baostock as bs
import numpy as np
import pandas as pd

lg=bs.login()

portfolio_name="sh.601398"
s_date ="2010-01-01"
e_date = "2019-12-31"

#导入投资组合历史数据,对象portfolio
portfolio = bs.query_history_k_data_plus(portfolio_name,"date,pctChg",                        
    start_date= s_date, end_date= e_date, frequency="d", adjustflag="2")
#把投资组合历史数据清理成可用的DataFrame数据结构，对象portfolio_data
data_list=[]
while (portfolio.error_code == '0') & portfolio.next():
    data_list.append(portfolio.get_row_data())
portfolio_data=pd.DataFrame(data_list,columns=portfolio.fields)
#结果集输出到CSV文件
portfolio_data.to_csv("portfolio_history_data.csv",index=False)
bs.logout()