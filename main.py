import streamlit as st 
import pandas as pd

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('data/world.sqlite')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/styles.css")


def main():
	st.title("SQLTester :nerd_face:")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("HomePage")
		st.write("Create a sample production table with random sample values and practice SQL queries here before going to the production cloud servers")
		# Columns/Layout
		col1,col2 = st.columns(2)

		with col1:
			with st.form(key='query_form'):
				raw_code = st.text_area("SQL Code Here")
				submit_code = st.form_submit_button("Execute")

			# Table of Info

			with st.expander("Table Info", expanded=True):
				table_info = {'city':city,'country':country,'countrylanguage':countrylanguage}
				st.json(table_info)
			
		# Results Layouts
		with col2:
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)
				with st.expander("Results in Table", expanded=True):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)
				with st.expander("Results in Json"):
					st.write(query_results)


	else:
		st.subheader("About")
		st.write("Most of our databases are now in the cloud servers and each user liscense or registration costs subscription money, each code executed also costs money, hence it is becoming harder for the beginers to get used to and learn the data and play around with the databases. Hence I have created this SQL tester app, where the users can define databases with sample data and execute SQL queries and get familiar with data and SQL, thus well prepared when getting to the production and cloud servers and not waste any resources")

if __name__ == '__main__':
	main()