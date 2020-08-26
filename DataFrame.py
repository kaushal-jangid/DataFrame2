import pandas as pd
import datetime
row_data = [{
            "lastCheckedDate": 1598367714241,
            "lastCheckedDateForEW": 1598362000461,
            "dataUpload": [
                {
                    "organizations": [
                        {
                            "name": "ECOMA, Inc. (Dallas, TX Office) -  (ECOM AgroindustrialCorp Cotton)",
                            "ID": 1057434
                        }
                    ],
                    "ID": 710
                }
            ],
            "ID": 3,
            "assignedDA": [
                {
                    "name": "Megha Sharma",
                    "ID": 953
                }
            ]
        },
        {
                    "lastCheckedDate": 1598367715000,
                    "lastCheckedDateForEW": 1598866004461,
                    "dataUpload": [
                        {
                            "organizations": [
                                {
                                    "name": "ECOMB, Inc. (Dallas, TX Office) -  (ECOM AgroindustrialCorp Cotton)",
                                    "ID": 1057434
                                }
                            ],
                            "ID": 710
                        }
                    ],
                    "ID": 3,
                    "assignedDA": [
                        {
                            "name": "Megha Sharma2",
                            "ID": 953
                        }
                    ]
                }]

# Function to convert EPoch to UTC
def EpochConverter(epochValue):
    return datetime.datetime.fromtimestamp(epochValue/1e3)

# Process DataFrame
df = pd.DataFrame(row_data)

# Amend Values
df['lastCheckedDate'] = df['lastCheckedDate'].apply(EpochConverter)
df['lastCheckedDateForEW'] = df['lastCheckedDateForEW'].apply(EpochConverter)

def OrgAddress(Value):
    return row_data[Value]['dataUpload'][Value]['organizations'][Value]['name']

df.insert(2,"Organisation", OrgAddress(0)) # TODO : Need function to traverse value Should be scalar

def Name(Value):
    return row_data[Value]['assignedDA'][Value]['name']

df.insert(3,"Name", Name(0)) # TODO : Need function to traverse value Should be scalar

# using now() to get current time
current_time = datetime.datetime.now()
df.insert(4,"Current_Time",current_time)

# Insert New DataFrame for Org


# Insert New row to calculate time Difference
df['Time_Difference'] = df['Current_Time'] - df['lastCheckedDate']

# Final Columns to be printed
print(df[['lastCheckedDate', 'lastCheckedDateForEW' , 'Organisation', 'Name' , 'Current_Time' , 'Time_Difference']])
