# importing pandas as pd 
import pandas as pd 

  
# read an excel file and convert  
# into a dataframe object 
df = pd.read_csv("Crimes.csv") 

df = df[["DATE OCC", "TIME OCC", "AREA NAME", "Crm Cd 1", "Crm Cd Desc", "LAT", "LON"]]

# print((df.isnull().sum()).sort_values(ascending=False) / df.shape[0])

# print(df)
# print(df.dtypes)


df = df[(df["AREA NAME"] == "Wilshire") | (df["AREA NAME"] == "Hollywood") | 
(df["AREA NAME"] == "Southwest") | (df["AREA NAME"] == "Topanga") | (df["AREA NAME"] == "Mission")]

df_car = df[df["Crm Cd Desc"].str.contains("VEHICLE") & ~df["Crm Cd Desc"].str.contains("FROM")].copy()
df_car.loc[:, 'score'] = 45
# print(df_car)
# sample_car = df_car.sample(n = 200)
# pd.set_option('display.max_rows', None)
# print(sample_car)
# pd.reset_option('display.max_rows')


df_as = df[df["Crm Cd Desc"].str.contains("ASSAULT")].copy()
df_as.loc[:, 'score']  = 70
# sample_as = df_as.sample(n = 200)
# pd.set_option('display.max_rows', None)
# print(sample_as)
# pd.reset_option('display.max_rows')

df_sa = df[df["Crm Cd Desc"].str.contains("SEX") | df["Crm Cd Desc"].str.contains("RAPE")].copy()
df_sa.loc[:, 'score']  = 90
# sample_sa = df_sa.sample(n = 200)
# pd.set_option('display.max_rows', None)
# print(sample_sa)
# pd.reset_option('display.max_rows')
# print(df_sa)

df_id = df[df["Crm Cd Desc"].str.contains("IDENTITY")].copy()
df_id.loc[:, 'score'] = 25
# sample_id = df_id.sample(n = 200)
# pd.set_option('display.max_rows', None)
# print(sample_id)
# pd.reset_option('display.max_rows')
# print(df_id)

df_homi = df[df["Crm Cd Desc"].str.contains("HOMICIDE") | df["Crm Cd Desc"].str.contains("MURDER")].copy()
df_homi.loc[:, 'score'] = 100
# sample_homi = df_homi.sample(n = 200)
# pd.set_option('display.max_rows', None)
# print(sample_homi)
# pd.reset_option('display.max_rows')
# print(df_homi)


# unique_names = df[["Crm Cd 1", "Crm Cd Desc"]].drop_duplicates()
# print(unique_names)

# unique2 = df["Crm Cd Desc"].unique()
# print(unique2)
# df["crime_score"] = random.random()


# print(df)

df_combined = pd.concat([df_as, df_car, df_sa, df_homi, df_id])

df_combined = df_combined.drop_duplicates()
df_combined = df_combined[df_combined['AREA NAME'] == "Hollywood"]

df_combined.reset_index(drop=True, inplace=True)
# sample_combined = df_combined.sample(n = 500)
# pd.set_option('display.max_rows', None)
# print(sample_combined)
# pd.reset_option('display.max_rows')
# print(df_combined)
# df.loc[df['AREA NAME'] == 'Hollywood', 'score'] = df.loc[df['AREA NAME'] == 'Hollywood', 'score'] / 70000
# df.loc[df['AREA NAME'] == 'Wilshire', 'score'] = df.loc[df['Wilshire'] == 'Hollywood', 'score'] / 46000
# df.loc[df['AREA NAME'] == 'Southwest', 'score'] = df.loc[df['AREA NAME'] == 'Hollywood', 'score'] / 70000
# df.loc[df['AREA NAME'] == 'Hollywood', 'score'] = df.loc[df['AREA NAME'] == 'Hollywood', 'score'] / 70000
# df.loc[df['AREA NAME'] == 'Hollywood', 'score'] = df.loc[df['AREA NAME'] == 'Hollywood', 'score'] / 70000
df_combined.loc[df_combined["Crm Cd Desc"].str.contains("SEX"), "Crm Cd Desc"]='SA'
df_combined.loc[df_combined["Crm Cd Desc"].str.contains("RAPE"), "Crm Cd Desc"]='SA'
df_combined.loc[df_combined["Crm Cd Desc"].str.contains("ASSAULT"), "Crm Cd Desc"]='ASSAULT'
df_combined.loc[df_combined["Crm Cd Desc"].str.contains("VEHICLE"), "Crm Cd Desc"]='VEHICLE'
df_combined.loc[df_combined["Crm Cd Desc"].str.contains("IDENTITY"), "Crm Cd Desc"]='ID THEFT'
df_combined.loc[df_combined["Crm Cd Desc"].str.contains("HOMICIDE"), "Crm Cd Desc"]='HOMICIDE'
df_combined.loc[df_combined["Crm Cd Desc"].str.contains("MURDER"), "Crm Cd Desc"]='HOMICIDE'

df_combined = df_combined.sort_values(["DATE OCC", "TIME OCC", "AREA NAME"])

df_combined.to_csv('jv_output_cleaned.csv', index=False)

# SEX OFFENDER REGISTRANT OUT OF COMPLIANCE