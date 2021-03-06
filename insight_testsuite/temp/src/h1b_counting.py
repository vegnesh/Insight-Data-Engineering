import csv


# Loading CSV data into as a dictionary. Every row is a dictionary and its stored as a list in DATALIST
DataList = []
#with open('Sample_data.csv.txt', mode='r') as csv_file:
with open('../input/h1b_input.csv', mode='r', encoding="utf8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ';')
    line_count = 0
    for row in csv_reader:
        DataList.append(row)


# Intermediate Data Types - Store Company ID, Company Name and States
SOC_Code_List = []
State_List    = []
SOC_Dict = {}

# Loops through DATALIST to store only the company details and state details for the people whose H1B is certified.
for x in DataList:
    if (x["CASE_STATUS"].upper() == "CERTIFIED"):
        SOC_Code_List.append(x["SOC_CODE"])
        State_List.append(x["WORKSITE_STATE"])
        SOC_Dict[x["SOC_CODE"]] = x["SOC_NAME"]
      


# Identifies the unique states and company names - Used for obtaining the statistics    
SOC_Code_Set = list(SOC_Dict.keys())
State_Set = set(State_List)

# Obtains the count of number of certified H1B in each state/Company
State_Count = []
for x in State_Set:
    State_Count.append(State_List.count(x))
SOC_Count = []
for x in SOC_Code_Set:
    SOC_Count.append(SOC_Code_List.count(x))

Total_State = sum(State_Count)
Total_SOC = sum(SOC_Count)

Per_State = []
Per_SOC = []

# Estimating the percentages
for x in State_Count:
    Per_State.append(str(round(x/Total_State*100.0,1))+'%')

for x in SOC_Count:
    Per_SOC.append(str(round(x/Total_SOC*100.0,1))+'%')

# Sorting according to the preference given    
zippedState = zip(State_Count,State_Set, Per_State)
zippedSOC   = zip(SOC_Count,SOC_Code_Set, Per_SOC)
Final_State = sorted(zippedState, key = lambda x:(-x[0],x[1]))
Final_SOC   = sorted(zippedSOC, key = lambda x:(-x[0],SOC_Dict[x[1]]))


# Writing into Files
myFile = open('../output/top_10_occupations.txt', 'w')
numVal = 0
with myFile:
    headers = ["TOP_OCCUPATIONS","NUMBER_CERTIFIED_APPLICATIONS","PERCENTAGE"]
    writer = csv.DictWriter(myFile, fieldnames=headers, delimiter = ";")
    writer.writeheader()
    for x,y,z in Final_SOC:
        writer.writerow({'TOP_OCCUPATIONS':SOC_Dict[y],'NUMBER_CERTIFIED_APPLICATIONS':x,'PERCENTAGE':z})
        numVal = numVal + 1
        if (numVal >= 10):
            break
        
numVal = 0
myFile2 = open('../output/top_10_states.txt', 'w')
with myFile2:
    headers = ["TOP_STATES","NUMBER_CERTIFIED_APPLICATIONS","PERCENTAGE"]
    writer = csv.DictWriter(myFile2, fieldnames=headers, delimiter = ";")
    writer.writeheader()
    for x,y,z in Final_State:
        writer.writerow({'TOP_STATES':y,'NUMBER_CERTIFIED_APPLICATIONS':x,'PERCENTAGE':z})
        numVal = numVal + 1
        if (numVal >= 10):
            break
