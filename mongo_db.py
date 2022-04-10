from flask import Flask
import pymongo
from app import app

# Connection string from MongoDb Atlas
CONN_STRING = "mongodb+srv://od_capstone:capPROJ123@cluster0.nrcft.mongodb.net/capstone-project?retryWrites=true&w=majority"

# Initiating mongodb client
def open_mongo_diseases(index):
    client = pymongo.MongoClient(CONN_STRING)
    # Loading database
    db = client.get_database('capstone-project')
    collection = db['crop-diseases']

    # Disease data dictionary is sourced from the collection
    disease_data = collection.find_one({'Id': int(index)})

    # CLI: Printing the dictionary
    print(type(disease_data))

    # Closing the MongoDB session after sourcing data.
    client.close()
    return disease_data

def new_data(entry_name, caused_by, about, link, cure):
    # Adding the data in MongoDB
    # Opening connection
    client = pymongo.MongoClient(CONN_STRING)
    # Loading database
    db = client.get_database('capstone-project')
    collection = db['new-data']

    # alert variable
    alert=''

    # Creating dictionary
    entry_dict = {
        "Name": entry_name,
        "Caused_by": caused_by,
        "About": about,
        "More_info_link": link,
        "Cure": cure
    }

    # Checking for duplicacy
    dupl_data = collection.find()

    # Variable to check if duplicate is present
    counter=0

    for entry in dupl_data:
        if entry['Name'] == entry_name:
            print("Crop already entered by user.")
            alert = "Crop already entered by user."
            counter = 1
            break
    
    if counter == 0:
        # Inserting the dictionary
        collection.insert_one(entry_dict)

        # CLI: Printing the entry
        check_dict = collection.find().sort({'Name':-1}).limit(1)

        if check_dict['Name'] == entry_name:
            print(check_dict)
            print("Entry Successful")
            alert = "successful"
        else:
            print("Entry unsuccessful")
            alert = "unsuccessful"

    # Closing the MongoDB session after inserting data.
    client.close()
    return alert