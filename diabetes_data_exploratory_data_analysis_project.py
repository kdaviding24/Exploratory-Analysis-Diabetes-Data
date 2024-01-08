import pandas as pd
import numpy as np

data = pd.read_csv('diabetes.csv')

print(data.info())
# printed the info of the dataframe
# file contains 768 observations
#9 columns
#All columns are returning 768 non_null values
#print(data.Outcome.unique())
#printed the unique entries of the Outcome column to understand why it was an object datatype.
# it is an array of strings that inclue numbers 1 and 0 followed by the letter "O". This could be a mistake. If so will need to drop observation.
# According to the data dictionary all values in this column should be binary number values (1 or 0).
#print(data.describe())
#After printing the descripton of the data, it can be seen that some of the features have have 0 listed as some of there values.
#There are also some strange maxes in the glucose(846.0) and pregnancy(17.0) columns
data[['Glucose', 'BloodPressure', 'Insulin', 'SkinThickness', 'BMI']] = data[['Glucose', 'BloodPressure', 'Insulin', 'SkinThickness', 'BMI']].replace(0, np.nan)
#replacing all values of 0 with NaN
print(data.dtypes)
data.Outcome = data.Outcome.replace('O', 0)
data.Outcome = data.Outcome.astype('int')
#replaced all occurences of the letter 'O' with the number 0 and changed the data type for the column as well
print(data.dtypes)

print(data[data.columns].value_counts())

null_list = ['Glucose', 'BloodPressure', 'Insulin', 'SkinThickness', 'BMI']

for column in null_list:
  data[column].fillna(data[column].median(), inplace = True)
# updated null values with the medians for each column based on hight standard deviation
