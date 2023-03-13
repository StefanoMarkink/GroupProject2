<<<<<<< HEAD
<<<<<<< HEAD
import pandas as pd

df= pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vTt2zTAl0BKc4VO8SZwexi2sHjAwryHhxEvgTHDpqYaZRFULG4ykJuiwTXSk9xEEJ4eWlpmRxBT_GrW/pub?output=xlsx')

name=["What is your name?"]
email=["What is your email?"]
=======
#Hello
=======
>>>>>>> d484826f816568186e89c01598e2833d44788b72
import pandas as pd
import csv
import random
import copy
import os


df= pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vTt2zTAl0BKc4VO8SZwexi2sHjAwryHhxEvgTHDpqYaZRFULG4ykJuiwTXSk9xEEJ4eWlpmRxBT_GrW/pub?output=xlsx')

name="What is your name?"
email="What is your email?"
# path to the CSV files with participant data
participants_csv = "Coffee Partner Lottery participants.csv"

# header names in the CSV file (name and e-mail of participants)
header_name = "Your name:"
header_email = "Your e-mail:"

# path to TXT file that stores the pairings of this round
new_pairs_txt = "Coffee Partner Lottery new pairs.txt"

# path to CSV file that stores the pairings of this round
new_pairs_csv = "Coffee Partner Lottery new pairs.csv"

# path to CSV file that stores all pairings (to avoid repetition)
all_pairs_csv = "Coffee Partner Lottery all pairs.csv"
        
# init set of old pairs
opairs = set()

DELIMITER=','

print(' Test')

# load all previous pairings (to avoid redundancies)
if os.path.exists(all_pairs_csv):
    with open(all_pairs_csv, "r") as file:
        csvreader = csv.reader(file, delimiter=DELIMITER)
        for row in csvreader:
            group = []
            for i in range(0,len(row)):
                group.append(row[i])                        
            opairs.add(tuple(group))

# load participant's data
formdata = pd.read_csv(participants_csv, sep=DELIMITER)

# create duplicate-free list of participants
participants = list(set(formdata[header_email]))

 # init set of new pairs
npairs = set()

# running set of participants
nparticipants = copy.deepcopy(participants)

# Boolean flag to check if new pairing has been found
new_pairs_found = False

# try creating new pairing until successful
while not new_pairs_found:   # to do: add a maximum number of tries
  
    # if odd number of participants, create one triple, then pairs
    if len(participants)%2 != 0:
        
        # take three random participants from list of participants
        p1 = random.choice(nparticipants)
        nparticipants.remove(p1)
    
        p2 = random.choice(nparticipants)
        nparticipants.remove(p2)
        
        p3 = random.choice(nparticipants)
        nparticipants.remove(p3)
        
        # create alphabetically sorted list of participants
        plist = [p1, p2, p3]
        plist.sort()
                        
        # add alphabetically sorted list to set of pairs
        npairs.add(tuple(plist))

  
    # while still participants left to pair...
    while len(nparticipants) > 0:

        # take two random participants from list of participants
        p1 = random.choice(nparticipants)
        nparticipants.remove(p1)
    
        p2 = random.choice(nparticipants)
        nparticipants.remove(p2)
                
        # create alphabetically sorted list of participants
        plist = [p1, p2]
        plist.sort()
                        
        # add alphabetically sorted list to set of pairs
        npairs.add(tuple(plist))

 
    # check if all new pairs are indeed new, else reset
    if npairs.isdisjoint(opairs):
        new_pairs_found = True
    else:
        npairs = set()
        nparticipants = copy.deepcopy(participants)


# assemble output for printout
output_string = ""

output_string += "------------------------\n"
output_string += "Today's coffee partners:\n"
output_string += "------------------------\n"

group_names = []

for pair in npairs:
    pair = list(pair)
    names_pergroup = []
    output_string += "* "
    for i in range(0,len(pair)):
        name_email_pair = f"{formdata[formdata[header_email] == pair[i]].iloc[0][header_name]} ({pair[i]})"
        names_pergroup.append(f"{formdata[formdata[header_email] == pair[i]].iloc[0][header_name]}")
        if i < len(pair)-1:
            output_string += name_email_pair + ", "
        else:
            output_string += name_email_pair + "\n"
            
    group_names.append(names_pergroup)
            
print(group_names)





















### 8. The program generates messages to all groups which address the participants by name, inform
## them about having been matched for a meeting, and include the conversation starter. It saves these
## messages in one or multiple text files.

introtext = ""
for group in group_names:
    introduction = "Hey"
    for person in group:
        introduction += " " +person

    introduction += ", you have been matched for a meeting. To get the conversation started use X. \n \n"
    introtext += introduction



with open("introduction.txt", "wb") as file:
    file.write(introtext.encode("utf8"))

    
# write output to console
print(output_string)

# write output into text file for later use
with open(new_pairs_txt, "wb") as file:
    file.write(output_string.encode("utf8"))



# write new pairs into CSV file (for e.g. use in MailMerge)
with open(new_pairs_csv, "w") as file:
    header = ["name1", "email1", "name2", "email2", "name3", "email3"]
    file.write(DELIMITER.join(header) + "\n")
    for pair in npairs:
        pair = list(pair)
        for i in range(0,len(pair)):
            name_email_pair = f"{formdata[formdata[header_email] == pair[i]].iloc[0][header_name]}{DELIMITER} {pair[i]}"
            if i < len(pair)-1:
                file.write(name_email_pair + DELIMITER + " ")
            else:
                file.write(name_email_pair + "\n")
                
# append pairs to history file
if os.path.exists(all_pairs_csv):
    mode = "a"
else:
    mode = "w"

