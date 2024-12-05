# If  else looping
patient_name = input('Enter patient Name: ')
patient_age = int(input('Enter patient Age: '))
patient_gender = input('Enter patient Gender (F/M): ')
pat_ins = input('Does patient have Insurance (Y/N)? ')
new_patient = input('First time to this Hospital (Y/N)? ')
#  Comparision Operators
if new_patient.upper() == 'Y':
    print(f'{patient_name.title()} is a New Patient')
else:
    print(f'{patient_name.title()} is an Old Patient')

if len(patient_name) <= 2:
    print('Patient Name should be minimum 3 characters')
elif len(patient_name) >= 20:
    print('Patient Name should not exceed 20 characters')
else:
    print('Welcome to HH')
#  Logical Operators
if patient_age <= 14 and (patient_gender.upper() == 'FEMALE' or patient_gender.upper() == 'F'):
    print('Patient is a Female and a Minor')
elif patient_age <= 14 and (patient_gender.upper() == 'MALE' or patient_gender.upper() == 'M'):
    print('Patient is a Male and a Minor')
elif patient_age >= 60:
    print(f'{patient_name.title()} is a Senior Citizen')
elif 14 <= patient_age <= 60:
    print(f'{patient_name} is an Adult')
elif patient_age == 0 or patient_gender == ' ':
    print('Patient Age or Gender info is missing or Incorrect')
treat_cost = 25000
if pat_ins.upper() != 'Y':
    print(f'Treatment would cost {(treat_cost / 100) * 30}')
else:
    print(f'Treatment would cost {(treat_cost / 100) * 10}')
