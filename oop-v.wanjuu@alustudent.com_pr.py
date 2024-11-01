class Patient:
    def __init__(self, id, name, age, gender, admission_date, condition):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition

    def get_details(self):
        return (f"Patient ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Admission Date: {self.admission_date}\n"
                f"Condition: {self.condition}\n")


# Function to count the number of patients in a list
def count_patients(patient_list):
    return len(patient_list)


# Function to list all patient names
def list_patient_names(patient_list):
    return [patient.name for patient in patient_list]


# Testing the Code
if __name__ == "__main__":
    # Creating patient objects
    patient1 = Patient(1, "Linda Maria", 30, "Female", "2024-10-15", "Flu")
    patient2 = Patient(2, "Tariq Jones", 45, "Male", "2024-10-20", "Broken Arm")
    patient3 = Patient(3, "Victor Charlie", 22, "Male", "2024-10-25", "Allergy")

    # Store patients in a list
    patient_list = [patient1, patient2, patient3]

    # Testing the get_details method
    print("Patient Details:")
    for patient in patient_list:
        print(patient.get_details())

    # Testing the count_patients function
    print("Total number of patients:", count_patients(patient_list))

    # Testing the list_patient_names function
    print("List of patient names:", list_patient_names(patient_list))
