import pandas as pd

"""
create a dataframe with rating of movies by person one and two i.e movie1 and movie2 as columns.
The columns should have rating for movies. the Dataframe should have index like movie name
"""

list_movie1 = [5,5,4,4,3]
list_movie2 = [5,4,5,4,1]
movie_name = ['KANKN','ZNMGD','BMB','Gandhi','Uri']

df = pd.dataframe("movie_1":list_movie1,"movie_2":list_movie2,index=movie_name)

"""
Changes the movie rating from star to category
"""

def movie_grade(rating):
  if rating == 5:
    return 'A'
  elif rating == 4:
    return 'B'
  elif rating == 3:
    return 'C'
  elif rating == 2:
    return 'D'
  else rating == 1:
    return 'E'
  
df.applymap(movie_grade)

"""
Data operation with stats. In this situation we have test result of student of class for test1 and test2. we need find average student name, 
max marks for each test and min marks for each test.
"""

test_1 = [27,28,29,30,21]
test_2 = [28,29,26,21,29]
names = ['amit','sachin','archit','shreya','ayushi']

result = pd.DataFrame("test_1":test_1,"test_2":test_2,index=names)

result.max()
result.min()
result.mean()

"""
we neeed to create a dataframe and then Group by last name. we need to create two columns first name and last name. Then we need to group by last name. 
"""

first_name_list = ['archit','shreya','ayushi','amit','smita']
last_name_list = ['Rai','sharma','Rai','rastogi','kumari']

df = pd.DataFrame("first_name_list":first_name_list,"first_name_list":last_name_list)

df_groupby = df.groupBy('last_name')
df_get_rai = df_groupBy.get_group('Rai')

"""
Sorting by firstname
"""

first_name_list = ['archit','shreya','ayushi','amit','smita']
last_name_list = ['Rai','sharma','Rai','rastogi','kumari']

df = pd.DataFrame("first_name_list":first_name_list,"first_name_list":last_name_list)

df.sort_values('first_name_list')

  
  
  
  
  
  
