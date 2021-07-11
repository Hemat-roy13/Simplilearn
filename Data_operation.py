import pandas as pd

"""
create a dataframe with rating of movies by person one and two i.e movie1 and movie2 as columns.The columns should have rating for movies. the Dataframe should have index like movie name
"""

list_movie1 = [5,5,4,4,3]
list_movie2 = [5,4,5,4,1]
movie_name = ['KANKN','ZNMGD','BMB','Gandhi','Uri']

df = pd.dataframe("movie_1":list_movie1,"movie_2":list_movie2,index=movie_name)
