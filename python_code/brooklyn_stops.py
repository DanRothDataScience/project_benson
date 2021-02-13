
## https://en.wikipedia.org/wiki/List_of_New_York_City_Subway_stations_in_Brooklyn
## These stops were copy / pasted into a spreadsheet, dumped to csv and then loaded into pandas

df = pd.read_csv('dirty_wikipedia_stops.csv', header=None)
df.columns = ["stop", 1, 2, 3, 4, 5]

# The stops occasionally have some bad data on the next row that needs to be removed.  This data always starts with some variation
# of weird whitespace and a single train line.  I stripped the whitespace and then checked the first two characters for len == 1 
# after the trailing whitespace is removed.
stops = df['stop'].str.strip('\u200b ')
out = []
for stop in stops: 
    if len(stop[:2].strip()) != 1: 
        out.append(stop)

#The data was written out and then manual cleanup was performed, removing special unicode trailing characters and removing the "th", "rd", and "nd" from numbers
from bk_stops import bks
#Next I normalized the data into the format found in the turnstiles dataset
out = []
for stop in bks: 
   stop = stop.replace('AVENUE', 'AV') 
   stop = stop.replace('STREET', 'ST') 
   stop = stop.replace('PARKWAY', 'PKWY')
   out.append(stop)

#Now the data is ready to be loaded by using the out as a replace parameter to "Brooklyn" and assigning it to the borough
turnstiles_daily['Borough'] = turnstiles_daily['STATION'].replace(out, 'Brooklyn')
turnstiles_daily[turnstiles_daily['Borough'] == 'Brooklyn']
