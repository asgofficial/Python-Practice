import csv
from datetime import datetime


# -------------------------------------------------
# 1. PATIENT REGISTRATION - DICTIONARY
# -------------------------------------------------

patients = {}

def register_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    phone = input("Enter Phone Number: ")

    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone
    }

    print("Patient registered successfully!")


# -------------------------------------------------
# 2. APPOINTMENT SCHEDULING - LIST
# -------------------------------------------------

appointments = []

def schedule_appointment():
    patient_id = input("Enter Patient ID: ")
    doctor = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date: ")

    appointment = [patient_id, doctor, date]
    appointments.append(appointment)

    print("Appointment scheduled successfully!")


# -------------------------------------------------
# 3. MEDICAL RECORDS - FILE HANDLING
# -------------------------------------------------

def add_medical_record():
    patient_id = input("Enter Patient ID: ")
    diagnosis = input("Enter Diagnosis: ")
    treatment = input("Enter Treatment: ")
    medicines = input("Enter Medicines: ")

    with open("medical_records.txt", "a") as file:
        file.write(
            f"{patient_id},{diagnosis},{treatment},{medicines}\n"
        )

    print("Medical record saved successfully!")


def view_medical_records():
    try:
        with open("medical_records.txt", "r") as file:
            records = file.readlines()

            print("\nMedical Records")
            print("-------------------------")

            for record in records:
                print(record.strip())

    except FileNotFoundError:
        print("No medical records found.")


# -------------------------------------------------
# 4. DOCTOR INFORMATION - TUPLE
# -------------------------------------------------

doctors = (
    ("D001", "Dr. Sharma", "Cardiologist"),
    ("D002", "Dr. Mehta", "Neurologist"),
    ("D003", "Dr. Singh", "Orthopedic")
)

def show_doctors():

    print("\nDoctor Information")
    print("-------------------------")

    for doctor in doctors:
        print("Doctor ID:", doctor[0])
        print("Name:", doctor[1])
        print("Specialization:", doctor[2])
        print("-------------------------")


# -------------------------------------------------
# 5. BILLING SYSTEM - CLASS AND OBJECT
# -------------------------------------------------

class Billing:

    def __init__(self, patient_id, consultation, medicine, room):
        self.patient_id = patient_id
        self.consultation = consultation
        self.medicine = medicine
        self.room = room

    def calculate_bill(self):
        total = self.consultation + self.medicine + self.room
        return total

    def show_bill(self):
        total = self.calculate_bill()

        print("\nPatient Bill")
        print("-------------------------")
        print("Patient ID:", self.patient_id)
        print("Consultation:", self.consultation)
        print("Medicine:", self.medicine)
        print("Room Charges:", self.room)
        print("Total Bill:", total)


def generate_bill():

    patient_id = input("Enter Patient ID: ")

    consultation = float(
        input("Enter Consultation Charges: ")
    )

    medicine = float(
        input("Enter Medicine Charges: ")
    )

    room = float(
        input("Enter Room Charges: ")
    )

    bill = Billing(
        patient_id,
        consultation,
        medicine,
        room
    )

    bill.show_bill()


# -------------------------------------------------
# 6. REPORT GENERATION - PYTHON LIBRARIES
# -------------------------------------------------

def generate_report():

    filename = "hospital_report.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Patient ID", "Name", "Age", "Gender", "Phone"]
        )

        for patient_id, data in patients.items():

            writer.writerow([
                patient_id,
                data["name"],
                data["age"],
                data["gender"],
                data["phone"]
            ])

    print("Report generated successfully!")
    print("Report saved as:", filename)


# -------------------------------------------------
# MAIN MENU
# -------------------------------------------------

while True:

    print("\n========== HOSPITAL MANAGEMENT SYSTEM ==========")

    print("1. Register Patient")
    print("2. Schedule Appointment")
    print("3. Add Medical Record")
    print("4. View Medical Records")
    print("5. Show Doctors")
    print("6. Generate Bill")
    print("7. Generate Patient Report")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_patient()

    elif choice == "2":
        schedule_appointment()

    elif choice == "3":
        add_medical_record()

    elif choice == "4":
        view_medical_records()

    elif choice == "5":
        show_doctors()

    elif choice == "6":
        generate_bill()

    elif choice == "7":
        generate_report()

    elif choice == "8":
        print("Thank you for using Hospital Management System!")
        break

    else:
        print("Invalid choice!")