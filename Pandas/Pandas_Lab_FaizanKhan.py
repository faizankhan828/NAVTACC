#SECTION 1 — Creating DataFrames & Series | Reading Files

#Q01 Build a Mini DataFrame from Scratch
'''
Task:
• Create a pd.Series of 5 survival statuses [1, 0, 1, 1, 0] with passenger name labels: Alice, Bob,
Charlie, Diana, Edward.
• Create a DataFrame with columns: PassengerId [1–5], Survived [1,0,1,1,0], Pclass [1,3,1,2,3], Fare
[71.28, 7.25, 51.86, 13.00, 8.05].
• Print both objects. Check the dtype of the Series.
'''
import pandas as pd
from pathlib import Path
survival_status = pd.Series([1, 0, 1, 1, 0], index=['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'])
df = pd.DataFrame({
    'PassengerId': [1, 2, 3, 4, 5],
    'Survived': [1, 0, 1, 1, 0],
    'Pclass': [1, 3, 1, 2, 3],
    'Fare': [71.28, 7.25, 51.86, 13.00, 8.05]
})
print("Survival Status Series:")
print(survival_status)
print("\nDataFrame:")
print(df)

print(f"\nDtype of survival_status: {survival_status.dtype}")

#Q02 Load the Titanic CSV File

'''
Task:
• Load titanic.csv into a DataFrame called df.
• Print the first 5 rows using .head().
• Print the last 3 rows using .tail(3).
• Check its shape (rows, columns).
'''
csv_path = Path(__file__).parent / 'data' / 'Titanic.csv'
df = pd.read_csv(csv_path)
print("First 5 rows:")
print(df.head())
print("\nLast 3 rows:")
print(df.tail(3))
print(f"\nShape of the DataFrame: {df.shape}")


#SECTION 2 — Viewing & Inspecting Data | Selecting & Indexing
#Q03 Inspect & Explore the Dataset
'''
Task:
• Display column names and their data types.
• Show summary statistics for all numeric columns (count, mean, std, min, max).
• Count the total number of missing values per column.
• How many passengers are in each Pclass? Use value_counts().
'''
print("Column names and data types:")
print(df.dtypes)
print("\nSummary statistics for numeric columns:")
print(df.describe())
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nNumber of passengers in each Pclass:")
print(df['Pclass'].value_counts())



#Q04 Select & Index Specific Data

'''
Task:
• Select only the Age and Fare columns and show the first 5 rows.
• Using .iloc[], select rows 10 to 14 (inclusive) and the first 3 columns.
• Using .loc[], select all rows where Survived == 1 and display PassengerId, Pclass, Fare.
• Find the fare paid by the passenger with PassengerId = 7 using a single expression.
'''
print("Age and Fare columns (first 5 rows):")
print(df[['Age', 'Fare']].head())
print("\nRows 10 to 14 (inclusive) and first 3 columns:")
print(df.iloc[10:15, :3])
print("\nPassengers who survived (PassengerId, Pclass, Fare):")
print(df.loc[df['Survived'] == 1, ['PassengerId', 'Pclass', 'Fare']])
print("\nFare paid by passenger with PassengerId = 7:")
fare_passenger_7 = df.loc[df['PassengerId'] == 7, 'Fare']
if not fare_passenger_7.empty:
    print(fare_passenger_7.iloc[0])
else:
    print("PassengerId 7 not found in this dataset.")



#SECTION 3 — Adding, Modifying & Deleting Columns | Handling Missing Data

#Q05 Engineer New Features

'''
Task:
• Add a new column FamilySize = SibSp + Parch + 1 (the +1 is for the passenger themselves).
• Add a boolean column IsAlone that is True when FamilySize == 1, else False.
• Add a column FareCategory: 'Low' if Fare < 15, 'Medium' if 15 <= Fare < 50, else 'High'.
• Drop the SibSp and Parch columns from df permanently (inplace).
• Confirm the new columns exist with df.columns.
'''

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = df['FamilySize'] == 1
df['FareCategory'] = pd.cut(df['Fare'], bins=[-float('inf'), 15, 50, float('inf')], labels=['Low', 'Medium', 'High'])
df.drop(['SibSp', 'Parch'], axis=1, inplace=True)
print("Updated columns in the DataFrame:")
print(df.columns)


#Q06 Handle Missing Values

'''
Task:
• Find which columns have missing values and how many.
• Fill missing Age values with the median age (calculate it first, then fill).
• Drop any remaining rows that still have any null values.
• Verify the dataset is now completely clean (zero nulls).
'''

print("Missing values per column before handling:")
print(df.isnull().sum())
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)
df.dropna(inplace=True)
print("\nMissing values per column after handling:")
print(df.isnull().sum())
print("\nDataset is now clean ")


#SECTION 4 — GroupBy & Aggregations | Sorting

#Q07 Aggregate with GroupBy

'''
Task:
• Calculate the survival rate (mean of Survived) for each Pclass.
• For each Pclass, find the average and max Fare. Use .agg() with a dictionary.
• Count the number of survivors and non-survivors by Pclass. Use groupby + value_counts or pivot.
• Which Pclass had the highest average Fare? Print just that class number.
'''

survival_rate_by_pclass = df.groupby('Pclass')['Survived'].mean()
fare_stats_by_pclass = df.groupby('Pclass')['Fare'].agg(['mean', '  max'])
survivor_counts_by_pclass = df.groupby('Pclass')['Survived'].value_counts()
highest_avg_fare_class = fare_stats_by_pclass['mean'].idxmax()  
print("Survival rate by Pclass:")
print(survival_rate_by_pclass)
print("\nAverage and max Fare by Pclass:")
print(fare_stats_by_pclass)
print(f"\nPclass with the highest average Fare: {highest_avg_fare_class}")


