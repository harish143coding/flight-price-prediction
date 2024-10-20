# importin the required python frameworks
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# importing the data
df = pd.read_excel("Data_Train.xlsx")
print("Initial few rows of the dataset: \n", df.head())

#getting the view of total nr of rows and columns in the dataset
print("\nTotal nr of rows and columns in the dataset: \n", df.shape)

# getting the overview of the features and their types
print("\nOverview of the features and types in the dataset:", df.info())

# getting the overview of the dataset 
print("\n Overview of the dataset: \n", df.describe())

#getting the overview of the data including the object 
print("\n overview of the dataset: \n", df.describe(include='object').T)


df.isnull().sum()

# To find the unique values
for i in df.columns:
     print(f"The unique values in feature {i} is", df[i].unique(), sep='\n')

# creating a central Function for processing and modelling the data
def preprocess(data):

     df.dropna(inplace=True)
     df.drop_duplicates(inplace=True)
     df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'])
     df['day'] = pd.DatetimeIndex(df['Date_of_Journey']).day
     df['month'] = pd.DatetimeIndex(df['Date_of_Journey']).month
     df['weekday'] = pd.DatetimeIndex(df['Date_of_Journey']).weekday

     df['Total_Stops'] = df['Total_Stops'].replace('non-stop', '0')
     df['Total_Stops'] = df['Total_Stops'].replace('1 stop', '1')
     df['Total_Stops'] = df['Total_Stops'].replace('2 stops', '2')
     df['Total_Stops'] = df['Total_Stops'].replace('3 stops', '3')
     df['Total_Stops'] = df['Total_Stops'].replace('4 stops', '4')

     df['Destination'] = np.where(df['Destination'] == 'New Delhi', 'Delhi', df['Destination'])
     df['Airline'] = np.where(df['Airline'] == 'Jet Airways Business', 'Jet Airways', df['Airline'])
     df['Airline'] = np.where(df['Airline'] == 'Vistara Premium Economy', 'Vistara', df['Airline'])
     df['Airline'] = np.where(df['Airline'] == 'Multiple carriers Premium economy', 'Multiple Carriers', df['Airline'])

     arrival_time = []
     for i in data["Arrival_Time"]:
         arrival_time.append(i[:5])
     df['Arrival_Time'] = arrival_time
     df['Arrival_Time_hour'] = pd.to_datetime(df['Arrival_Time']).dt.hour
     df['Arrival_Time_minute'] = pd.to_datetime(df['Arrival_Time']).dt.minute
     df['Duration_Total_Hour'] = df['Duration'].str.replace('h', '*1')\
     .str.replace('m', '*60')\
     .str.replace(' ', '+')\
     .apply(eval)
     data1 = pd.get_dummies(data, 
            prefix= ['Airline', 'Source', 'Destination'],
            columns= ['Airline', 'Source', 'Destination'],
            drop_first= True
            )
     data1.drop(['Date_of_Journey', 'Arrival_Time', 'Dep_Time',                                  'Duration','Additional_Info', 'Route'], 
                axis= 1, 
                inplace = True)
     return data, data1

     
### Get The EDA & Model Data
data_eda, data_model = preprocess(df)

#print(data_eda)

print(data_model)
# Univariate Exploratory Data Anaysis
sns.displot(pd.DataFrame(data_eda['Price']), kind='hist')
plt.title('Distribution of Flight Prices')
plt.xlabel('Price')
plt.ylabel('Density')
#plt.show()
     
# create historam to visuaize the distribution of flight prices
plt.figure(figsize=(8, 5))
sns.histplot(pd.DataFrame(data_eda['Price']), kde=True, bins=30)
plt.title("Flight Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
#plt.show()


         
         
     