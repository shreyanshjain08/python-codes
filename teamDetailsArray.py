import numpy as np

# Function to collect data from a single team with input validation
def collect_team_data():
    name = input("Enter Team Member Name: ")
    city = input("Enter City: ")
    college = input("Enter College name: ")
    whatsapp_number = input("Enter WhatsApp Number: ")
    life_purpose = input("Enter Life Purpose in Max 5 Words: ")

    words = life_purpose.split()

    # Validate life purpose length
    while len(words) > 5:
        print("Life purpose cannot exceed 5 words. Please re-enter.")
        life_purpose = input("Enter Life Purpose in Max 5 Words: ")
        words = life_purpose.split()

    return {"Name": name, "City": city, "College": college, "WhatsApp Number": whatsapp_number, "Life Purpose": life_purpose}

# Collect data from all five teams
team_data = []
for i in range(5):
    print(f"\nCollecting Data from Team {i+1}")
    team_data.append(collect_team_data())

# Create the NumPy array
data_array = np.array(team_data, dtype=object)

# Print the table with formatted headers (assuming string data types)
print("\nTeam Member Data:")
print("{:<20} {:<20} {:<20} {:<25} {:<20}".format("Name", "City", "College", "WhatsApp Number", "Life Purpose"))
for row in data_array:
    print("{:<20} {:<20} {:<20} {:<25} {:<20}".format(row["Name"], row["City"], row["College"], row["WhatsApp Number"], row["Life Purpose"]))
