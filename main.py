from abc import ABC, abstractmethod

class User (ABC):
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_gender(self,gender):
        self.__gender = gender

    def get_name(self):
        return self.__name   
     
    def get_age(self):
        return self.__age   
    
    def get_gender(self):
        return self.__gender  
     
    @abstractmethod
    def display_info(self):
        pass 
    
class Patient (User):

    def __init__(self, name, age, gender,patient_id):
        super().__init__(name, age, gender)
        self.__patient_id = patient_id
        self.__medical_history =[]

    def set_patient_id(self,pateient_id):
        self.__patient_id = pateient_id

    def get_patient_id(self):
        return self.__patient_id
    
    def add_medical_record(self,record):
        self.__medical_history.append(record)    

    def get_medical_history(self):
        return self.__medical_history     
    
    def display_info(self):
        print ("Patient Information: ")
        print (f"Name: {self.get_name()}")
        print (f"Age: {self.get_age()}")
        print (f"Gender: {self.get_gender()}")
        print (f"Patient ID: {self.get_patient_id()}")
        print ("Medical history: ")
        if self.__medical_history:
            for x in self.__medical_history:
                print (f"- {x}")
        else:
            print ("No medical history found") 

class Doctor(User):
    def __init__(self, name, age, gender,doctor_id,specialty):
        super().__init__(name, age, gender)
        self.__doctor_id = doctor_id
        self.__specialty = specialty

    def set_doctor_id (self,doctor_id):
        self.__doctor_id = doctor_id    

    def set_specialty (self,specialty):
        self.__specialty = specialty  

    def get_doctor_id (self):
        return self.__doctor_id   
     
    def get_specialty (self):
        return self.__specialty 
     
    def display_info(self):
        print("🔹 Doctor Information:")
        print(f"Name: {self.get_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Gender: {self.get_gender()}")
        print(f"Doctor ID: {self.get_doctor_id()}")
        print(f"Specialty: {self.get_specialty()}")

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date_time):
        self.__appointment_id = appointment_id  # Encapsulation
        self.__patient = patient                # Object of class Patient
        self.__doctor = doctor                  # Object of class Doctor
        self.__date_time = date_time            

    def get_appointment_id(self):
        return self.__appointment_id

    def set_appointment_id(self, appointment_id):
        self.__appointment_id = appointment_id

    def get_patient(self):
        return self.__patient

    def set_patient(self, patient):
        self.__patient = patient

    def get_doctor(self):
        return self.__doctor

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def get_date_time(self):
        return self.__date_time

    def set_date_time(self, date_time):
        self.__date_time = date_time

    # --------- Summary Method ---------
    def get_summary(self):
        print("📅 Appointment Summary:")
        print(f"- Patient: {self.__patient.get_name()}")
        print(f"- Doctor: Dr. {self.__doctor.get_name()} ({self.__doctor.get_specialty()})")
        print(f"- Date & Time: {self.__date_time}")
