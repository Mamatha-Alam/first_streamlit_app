import streamlit

streamlit.title("My Mom's new healthy diner")

streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 and Blueberry OatMeal')
streamlit.text('Kale, Spinach and Rocket smoothie')
streamlit.text('Hard Boiled Free range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
                
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
