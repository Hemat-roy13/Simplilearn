import pandas as pd

"""
DataFame as Lists
"""
lst_host = ['delhi','delhi','delhi','delhi','delhi']
lst_year = [2012,2013,2014,2015,2016]
lst_no_part = [198,199,200,201,202]
pandas_df = pd.DataFrame('Host': lst_host,'Year': lst_year, 'Part':lst_no_part)
print (pandas_df)

"""
DataFrame as Dict
"""

