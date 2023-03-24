import requests
import json
import csv
import pandas as pd



url_path = 'https://www.themuse.com/api/public/jobs?page=50'
read_json= requests.get(url_path)
print (read_json)

data = read_json.json()
print (data)

print (type (data))

handling_json_file = json.dumps(data, indent=2)  # for print data as a dictionary more easier to read than json 

print (handling_json_file)


# Create json file ---------------
with open ('new_data.json', 'w') as f:
    f.write(handling_json_file)


# Extracting the data from Json file ------

for i in read_json.json()["results"]:
    print (i ['locations'][0]["name"])
    
for i in read_json.json()["results"]:
    print (i ['locations'][0]["name"], ('===>') ,i ['categories'][0]["name"])   
    
# Extracting the data that required from from the “Response body” from Json file ------ 
for i in read_json.json()["results"]:
    print (i ["publication_date"], 
           i ['type'],
           i ['company']['name'],
           i ['locations'][0]["name"],
           i ['categories'][0]["name"])
    
# Create CSV file and stor the data into CSV file ---------------

with open("jobs.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Publication_Date", "Job_type", "company_name" ,"locations", "Job_name"]) # Write header row
    for i in data["results"]:         # Write data rows
        writer.writerow([i["publication_date"],
                            i['type'],
                            i['company']['name'],
                            i['locations'][0]["name"],
                            i['categories'][0]["name"]])


# Manipulate data: create a table include:--------

df = pd.read_csv ('jobs.csv')
df.head()  
df.info()

# Make a date simple with Regular Expressions ------

df["Publication_Date"]= df["Publication_Date"].str.extract("(\d+-\d+-\d+)") 
# separate the locations column for two columns ( city and country ----
df[['City', 'country']] = df.locations.str.split(",", expand = True)
# drop locations column -------
df.drop("locations", axis=1, inplace=True) 
print (df)  

# save df into csv ------ 
df.to_csv('jobs_to_s3.csv')




