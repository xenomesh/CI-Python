import pickle
# THIS IS THE SECOND FILE FOR HOMEWORK 4
def pickle_it(contacts):
    output_file = open('contacts.dat', 'wb')
    pickle.dump(contacts, output_file)
    output_file.close()

def unpickle_it():
    input_file = open('contacts.dat', 'rb')
    # Load the contact dictionary or create an empty dictionary if file is empty
    try:
        contacts = pickle.load(input_file)
    except:
        contacts = {}

    # Close the file
    input_file.close()
    # Return the contacts dictionary
    return contacts
