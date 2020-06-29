import pandas as pd
my_dataset = pd.read_csv('survey_results_public.csv', index_col='Respondent') 
#read the .csv file from the same folder and assigns the 'Respondent' column as the index
print(my_dataset)
print(my_dataset.shape)
my_dataset
my_dataset.shape # shows the column and row size in the form a tuple'''
my_dataset.info() # yields info about the dataset: data, column, data type'''
pd.set_option('display.max_columns', 85)
#shows all 85 rows in the data'''
pd.set_option('display.max_row', 85)  
#shows all 85 rows in the data'''
my_dataset_schema = pd.read_csv('survey_results_schema.csv')
my_dataset
my_dataset_schema.columns
my_dataset.head(10)
# shows 10 first rows of data.() shows the first 5 rows
my_dataset.tail(10)
# shows 10 last rows of data. () shows the last 5 rows
my_dataset_schema.set_index('Column', inplace=True)# Sets 'Column' as the index
my_dataset_schema.loc['MgrIdiot'] # gets the info about 'MgrIdiot' col.
my_dataset_schema.loc['MgrIdiot', 'QuestionText'] # gets the info about 'MgrIdiot' row and 'QuestionText' column.
my_dataset_schema.sort_index() #sorts the index column alphabetically
my_dataset_schema.sort_index(inplace=True) #sorts the index column alphabetically PERMANENTLY.
my_dataset_schema.sort_index(ascending=False) # sorts the index column alphabetically in descending order
ostadio = pd.read_csv('ostadio_march_30_2020.csv')
ostadio
ostadio.info()
ostadio.head()
my_dataset.shape
ostadio.shape
my_dataset.columns
my_dataset.iloc[[],2]
my_dataset['Hobbyist']
ostadio.columns
ostadio['Users']
my_dataset['Hobbyist'].value_counts()
#now we want to only see the data for the 'Country' column that equals the following 5 countries. This is a neat solution:
countries = ['United States', 'Canada', 'India', 'Germany', 'United Kingdom'] #creates a list of these countries
filt = my_dataset['Country'].isin(countries) #creates a filter to separate the ones from countries
my_dataset.loc[filt, 'Country'] #filters out and shows only the Country column for the filtered data.
#next, we want to find the ones who has Python under the 'LanguageWorkedWith' column.
filt = my_dataset['LanguageWorkedWith'].str.contains('Python', na=False)
my_dataset.loc[filt] #shows data rows that has Python under 'LanguagWorkedWith'.
my_dataset.loc[filt, 'Country'] #from the filtered data, only shows their 'Country' column data.
my_dataset.rename(columns = {'ConvertedComp':'Salary'}, inplace=True)#changes the column name and make it permanent with inplace=true
my_dataset['Salary']
my_dataset.columns
my_dataset['Hobbyist']
my_dataset['Hobbyist'].map({ 'Yes' : True, 'No' : False})#changes yes & no string values to boolean variable
my_dataset['Hobbyist'] = my_dataset['Hobbyist'].map({ 'Yes' : True, 'No' : False})
my_dataset.sort_values(by='Country', inplace=True)#sorts the dataframe based on 'Country' column.
my_dataset['Country'].head(50)
my_dataset[['Country', 'Salary']].head(50) #shows 'Country' and 'Salary' columns for the first 50 rows.
my_dataset.sort_values(by=['Country', 'Salary'], ascending= [True, False]) #sorts based on 'Country' in ascending and then 'Salary' in descending order.
my_dataset['Salary'].nlargest(10) #shows the 10 largest values for 'Salary'.
my_dataset.nlargest(10, 'Salary') #shows all columns data for the 10 rows with largest values in 'Salary'.
my_dataset['Salary'].nsmallest(10) #shows the 10 smallest values for 'Salary'.
my_dataset.nsmallest(10, 'Salary') # shows all columns data for the 10 rows with smallest values in 'Salary'.
my_dataset['Salary'].median() #shows median value for the 'Salary' column
my_dataset['Salary'].mean() #shows mean value for the 'Salary' column
my_dataset.median() # goes through the whole dataframe and shows median for numerical columns.
my_dataset.describe() #shows descriptive stats for quantitative columns
my_dataset['Salary'].describe() #descriptive stats for Salary column.
my_dataset['Salary'].count() #returns the number of non-null values in a series.
my_dataset['Hobbyist'].value_counts() # shows the frequency of different values in the series.
my_dataset['SocialMedia'].value_counts() #shows the frequency of different values under the 'SocialMedia' column/series.
my_dataset['SocialMedia'].value_counts(normalize=True) #shows the normalized version of frequency of values under 'SocialMedia' column/series.
##GROUPBY operation involves some combination up of SPLITTING the object, APPLYING the function, and COMBINING the result. 
my_dataset['Country'].value_counts()
my_dataset.groupby(['Country']) #groups the rows by 'Country'.
country_grp = my_dataset.groupby(['Country']) # create a variable to keep and use the grouping later.
country_grp.get_group('United States') # gives a dataframe that only has the 'Country' column set as 'United States'.
#Now doing the same thing using filter: shows data rows with 'United States' under 'Country' column.
filt = my_dataset['Country'] == 'United States'
my_dataset.loc[filt]
my_dataset.loc[filt]['SocialMedia'].value_counts() #shows value frequency under 'SocialMedia' column, based on the defined filter (countr=United States)
country_grp['SocialMedia'].value_counts() #gives a series that shows frequency of 'SocialMedia' values broken down by 'Country' (because of the grouping that was defined earlier)
country_grp['SocialMedia'].value_counts().head(50) #shows top 50 of the above command.
country_grp['SocialMedia'].value_counts().loc['India'] #shows the outcome for only 'India'. So using this grouping, now we can see the outcome for each 'country' without needing to create a new filter each time.
country_grp['SocialMedia'].value_counts(normalize=True).loc['India'] #normalized form of above command.
country_grp['Salary'].median() #applies median function to country group, so shows median values for each country in the form of a dataframe, in which country names are index.
country_grp['Salary'].median().loc['Germany'] # since in above output country names are the indexes, we can use country names to address acertain row, for example 'Germany'.
#Now use agg method to apply multiple functions to the group at the same time.
country_grp['Salary'].agg(['median', 'mean']) #shows both the median and mean for our country-based grouping.
country_grp['Salary'].agg(['median', 'mean']).loc['Canada'] #shows the above for just Canada.
#filter
filt = my_dataset['Country'] == 'India'
my_dataset.loc[filt]
my_dataset.loc[filt]['LanguageWorkedWith'].str.contains('Python') #after the filter('Country' equals 'India'), checks if 'Pyhton' is under 'LanguageWorkedWith' for each respondent and assigns a boolean value to each respondent based on that.
my_dataset.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum() #does the above, and sums the booleans (True=1 & False=0)
country_grp['LanguageWorkedWith'].str.contains('Python').sum() #.str cannot be applied to byGroupSeries ERROR. Instead we do the following:
country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())#ruuning the apply method on this series bygroup, then we're passing on a function that is going to run on each one of these series.
#now try to calculate the percentage of respondents that worked with python over all respondents for each country.
country_respondents = my_dataset['Country'].value_counts()     
country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
python_my_dataset = pd.concat([country_respondents, country_uses_python], axis = 'columns', sort = False) #concatanates(attaches) two series together and matches up on the index.
python_my_dataset
python_my_dataset.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True) #rename the columns to names more relatable to what the values are in those columns.
python_my_dataset['PctKnowsPython'] = (python_my_dataset['NumKnowsPython']/python_my_dataset['NumRespondents'])*100 #adds a new column that calculates the percentage of repondents from each country who have worked with Python.
python_my_dataset['PctKnowsPython']
python_my_dataset.sort_values(by= 'PctKnowsPython', ascending = False) #sorts the 'PctKnowsPython'series in descending manner
python_my_dataset.sort_values(by= 'PctKnowsPython', ascending = False, inplace=True) #makes PERMANENT
python_my_dataset.loc['Japan'] #search for info about Japan in the new dataframe(python_my_dataset). Country names are indexes in this dataframe.
##Cleaning data
import pandas as pd
import numpy as np
na_vals = ['NA', 'Missing']
my_dataset = pd.read_csv('survey_results_public.csv', index_col='Respondent', na_values = na_vals) 
#when reading the csv file, above command will make python treat the list of values as missing values with NaN value.
#now let's calculate the average years of experience ('YearsCode' column) with coding for this data.
my_dataset['YearsCode'].mean() #gives an error since data type is string, and not integer.
#so we should convert this to a float since there are NaN values. 
my_dataset['YearsCode'] = my_dataset['YearsCode'].astype(float) #this also produced an error (could not convert string to float: 'Less than 1 Year)
#so there are other values than numbers and NaN in this column. first let's check the unique values of the series in this column to see what we are facing.
my_dataset["YearsCode"].unique() #gives all the unique values in this column. It is seen that 
# there are values such as "Less than 1 year", "More than 50 years". So we need to replace them first.
my_dataset["YearsCode"].replace('Less than 1 year', 0, inplace=True) #replace 'Less than 1 year' with 0.
my_dataset["YearsCode"].replace('More than 50 years', 51, inplace=True) #replace 'More than 50 year' with 51.
my_dataset['YearsCode'] = my_dataset['YearsCode'].astype(float) #now convert to float should work fine and we can run arithmetic functions on it afterwards.
my_dataset['YearsCode'].mean() 
my_dataset['YearsCode'].median()

