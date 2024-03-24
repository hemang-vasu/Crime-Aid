import pandas as pd 
import math

# df = pd.read_csv("times.csv") 
df = pd.read_csv("predictions.csv") 

header = {
    'DATETIME': [],
    'Total Score': [],
    'AREA NAME': [],
    'LAT': [],
    'LON': []
}

newdf = pd.DataFrame(header)

# df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
unique_dates = df['DATE OCC'].unique()
# df['TIME OCC'] = pd.to_numeric(df['TIME OCC'], errors='coerce')

dateocc = df.iloc[0]['DATE OCC']
area = df.iloc[0]['AREA NAME']
score = df.iloc[0]['Total Score']
ttime = df.iloc[0]['TIME OCC'] 
lat = df.iloc[0]['LAT']
lon = df.iloc[0]['LON'] 
tscore = 0

# print(unique_dates)
for index, row in df.iterrows():
    ndateocc = row['DATE OCC']
    narea = row['AREA NAME']
    nscore = row['Total Score']
    ntime = row['TIME OCC'] 

    if ndateocc == dateocc and narea == area and ntime == ttime:
        tscore += nscore
    else:
        if ttime >= 10:
            cdf = pd.DataFrame({
                'DATETIME': [dateocc + ' ' + str(int(ttime)) + ":00:00"],
                'AREA NAME': [area],
                'Total Score': [tscore],
                'LAT': [lat],
                'LON': [lon]})
        else:
            cdf = pd.DataFrame({
            'DATETIME': [dateocc + ' 0' + str(int(ttime)) + ":00:00"],
            'AREA NAME': [area],
            'Total Score': [tscore],
            'LAT': [lat],
            'LON': [lon]})
        newdf = pd.concat([newdf, cdf], ignore_index = True)
        tscore = nscore
        dateocc = ndateocc
        area = narea
        ttime = ntime
        lat = row['LAT']
        lon = row['LON']
        # print(tscore)
        # print(newdf)

newdf = pd.concat([newdf, pd.DataFrame({
'DATETIME': [dateocc + ' ' + str(ttime)],
'AREA NAME': [area],
'Total Score': [tscore],
'LAT': [lat],
'LON': [lon]}, index=[0])], ignore_index= True)

# newdf.to_csv('gTimes.csv', index=False)
newdf.to_csv('predTimes.csv', index=False)

# for d in unique_dates:
#     for i in range(100, 2400, 100):
#         for city in ['Wilshire', 'Hollywood', 'Topanga', 'Mission', 'Southwest']:
#             filtered_df = df[(df['AREA NAME'] == city) & (df['DATE OCC'] == d) & (df['TIME OCC'] >= (i - 100)) & (df['TIME OCC'] < i)]
#             print(filtered_df)
            
#             df.subtract(filtered_df)