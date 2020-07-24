'''
1、检验CAPM理论是否能解释中国股票市场的投资组合。
作业提示：给定的置信水平alpha在（0,1）之间，一般取alpha=0.1,0.05,0.01.
如果不能拒绝alpha为零，且beta显著不为零，则CAPM适用于中国股票市场的资产组合定价。否则不适合。
2、中国明星基金的业绩具有持续性吗？基于CAPM的实证研究。
作业提示：基金收益可分为alpha收益和beta收益两部分。alpha收益体现基金经理的选股、择时能力。
3、利用CAPM对中国基金经理的投资能力进行实证研究，并给出基金的排名。
作业提示：和题2相同，可以分为alpha收益和beta收益两部分，利用alpha收益综合beta收益来排名。
'''
import baostock as bs
import numpy as np
import pandas as pd