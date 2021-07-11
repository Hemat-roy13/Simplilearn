import pandas as pd

"""
Adding two dataframe with uncommon indices
"""

list_a = [1,2,3,4,5,6,7,8,9]
key_list_a = ['a','b','c','d','e','f','g','h','i']

first_element = pd.Series(list_a,index=key_list_a)

list_b = [1,2,3,4,5,66,7,6]
key_list_a = ['a','b','c','d','q','w','r','e']

second_element = pd.Series(list_b,index=key_list_b)

missing_values=first_element + second_element

"""
handle one drop NaN values
"""

missing_values_with_drop=missing_values.dropna()

"""
fill with zero
"""

missing_avlues_with_zero=missing_values.fillna(0)

"""
before adding fill with zero
"""
no_missing_data=first_element.add(second_element,fill_value=0)