#Q08 Sort & Rank Data

'''
Task:
• Sort the DataFrame by Fare in descending order. Show the top 5.
• Sort by Pclass ascending, then by Age descending. Show first 8 rows.
• Find the 3 passengers who paid the lowest fares. Display their PassengerId, Pclass, and Fare.
'''
print("Top 5 passengers by Fare (descending):")
print(df.sort_values(by='Fare', ascending=False).head())
print("\nData sorted by Pclass (asc) and Age (desc):")
print(df.sort_values(by=['Pclass', 'Age'], ascending=[True, False]).head(8))
print("\n3 passengers who paid the lowest fares:")
lowest_fare_passengers = df.nsmallest(3, 'Fare')[['PassengerId', 'Pclass', 'Fare']]
print(lowest_fare_passengers)


#SECTION 5 — Merging & Concatenating | Apply & Map

#Q09 Merge & Concatenate DataFrames
'''
Task:
• Create a small lookup DataFrame called class_info with columns Pclass [1,2,3] and ClassName
['First','Second','Third'].
• Merge df with class_info on Pclass using an inner join. Save as df_merged.
• Create df_top10 (top 10 highest fares) and df_bottom10 (lowest 10 fares). Concatenate them
vertically into df_combined and reset the index.
• How many rows does df_combined have?
'''

class_info = pd.DataFrame({'Pclass': [1, 2, 3],
    'ClassName': ['First', 'Second', 'Third']
})
df_merged = pd.merge(df, class_info, on='Pclass', how='inner')
df_top10 = df.nlargest(10, 'Fare')
df_bottom10 = df.nsmallest(10, 'Fare')
df_combined = pd.concat([df_top10, df_bottom10], ignore_index=True)
print(f"Number of rows in df_combined: {len(df_combined)}")


#Q10 Apply Custom Logic with Apply & Map

'''
Task:
• Using .apply() with a lambda, create a column AgeGroup: 'Child' if Age < 18, 'Adult' if 18 <= Age < 60,
else 'Senior'.
• Using .map(), create a column SurvivedLabel that maps 0 → 'Died' and 1 → 'Survived'.
• Using apply() on the whole row (axis=1), create a column RiskScore = Fare / (Age + 1). Round to 2
decimal places.
• Display the first 5 rows of [PassengerId, Age, AgeGroup, SurvivedLabel, RiskScore].
'''

df['AgeGroup'] = df['Age'].apply(lambda x: 'Child' if x < 18 else ('Adult' if x < 60 else 'Senior'))
df['SurvivedLabel'] = df['Survived'].map({0: 'Died', 1: 'Survived'})
df['RiskScore'] = df.apply(lambda row: round(row['Fare'] / (row['Age'] + 1), 2), axis=1)
print(df[['PassengerId', 'Age', 'AgeGroup', 'SurvivedLabel', 'RiskScore']].head())


#SECTION 6 — String Operations | DateTime | Saving Data

#Q11 String Operations with .str Accessor

'''
 Task:
• Convert the FareCategory column values to uppercase using .str.upper().
• Create a column PassengerCode by zero-padding PassengerId to 4 digits: e.g., 1 → '0001'. Use
.astype(str).str.zfill(4).
• Create a column ClassLabel by prepending 'CLASS-' to the Pclass string: e.g., 'CLASS-1'. Use .str
concatenation.
• Count how many passengers fall into each FareCategory (uppercase version).
'''                                       
df['FareCategory'] = df['FareCategory'].str.upper()
df['PassengerCode'] = df['PassengerId'].astype(str).str.zfill(4)
df['ClassLabel'] = 'CLASS-' + df['Pclass'].astype(str)
fare_category_counts = df['FareCategory'].value_counts()
print("FareCategory counts:")
print(fare_category_counts)


#Q12 DateTime Operations

'''
Task:
• Create a column EventDate with the value '1912-04-15' for every row. Convert it to datetime with
pd.to_datetime().
• Create a column YearsAgo = the number of years between today and EventDate. Use
pd.Timestamp.now() and .dt.days.
• Extract the month and day of week from EventDate into separate columns EventMonth and
EventDayOfWeek.
• What day of the week did the Titanic sink? Print the day name.
'''
df['EventDate'] = pd.to_datetime('1912-04-15')
df['YearsAgo'] = (pd.Timestamp.now() - df['EventDate']).dt.days // 365
df['EventMonth'] = df['EventDate'].dt.month
df['EventDayOfWeek'] = df['EventDate'].dt.day_name()
titanic_sinking_day = df['EventDayOfWeek'].iloc[0]
print(f"The Titanic sank on a {titanic_sinking_day}.")


#Q13 Save & Export Your Results

'''
Task:
• Save the full cleaned df to a new file called titanic_cleaned.csv without the row index.
• Save only survivors (Survived == 1) to titanic_survivors.csv.
• Save the Pclass survival rate table (from Q7) to a CSV called survival_by_class.csv.
• Export df to a JSON file called titanic_data.json using records orientation.

'''
df.to_csv('titanic_cleaned.csv', index=False)
df[df['Survived'] == 1].to_csv('titanic_survivors.csv', index=False)
survival_rate_by_pclass.to_csv('survival_by_class.csv')
df.to_json('titanic_data.json', orient='records')   
