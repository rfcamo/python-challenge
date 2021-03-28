# Imports here
import os
import csv


# Files to load and output
fileload = "employee_data.csv"
fileoutput = "PyBoss_Analysis.txt"

# Dictionary of states with abbreviations
state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

empid=[]
fname=[]
lname=[]
dob=[]
ssns=[]
state = []

# Read the csv and convert it into a list of dictionaries
with open(fileload) as emp_data:
    reader = csv.DictReader(emp_data)
	
    for row in reader:

        # Create empid list
        empid.append(row["Emp ID"])

        # Format and create dob list
        dob_format = row["DOB"].replace("-","/")
        dob = dob + [dob_format]
        
        # Name Split and create lname and fname list
        name = row["Name"].split()
        fname = fname + [name[0]]
        lname = lname + [name[1]]

        # Format ssn number
        ssn = row["SSN"]
        ssn_split = list(ssn)
        ssn_split[0:3] = ("*","*","*")
        ssn_split[4:6] = ("*","*")
        combined_ssn = "".join(ssn_split)
        ssns=ssns + [combined_ssn]

        # State abbreviate
        us_states = state_abbrev[row["State"]]
        state = state + [us_states]

# Zip all of the new lists together
empdb = zip(empid,fname,lname,dob,ssns,state)

# Write all of the election data to txt
with open(fileoutput, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp Id","First Name","Last Name","DOB","SSN","State"])
    writer.writerows(empdb)
