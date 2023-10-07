import streamlit as st
import pandas as pd
from pydataset import data

st.set_page_config(layout="wide")

st.title("Pandas Group By")
st.markdown(
    f""" I know that many of you are familiar with how to aggregate data in pandas.
    But I just want to show my favorite way to do it. I think it is very intuitive and
    easy to understand. I hope you like it. """)

st.markdown(f'## Required Packages')
st.code(f"""
        import pandas as pd
        from pydataset import data""", language='python')

st.markdown(f'## Load and show the iris dataset as an example')
load_data_command = f"""iris = data('iris')"""
st.code(load_data_command, language='python')
print_data_command = f"""iris.head()"""
st.code(print_data_command, language='python')
iris = data('iris')
st.dataframe(iris.head())

st.markdown(f'## Group by species and calculate the mean and other statistics')
st.markdown("This is the style I like the most. It is very intuitive and easy to understand.")
st.markdown("In the future I will add more examples what else you can do with group by using this style.")

aggreate_command = f"""
group_by_result = iris.groupby(['Species']).agg(
    count = ('Sepal.Length', 'count'),
    sepal_length_mean=('Sepal.Length', 'mean'),
    sepal_width_median=('Sepal.Width', 'median')
).reset_index()

group_by_result
"""
st.code(aggreate_command, language='python')

group_by_result = iris.groupby(['Species']).agg(
    count = ('Sepal.Length', 'count'),
    sepal_length_mean=('Sepal.Length', 'mean'),
    sepal_length_median=('Sepal.Length', 'median'),
    petal_length_mean=('Petal.Length', 'mean'),
    petal_length_median=('Petal.Length', 'median')
).reset_index()

st.dataframe(group_by_result)

st.markdown(f""" I like to use this style because it is very intuitive and easy to understand and I can instantly create the variable names I want.""")




