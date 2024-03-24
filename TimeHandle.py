import pandas as pd 
import math

df = pd.read_csv("jv_output_cleaned.csv") 

header = {
    'DATE OCC': [],
    'TIME OCC': [],
    'Total Score': [],
    'AREA NAME': [],
    'LAT': [],
    'LON': []
}

newdf = pd.DataFrame(header)

df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
unique_dates = df['DATE OCC'].unique()
df['TIME OCC'] = pd.to_numeric(df['TIME OCC'], errors='coerce')

dateocc = df.iloc[0]['DATE OCC']
area = df.iloc[0]['AREA NAME']
score = df.iloc[0]['score']
ttime = math.floor(df.iloc[0]['TIME OCC'] / 100)
lat = df.iloc[0]['LAT']
lon = df.iloc[0]['LON']
tscore = 0

# print(unique_dates)
for index, row in df.iterrows():
    ndateocc = row['DATE OCC']
    narea = row['AREA NAME']
    nscore = row['score']
    ntime = math.floor(row['TIME OCC'] / 100)

    if ndateocc == dateocc and narea == area and nscore == score and ntime == ttime:
        tscore += nscore
    else:
        cdf = pd.DataFrame({
            'DATE OCC': [dateocc],
            'TIME OCC': [ttime],
            'AREA NAME': [area],
            'Total Score': [tscore],
            'LAT': [lat],
            'LON': [lon]})
        newdf = pd.concat([cdf, newdf], ignore_index = True)
        tscore = nscore
        dateocc = ndateocc
        area = narea
        score = nscore
        ttime = ntime
        lat = row['LAT']
        lon = row['LON']
        # print(newdf)

newdf = pd.concat([newdf, pd.DataFrame({
'DATE OCC': dateocc,
'TIME OCC': ttime,
'AREA NAME': area,
'Total Score': tscore,
'LAT': [lat],
'LON': [lon]}, index=[0])], ignore_index= True)

newdf = newdf.sort_values(["DATE OCC", "TIME OCC", "AREA NAME"])

newdf.to_csv('times.csv', index=False)


# for d in unique_dates:
#     for i in range(100, 2400, 100):
#         for city in ['Wilshire', 'Hollywood', 'Topanga', 'Mission', 'Southwest']:
#             filtered_df = df[(df['AREA NAME'] == city) & (df['DATE OCC'] == d) & (df['TIME OCC'] >= (i - 100)) & (df['TIME OCC'] < i)]
#             print(filtered_df)
            
#             df.subtract(filtered_df)