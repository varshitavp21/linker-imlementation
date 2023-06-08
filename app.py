import streamlit as st
import sqlite3

# Set up the Streamlit application
st.title("Voter Registration Form")
st.write("hello")

# Define the form fields
# first_name = st.text_input("First Name")
# last_name = st.text_input("Last Name")
# address = st.text_input("Address")
# city = st.text_input("City")
# state = st.text_input("State")
# zip_code = st.text_input("Zip Code")
# phone_number = st.text_input("Phone Number")
# email_address = st.text_input("Email Address")

# # Handle form submission
# if st.button("Submit"):
#     # Create a new voter registration record
#     voter_registration_record = {
#         "first_name": first_name,
#         "last_name": last_name,
#         "address": address,
#         "city": city,
#         "state": state,
#         "zip_code": zip_code,
#         "phone_number": phone_number,
#         "email_address": email_address,
#     }

#     # Connect to the SQLite database
#     conn = sqlite3.connect("voter_registration.db")

#     # Create a new table (if it doesn't exist)
#     c = conn.cursor()
#     c.execute('''
#     CREATE TABLE IF NOT EXISTS voter_registration (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zip_code text,
#         phone_number text,
#         email_address text
#     )
#     ''')

#     # Insert the voter registration record into the table
#     c.execute('''
#     INSERT INTO voter_registration (first_name, last_name, address, city, state, zip_code, phone_number, email_address)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#     ''', (first_name, last_name, address, city, state, zip_code, phone_number, email_address))

#     # Commit the changes to the database
#     conn.commit()

#     # Close the connection to the database
#     conn.close()

#     # Display a success message
#     st.success("Your voter registration record has been submitted successfully!")
