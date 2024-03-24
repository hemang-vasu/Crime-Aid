# importing pandas as pd 
import pandas as pd 

  
# read an excel file and convert  
# into a dataframe object 
df = pd.read_csv("Crimes.csv") 

df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])

df = df[["DATE OCC", "TIME OCC", "AREA NAME", "Crm Cd 1", "Crm Cd Desc"]]

# print((df.isnull().sum()).sort_values(ascending=False) / df.shape[0])

# print(df)
# print(df.dtypes)

df_car = df[df["Crm Cd Desc"].str.contains("VEHICLE") & ~df["Crm Cd Desc"].str.contains("FROM")]
#print(df_car)
# sample_car = df_car.sample(n = 200)
# pd.set_option('display.max_rows', None)
# print(sample_car)
# pd.reset_option('display.max_rows')

df_loc = df[(df["AREA NAME"] == "Wilshire") | (df["AREA NAME"] == "Hollywood") | 
(df["AREA NAME"] == "Southwest") | (df["AREA NAME"] == "Topanga") | (df["AREA NAME"] == "Mission")]

df_loc = df_loc[df_loc["Crm Cd Desc"].str.contains("VEHICLE") & ~df_loc["Crm Cd Desc"].str.contains("FROM") | df_loc["Crm Cd Desc"].str.contains("ASSAULT") | df_loc["Crm Cd Desc"].str.contains("SEX") | df_loc["Crm Cd Desc"].str.contains("RAPE") | df_loc["Crm Cd Desc"].str.contains("IDENTITY") | df_loc["Crm Cd Desc"].str.contains("HOMOCIDE")]
df_loc.loc[df_loc["Crm Cd Desc"].str.contains("SEX"), "Crm Cd Desc"]='SA'
df_loc.loc[df_loc["Crm Cd Desc"].str.contains("RAPE"), "Crm Cd Desc"]='SA'
df_loc.loc[df_loc["Crm Cd Desc"].str.contains("ASSAULT"), "Crm Cd Desc"]='ASSAULT'
df_loc.loc[df_loc["Crm Cd Desc"].str.contains("VEHICLE"), "Crm Cd Desc"]='VEHICLE'
df_loc.loc[df_loc["Crm Cd Desc"].str.contains("IDENTITY"), "Crm Cd Desc"]='ID THEFT'
df_loc.loc[df_loc["Crm Cd Desc"].str.contains("HOMOCIDE"), "Crm Cd Desc"]='HOMOCIDE'
#pd.set_option('display.max_rows', None)
#print(df_loc.sample(n=200))
df_loc = df_loc.drop_duplicates()
df_loc= df_loc.sort_values(["DATE OCC", "TIME OCC"])
print(len(df_loc))
df_loc.to_csv('output_cleaned.csv', index=False)