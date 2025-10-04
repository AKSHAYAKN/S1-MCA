contacts1 = {
    "Amu":"9878654387", "Teena":"6878231223"
}
contacts2 = {"Jhon":"7865989073","Priya":"7889905664"}
print("contacts1:", contacts1)
print("contacts2:", contacts2)
merged_contacts = contacts1.copy()
merged_contacts.update(contacts2)
print("merged_contacts:")
print(merged_contacts)