with open(all_pairs_csv, mode) as file:
    for pair in npairs:
        pair = list(pair)
        for i in range(0,len(pair)):
            if i < len(pair)-1:
                file.write(pair[i] + DELIMITER)
            else:
                file.write(pair[i] + "\n")


<<<<<<< HEAD
             
# print finishing message
print()
print("Job done.")
>>>>>>> StefanoProject
=======
# print finishing message
print()
=======
import pandas as pd
import csv
import random
import copy
import os

# path to the CSV files with participant data
participants_csv = "Coffee Partner Lottery participants.csv"

# header names in the CSV file (name and e-mail of participants)
header_name = "Your name:"
header_email = "Your e-mail:"

# path to TXT file that stores the pairings of this round
new_pairs_txt = "Coffee Partner Lottery new pairs.txt"

# path to CSV file that stores the pairings of this round
new_pairs_csv = "Coffee Partner Lottery new pairs.csv"

# path to CSV file that stores all pairings (to avoid repetition)
all_pairs_csv = "Coffee Partner Lottery all pairs.csv"
        
# init set of old pairs
opairs = set()

DELIMITER=','

print(' Test')

# load all previous pairings (to avoid redundancies)
if os.path.exists(all_pairs_csv):
    with open(all_pairs_csv, "r") as file:
        csvreader = csv.reader(file, delimiter=DELIMITER)
        for row in csvreader:
            group = []
            for i in range(0,len(row)):
                group.append(row[i])                        
            opairs.add(tuple(group))

# load participant's data
formdata = pd.read_csv(participants_csv, sep=DELIMITER)

# create duplicate-free list of participants
participants = list(set(formdata[header_email]))

 # init set of new pairs
npairs = set()

# running set of participants
nparticipants = copy.deepcopy(participants)

# Boolean flag to check if new pairing has been found
new_pairs_found = False

# try creating new pairing until successful
while not new_pairs_found:   # to do: add a maximum number of tries
  
    # if odd number of participants, create one triple, then pairs
    if len(participants)%2 != 0:
        
        # take three random participants from list of participants
        p1 = random.choice(nparticipants)
        nparticipants.remove(p1)
    
        p2 = random.choice(nparticipants)
        nparticipants.remove(p2)
        
        p3 = random.choice(nparticipants)
        nparticipants.remove(p3)
        
        # create alphabetically sorted list of participants
        plist = [p1, p2, p3]
        plist.sort()
                        
        # add alphabetically sorted list to set of pairs
        npairs.add(tuple(plist))

  
    # while still participants left to pair...
    while len(nparticipants) > 0:

        # take two random participants from list of participants
        p1 = random.choice(nparticipants)
        nparticipants.remove(p1)
    
        p2 = random.choice(nparticipants)
        nparticipants.remove(p2)
                
        # create alphabetically sorted list of participants
        plist = [p1, p2]
        plist.sort()
                        
        # add alphabetically sorted list to set of pairs
        npairs.add(tuple(plist))

 
    # check if all new pairs are indeed new, else reset
    if npairs.isdisjoint(opairs):
        new_pairs_found = True
    else:
        npairs = set()
        nparticipants = copy.deepcopy(participants)


# assemble output for printout
output_string = ""

output_string += "------------------------\n"
output_string += "Today's coffee partners:\n"
output_string += "------------------------\n"

group_names = []

for pair in npairs:
    pair = list(pair)
    names_pergroup = []
    output_string += "* "
    for i in range(0,len(pair)):
        name_email_pair = f"{formdata[formdata[header_email] == pair[i]].iloc[0][header_name]} ({pair[i]})"
        names_pergroup.append(f"{formdata[formdata[header_email] == pair[i]].iloc[0][header_name]}")
        if i < len(pair)-1:
            output_string += name_email_pair + ", "
        else:
            output_string += name_email_pair + "\n"
            
    group_names.append(names_pergroup)
            
print(group_names)





















### 8. The program generates messages to all groups which address the participants by name, inform
## them about having been matched for a meeting, and include the conversation starter. It saves these
## messages in one or multiple text files.

introtext = ""
for group in group_names:
    introduction = "Hey"
    for person in group:
        introduction += " " +person

    introduction += ", you have been matched for a meeting. To get the conversation started use X. \n \n"
    introtext += introduction



with open("introduction.txt", "wb") as file:
    file.write(introtext.encode("utf8"))

    
# write output to console
print(output_string)

# write output into text file for later use
with open(new_pairs_txt, "wb") as file:
    file.write(output_string.encode("utf8"))



# write new pairs into CSV file (for e.g. use in MailMerge)
with open(new_pairs_csv, "w") as file:
    header = ["name1", "email1", "name2", "email2", "name3", "email3"]
    file.write(DELIMITER.join(header) + "\n")
    for pair in npairs:
        pair = list(pair)
        for i in range(0,len(pair)):
            name_email_pair = f"{formdata[formdata[header_email] == pair[i]].iloc[0][header_name]}{DELIMITER} {pair[i]}"
            if i < len(pair)-1:
                file.write(name_email_pair + DELIMITER + " ")
            else:
                file.write(name_email_pair + "\n")
                
# append pairs to history file
if os.path.exists(all_pairs_csv):
    mode = "a"
else:
    mode = "w"

with open(all_pairs_csv, mode) as file:
    for pair in npairs:
        pair = list(pair)
        for i in range(0,len(pair)):
            if i < len(pair)-1:
                file.write(pair[i] + DELIMITER)
            else:
                file.write(pair[i] + "\n")


# print finishing message
print()
>>>>>>> 0f7a8cbe8a0fa5501e49c0f1cd846c24376ee174
print("Job done.")
>>>>>>> d484826f816568186e89c01598e2833d44788b72
