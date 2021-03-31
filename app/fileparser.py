import pandas as pd

def load_unto_dataframe():
    myheaders = ["Airport ID","Name","City","Country","IATA","ICAO","Latitude",
        "Longitude", "Altitude", "Timezone", "DST", "TZ", "Type", "Source"]
    df = pd.read_csv("data/airports.dat", names=myheaders)
    df = df.replace("\\N", "Not Found")
    # resolve issue where can't be displayed - name,city (need to encode to UTF8)
    # issue due to polish letters
    return df
