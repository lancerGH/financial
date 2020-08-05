import baostock as bs
import numpy as np
import pandas as pd
import statsmodels.api as sm


funds_name=["华安安顺(519909.OF).csv","华安宝利配置(040004.OF).csv","华安大国新经济(000549.OF).csv","华安大中华升级(040021.OF).csv",
"华安宏利(040005.OF).csv","华安生态优先(000294.OF).csv","华安物联网主题(001028.OF).csv"]

m=pd.read_csv("market_history_data.csv",usecols=[0,1])
m["date"]=pd.to_datetime(m["date"])       #市场数据

funds_market=[]                             #基金数据
for f in funds_name:
    y=pd.read_csv(f,usecols=[0,5])        #读取基金数据，返回dataframe类型
    y["日期"]=pd.to_datetime(y["日期"])    #转换日期列为datetime类型
    y.sort_values(by=["日期"],ascending=False)

    z=pd.merge(y,m,how="inner",left_on=["日期"],right_on=["date"]) #inner join
    funds_market.append(z)

for i in funds_market:
    y=pd.DataFrame(i["涨跌幅(%)"])
    #print(y)
    x_model=sm.add_constant(i["pctChg"])
    #print(type(x_model))
    model=sm.OLS(y,x_model)
    results = model.fit()
    print(results.summary())