import random

# List of German first and last names
first_names = ['Anna', 'Max', 'Sophie', 'Leon', 'Mia', 'Ben', 'Emma', 'Paul', 'Hanna', 'Lukas', 'Lea', 'Finn', 'Julian', 'Clara', 'Noah', 'Marie', 'Tom', 'Ella', 'Felix', 'Lina', 'Jonas', 'Laura', 'Tim', 'Lena']
last_names = ['Müller', 'Mustermann', 'Schneider', 'Fischer', 'Weber', 'Meyer', 'Wagner', 'Becker', 'Schulz', 'Hoffmann', 'Zimmermann', 'Krüger', 'Braun', 'Lange', 'Klein', 'König', 'Böhm', 'Graf', 'Schmid', 'Peters', 'Jung', 'Fuchs', 'Neumann', 'Busch']

# Generate phone numbers
def generate_phone_number():
    return f"+49 {random.randint(150, 179)} {random.randint(1000000, 9999999)}"

# Generate data
data = []
for i in range(1, 501):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    phone = generate_phone_number()
    data.append((i, name, phone))

# Save to an SQL file
with open('german_contacts.sql', 'w') as file:
    file.write("CREATE TABLE GermanContacts (\n")
    file.write("    ID INT AUTO_INCREMENT PRIMARY KEY,\n")
    file.write("    Name VARCHAR(255) NOT NULL,\n")
    file.write("    PhoneNumber VARCHAR(15) NOT NULL\n")
    file.write(");\n\n")
    file.write("INSERT INTO GermanContacts (ID, Name, PhoneNumber) VALUES\n")
    file.writelines([f"({id}, '{name}', '{phone}'),\n" for id, name, phone in data[:-1]])
    file.write(f"({data[-1][0]}, '{data[-1][1]}', '{data[-1][2]}');\n")

