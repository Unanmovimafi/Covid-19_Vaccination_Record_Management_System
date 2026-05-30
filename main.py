#The username and password are 'Admin'

import datetime

def isVcValid(vc):
    if vc == "VC1" or vc == "VC2":
        return vc
    else:
        input("Invalid VC! Please either enter VC1 or VC2 only.(Press enter to continue)")
        return False

def isNameValid(name):
    if name.isupper() and len(name) >= 2:
        return name
    else:
        input("Invalid Name! Your name should all upper case and more than 2 character.(Press enter to continue)")
        return False

def isGenderValid(gender):
    if gender == "M" or gender == "F":
        return gender
    else:
        input("Invalid Gender! Please type M or F only.(Press enter to continue)")
        return False

def isIcNumberValid(ic):
    if ic.isnumeric() and len(ic) == 12:
        return ic
    else:
        input("Invalid IC Number! Your ic number should be all numbers and have 12 digits.(Press enter to continue)")
        return False

def isContact_numberValid(contact_number):
    if contact_number.isnumeric() and len(contact_number) in range(8, 11):
        return contact_number
    else:
        input("Invalid Contact Number! Your contact number should be all numbers and follow Malaysia phone number format.(Press enter to continue)")
        return False

def isEmailValid(email):
    if "@" in email and ".com" in email:
        if email.startswith("@") or email.count(" ") > 0:
            input("Invalid email format! Please type your correct email.(Press enter to continue)")
            return False
        else:
            return email
    else:
        input("Invalid email format! Please type your correct email.(Press enter to continue)")
        return False

def isHeightValid(height):
    if height.isnumeric():
        height = int(height)
        if height >= 100:
            return height
        else:
            input("Invalid Height! The minimum height is 100.(Press enter to continue)")
            return False
    else:
        input("Invalid Height! Please type your correct height in number and no need to type unit of measurement(cm/m).(Press enter to continue)")
        return False

def isWeightValid(weight):
    if weight.isnumeric():
        weight = int(weight)
        if weight >= 30:
            return weight
        else:
            input("Invalid Weight! The minimum weight is 30.(Press enter to continue)")
            return False
    else:
        input("Invalid Weight! Please type your correct weight in number and no need to type unit of measurement(kg).(Press enter to continue)")
        return False

def isMedical_optionValid(medical_option):
    if medical_option == "Y" or medical_option == "N":
        return medical_option
    else:
        input("Invalid Option! Please only type Y or N.(Press enter to continue)")
        return False

def isFirstGroupPrefer_vcValid(prefer_vc):
    if prefer_vc == "AF" or prefer_vc == "CZ" or prefer_vc == "DM":
        return prefer_vc
    else:
        input("Invalid Code!Your age only available for vaccine AF or CZ or DM only.(Press enter to continue)")
        return False

def isSecondGroupPrefer_vcValid(prefer_vc):
    if prefer_vc == "AF" or prefer_vc == "BV" or prefer_vc == "CZ" or prefer_vc == "DM" or prefer_vc == "EC":
        return prefer_vc
    else:
        input("Invalid Code! Please only type the vaccine code this vaccination centre have only.(Press enter to continue)")
        return False

def isThirdGroupPrefer_vcValid(prefer_vc):
    if prefer_vc == "AF" or prefer_vc == "BV" or prefer_vc == "DM" or prefer_vc == "EC":
        return prefer_vc
    else:
        input("Invalid Code! Your age only available for vaccine AF or BV or DN or EC only.(Press enter to continue)")
        return False

def isBirthdayValid(birthday):
    date_format = "%d/%m/%Y"
    try:
        datetime.datetime.strptime(birthday, date_format)
        return birthday
    except ValueError:
        input("Invalid Date Format!(Press enter to continue)")
        return False

def isUserOrPwdValid(user):
    if user.count(" ") > 0 or len(user) <=4:
        input("Your username or password should be more than 4 character and not consists of any empty spaces.(Press enter to continue)")
        return False
    else:
        return user

def calculate_age(birthdate):
    today = datetime.datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def age_and_vaccination(age):
    print("Based on your age: " + str(age))
    if age in range(12, 18):
        print("The vaccine your available for is:")
        print("AF(2 Dose)(2 weeks/14 days)")
        print("CZ(2 Dose)(3 weeks/21 days)")
        print("DM(2 Dose)(4 weeks/28 days)")
        return age

    elif age in range(18, 46):
        print("The vaccine your available for is:")
        print("AF(2 Dose)(2 weeks/14 days)")
        print("BV(2 Dose)(3 weeks/21 days)")
        print("CZ(2 Dose)(3 weeks/21 days)")
        print("DM(2 Dose)(4 weeks/28 days)")
        print("EC(1 Dose)")
        return age

    elif age > 45:
        print("The vaccine your available for is:")
        print("AF(2 Dose)(2 weeks/14 days)")
        print("BV(2 Dose)(3 weeks/21 days)")
        print("DM(2 Dose)(4 weeks/28 days)")
        print("EC(1 Dose)")
        return age

    else:
        input("Invalid Age. Your age is not suitable for any vaccine we have.(Press enter to continue)")
        return False

def patient_IDGenerator():
    f = open("patients.txt", "a")
    f.close()
    with open("patients.txt", "r") as file:
        counter = len(file.readlines()) + 1
    patient_id = f'{counter:05d}'
    patient_id = "PA" + patient_id
    return patient_id

def showInRegisterPatient(record):
    print("-----------------------------------------------------------------------------------------------------------")
    print("Patient's ID\t\t\t\t:", record[0])
    print("Patient's Vaccination Center:", record[1])
    print("Patient's Name\t\t\t\t:", record[2])
    if record[3] == "M":
        print("Patient's Gender\t\t\t: Male")
    elif record[3] == "F":
        print("Patient's Gender\t\t\t\t: Female")
    print("Patient's IC\t\t\t\t:", record[4])
    print("Patient's Contact Number\t:", record[5])
    print("Patient's Email Address\t\t:", record[6])
    print("Patient's Height\t\t\t:", record[7])
    print("Patient's Weight\t\t\t:", record[8])
    if record[9] == "N":
        print("Patient's Medical History\t: NONE")
    elif record[9] == "Y":
        print("Patient's Medical History\t:", record[10])
    print("Patient's Date of Birth\t\t:", record[11])
    print("Patient's Vaccine Choice\t:", record[12])
    print("----------------------------Above is your record. Please double check--------------------------------------")

def getPatientRecord(patient_id):
    counter = 0
    with open('patients.txt', 'r') as file:
        for lines in file:
            lines = lines.strip()
            line_array = lines.split(',')
            counter = counter + 1
            if line_array[0] == patient_id:
                return line_array, counter

def getVaccinationRecord(patient_id):
    counter = 0
    with open('vaccination.txt', 'r') as file:
        for lines in file:
            lines = lines.strip()
            line_array = lines.split(',')
            counter = counter + 1
            if line_array[0] == patient_id:
                return line_array, counter

def getAdminRecord(username):
    counter = 0
    with open('admin.txt', 'r') as fhand:
        for line in fhand:
            line = line.rstrip()
            line_array = line.rsplit(',')
            counter = counter + 1
            if line_array[0] == username:
                return line_array, counter

def getDoseDate_D1():
    today = datetime.datetime.today()
    date = today.strftime('%d/%m/%Y')
    return date

def getDoseDate_D2(vc):
    date = datetime.datetime.today()
    if vc == "AF":
        date = date + datetime.timedelta(days=14)
    elif vc == "BV" or vc == "CZ":
        date = date + datetime.timedelta(days=21)
    elif vc == "DM":
        date = date + datetime.timedelta(days=28)
    date = date.strftime("%d/%m/%Y")
    return date

def vaccinationStatusCheck(record):
    today = datetime.datetime.today()

    if record[1] == "D2":
        input("The patient already complete the vaccine in the past.(Press enter to continue)")
        return False
    elif record[1] == "D1":
        sec_date = datetime.datetime.strptime(record[4], '%d/%m/%Y')
        if sec_date <= today:
            return record
        else:
            input("The patient haven't reach his/her dose 2 appointment day yet.(Press enter to continue)")
            return False
    elif record[1] == "D0":
        return record

def vaccinationStatusChange(dose):
    new_status = []

    if dose[1] == "D0" and dose[2] == "EC":
        new_status = ["D2"]
    elif dose[1] == "D1":
        new_status = ["D2"]
    elif dose[1] == "D0":
        new_status = ["D1"]
    return new_status

def replaceRecord(file_name, line_num, text):
    line_num = int(line_num)
    line_num = line_num - 1
    with open(file_name, "r") as file:
        lines = file.readlines()
        lines[line_num] = text
    with open(file_name, "w") as file:
        file.writelines(lines)
        lines[line_num] = text

def receiveVaccine():
    print("-------------------------------------")
    patient_id = input("Enter Patient's ID(PAXXXXX):")
    if searchRecord(patient_id):
        showstatus(patient_id)
        print("-----Please let patient check if above is his/her correct record.------")
        vaccine_record = getVaccinationRecord(patient_id)[0]
        count_line = getVaccinationRecord(patient_id)[1]
        if vaccinationStatusCheck(vaccine_record):
            while True:
                opt = str.upper(input("Do the patient want to receive dose today?(Y/N)"))
                if opt == 'Y':
                    input("The patient's vaccination status has been change. Please proceed to take the patient to receive vaccine.(Press enter to continue)")
                    first_date = getDoseDate_D1()
                    sec_date = getDoseDate_D2(vaccine_record[2])
                    new_vaccine_status = vaccinationStatusChange(vaccine_record)

                    if vaccine_record[2] == "EC":
                        new_data = [vaccine_record[0], new_vaccine_status[0], vaccine_record[2], first_date]
                    elif new_vaccine_status[0] == "D2":
                        new_data = [vaccine_record[0], new_vaccine_status[0], vaccine_record[2], vaccine_record[3], vaccine_record[4]]
                    else:
                        new_data = [vaccine_record[0], new_vaccine_status[0], vaccine_record[2], first_date, sec_date]

                    if new_vaccine_status[0] == "D1":
                        input("Patient next appointment date is: "+ sec_date + "(Press enter to continue)")
                    elif new_vaccine_status[0] == "D2":
                        input("Patient have complete all vaccine.(Press enter to continue)")

                    new_record = ",".join(new_data) + "\n"
                    replaceRecord("vaccination.txt", count_line, new_record)
                    return patient_id
                elif opt == 'N':
                    return patient_id
                else:
                    input("Invalid Option! Please only type Y or N.")

def searchRecord(patient_id):
    if getPatientRecord(patient_id):
        record = getPatientRecord(patient_id)
        record = record[0]
        print("-------------------------------------")
        print("Patient's ID\t\t\t\t:", record[0])
        print("Patient's Vaccination Center:", record[1])
        print("Patient's Name\t\t\t\t:", record[2])
        if record[3] == "M":
            print("Patient's Gender\t\t\t: Male")
        elif record[3] == "F":
            print("Patient's Gender\t\t\t\t: Female")
        print("Patient's IC\t\t\t\t:", record[4])
        print("Patient's Contact Number\t:", record[5])
        print("Patient's Email Address\t\t:", record[6])
        print("Patient's Height\t\t\t:", record[7])
        print("Patient's Weight\t\t\t:", record[8])
        if record[9] == "N":
            print("Patient's Medical History\t: NONE")
        elif record[9] == "Y":
            print("Patient's Medical History\t:", record[10])
        print("Patient's Date of Birth\t\t:", record[11])
        print("Patient's Vaccine Choice\t:", record[12])
        print("-------------------------------------")
        return patient_id
    else:
        input("No Record Found. Either the record has been delete or wrong patient's ID.(Press enter to continue)")
        return False

def showstatus(patient_id):
    record = getVaccinationRecord(patient_id)[0]
    if record[2] == "AF" or record[2] == "BV" or record[2] == "CZ" or record[2] == "DM":
        print("Patient's Dosage Required\t\t\t: 2")
    elif record[2] == "EC":
        print("Patient's Dosage Required\t\t\t: 1")


    if record[1] == "D0":
        print("Patient's Vaccination status\t\t: NEW")
    elif record[1] == "D1":
        print("Patient's Vaccination status\t\t: COMPLETED-D1")
        print("Patient's First Dose Date\t\t\t:", record[3])
        print("Patient's Next Appointment Date\t\t:", record[4])
    elif record[1] == "D2" and record[2] == "EC":
        print("Patient's Vaccination status\t\t: COMPLETED")
        print("Patient's Dose Date\t\t\t\t\t:", record[3])
    elif record[1] == "D2":
        print("Patient's Vaccination status\t\t: COMPLETED")
        print("Patient's First Dose Date\t\t\t:", record[3])
        print("Patient's Second Dose Expected Date\t:", record[4])

def Modification():
    patient_id = input("Enter Patient's ID(PAXXXXX) to modify:")
    while True:
        if searchRecord(patient_id):
            print("----------Above Is Your Old Record---------")
            print("-------------------------------------------")
            print("Select any value to modify:")
            print("1. Vaccine Center")
            print("2. Name")
            print("3. Gender")
            print("4. IC Number")
            print("5. Contact Number")
            print("6. Email address")
            print("7. Height")
            print("8. Weight")
            print("9. Medical History")
            print("-------------------------------------------")
            print("Enter X or x to exit modify")
            print("-------------------------------------------")
            choice = input("Your choice:")
            record = getPatientRecord(patient_id)[0]
            count_line = getPatientRecord(patient_id)[1]
            if choice == "1":
                print("Old Vaccine Center:" + record[1])
                while True:
                    record[1] = input("New Vaccine Center:")
                    if isVcValid(record[1]):
                        break
            elif choice == "2":
                print("Old Name:" + record[2])
                while True:
                    record[2] = input("New Name:")
                    if isNameValid(record[2]):
                        break
            elif choice == "3":
                print("Old Gender:" + record[3])
                while True:
                    record[3] = input("New Gender:")
                    if isGenderValid(record[3]):
                        break
            elif choice == "4":
                print("Old IC Number:" + record[4])
                while True:
                    record[4] = input("New IC Number:")
                    if isIcNumberValid(record[4]):
                        break
            elif choice == "5":
                print("Old Contact Number:" + record[5])
                while True:
                    record[5] = input("New Contact Number:")
                    if isContact_numberValid(record[5]):
                        break
            elif choice == "6":
                print("Old Email Address:" + record[6])
                while True:
                    record[6] = input("New Email Address:")
                    if isEmailValid(record[6]):
                        break
            elif choice == "7":
                print("Old Height:" + record[7])
                while True:
                    record[7] = input("New Height:")
                    if isHeightValid(record[7]):
                        break
            elif choice == "8":
                print("Old Weight:" + record[8])
                while True:
                    record[8] = input("New Weight:")
                    if isWeightValid(record[8]):
                        break
            elif choice == "9":
                if record[9] == "Y":
                    print("Old Medical History:" + record[10])
                    record[10] = input("New Medical History:")
                elif record[9] == "N":
                    record[9] = "Y"
                    record[10] = input("New Medical History:")
            elif choice == "X" or choice == "x":
                return patient_id
            else:
                input("Invalid Option! Please only type number to choose.(Press enter to continue)")
                continue

            record = ",".join(record) + "\n"
            replaceRecord("patients.txt", count_line, record)
            input("Your change have successfully been saved.")
            return patient_id
        else:
            return patient_id

def deleteRecord():
    patient_id = input("Enter Patient's ID(PAXXXXX) to delete:")
    while True:
        print("--------------------------------------------------")
        if searchRecord(patient_id):
            print("--------------------------------------------------")
            showstatus(patient_id)
        else:
            return patient_id

        print("--------------------------------------------------")
        print("Are you sure your want to delete this record(Y/N):")
        print("--------------------------------------------------")
        opt = str.upper(input("Your choice:"))

        if opt == "Y":
            count_line = getPatientRecord(patient_id)[1]
            replaceRecord("patients.txt", count_line, "Deleted Record\n")
            replaceRecord("vaccination.txt", count_line, "Deleted Record\n")
            return patient_id
        elif opt == "N":
            return patient_id
        else:
            input("Invalid Option! Please only type Y or N.")

def ShowAllPatientsVaccinatedTodayOrAfter():
    counter = 0
    today = datetime.datetime.today()
    with open("vaccination.txt", "r") as file:
        for lines in file:
            lines = lines.strip()
            readlines = lines.split(',')
            if readlines[0] == "Deleted Record":
                continue
            if readlines[1] == "D1":
                sec_date = datetime.datetime.strptime(readlines[4], '%d/%m/%Y')
                if sec_date <= today:
                    patient_id = readlines[0]

                    with open("patients.txt", "r") as file2:
                        for line in file2:
                            line = line.strip()
                            list_of_line = line.split(",")
                            if list_of_line[0] == patient_id:
                                print("-------------------------------------------")
                                print("Patient's ID\t\t\t\t:", list_of_line[0])
                                print("Vaccination Center\t\t\t:", list_of_line[1])
                                print("Patient's Name\t\t\t\t:", list_of_line[2])
                                print("Patient's Vaccine\t\t\t:", list_of_line[12])
                                print("Patient's Second Dose Date\t:", readlines[4])
                                counter = counter + 1

        print("-------------------------------------------------")
        input("Total number of Patients are that may Vaccine Today or After are:" + str(counter) + "(Press enter to continue)")
        print("----------Redirecting Back To Home Page----------")

def ShowAllRegisteredPatients():
    counter = 0
    with open("patients.txt", "r") as file:
        for lines in file:
            lines = lines.strip()
            list_of_line = lines.split(",")
            if list_of_line[0] == "Deleted Record":
                continue
            print("-------------------------------------------")
            print("Patient's ID\t\t\t:", list_of_line[0])
            print("Vaccination Center\t\t:", list_of_line[1])
            print("Patient's Name\t\t\t:", list_of_line[2])
            print("Patient's Vaccine Choice:", list_of_line[12])
            counter = counter + 1
    print("-------------------------------------------")
    input("Total number of Registered Patients are:" + str(counter) + "(Press enter to continue)")

def ShowAllVaccinatedPatients(dose):
    counter = 0
    with open("vaccination.txt", "r") as file:
        for line in file:
            line = line.strip()
            readlines = line.split(',')
            if readlines[0] == "Deleted Record":
                continue
            if readlines[1] == dose:
                patient_id = readlines[0]
                with open("patients.txt", "r") as file2:
                    for lines in file2:
                        lines = lines.strip()
                        list_of_line = lines.split(",")
                        if list_of_line[0] == patient_id:
                            print("-------------------------------------------")
                            print("Patient's ID\t\t\t:", list_of_line[0])
                            print("Vaccination Center\t\t:", list_of_line[1])
                            print("Patient's Name\t\t\t:", list_of_line[2])
                            print("Patient's Vaccine Choice:", list_of_line[12])
                            counter = counter + 1

        print("-------------------------------------------")
        input("Total number of Patients are:" + str(counter) + "(Press enter to continue)")
        print("----------Redirecting Back To Home Page----------")

def vaccinationRecord(vaccine, status):
    count_vaccine = 0
    count_status = 0
    count_d = 0
    count_total = 0
    with open("vaccination.txt", "r") as file:
        for lines in file:
            lines = lines.strip()
            record = lines.split(',')
            if record[0] == "Deleted Record":
                continue
            count_total = count_total + 1
            if record[1] == status:
                count_status = count_status + 1
            if record[2] == vaccine:
                count_vaccine = count_vaccine + 1
            if record[1] == status and record[2] == vaccine:
                count_d = count_d + 1
    return count_vaccine, count_status, count_d, count_total

def printStatisticalInformatonByVaccine():
    print("----------------------------------------------------------------------")
    print("------------------------AF------BV------CZ-----DM------EC-----Total---")
    print("----------------------------------------------------------------------")
    print("Number of            |")
    print("peoples who are\t\t |\t" + str(vaccinationRecord("AF", "D0")[2]) + "\t\t" + str(vaccinationRecord("BV", "D0")[2]) + "\t\t"
                                    + str(vaccinationRecord("CZ", "D0")[2]) + "\t\t" + str(vaccinationRecord("DM", "D0")[2]) + "\t\t"
                                    + str(vaccinationRecord("EC", "D0")[2]) + "\t\t"+ str(vaccinationRecord("", "D0")[1]))
    print("waiting for dose 1   |")
    print("----------------------------------------------------------------------")
    print("Number of            |")
    print("peoples who are\t\t |\t" + str(vaccinationRecord("AF", "D1")[2]) + "\t\t" + str(vaccinationRecord("BV", "D1")[2]) + "\t\t"
                                    + str(vaccinationRecord("CZ", "D1")[2]) + "\t\t" + str(vaccinationRecord("DM", "D1")[2])+"\t\t"
                                    + str(vaccinationRecord("EC", "D1")[2]) + "\t\t" + str(vaccinationRecord("", "D1")[1]))
    print("waiting for dose 2   |  ")
    print("----------------------------------------------------------------------")
    print("Number of            | ")
    print("peoples who have\t |\t" + str(vaccinationRecord("AF", "D2")[2]) + "\t\t" + str(vaccinationRecord("BV", "D2")[2]) + "\t\t"
                                    + str(vaccinationRecord("CZ", "D2")[2]) + "\t\t" + str(vaccinationRecord("DM", "D2")[2]) + "\t\t"
                                    + str(vaccinationRecord("EC", "D2")[2]) + "\t\t" + str(vaccinationRecord("", "D2")[1]))
    print("completed vaccination|")
    print("----------------------------------------------------------------------")
    print("Total\t\t\t\t |\t " + str(vaccinationRecord("AF","")[0])+"\t\t" + str(vaccinationRecord("BV", "")[0]) + "\t\t"
                                + str(vaccinationRecord("CZ", "")[0]) + "\t\t" + str(vaccinationRecord("DM", "")[0]) + "\t\t"
                                + str(vaccinationRecord("EC", "")[0]) + "\t\t"+ str(vaccinationRecord("", "")[3]))
    print("----------------------------------------------------------------------")
    input("(Press enter to continue)")
    print("----------Redirecting Back To Home Page----------")

def VaccinationStatusRecord(vc, status):
    count_total_vc = 0
    count_d = 0
    count_total = 0
    with open("patients.txt", "r") as file:
        for lines in file:
            lines = lines.strip()
            record = lines.split(',')
            if record[0] == "Deleted Record":
                continue
            count_total = count_total + 1
            if record[1] == vc:
                count_total_vc = count_total_vc +1
                with open("vaccination.txt", "r") as file:
                    for line in file:
                        line = line.strip()
                        record_vc = line.split(',')
                        if record[0] == record_vc[0]:
                            if record_vc[1] == status:
                                count_d = count_d + 1
    return count_d, count_total_vc, count_total

def printStatisticalInformatonByVC():
    print("--------------------------------------------------------------------------------------")
    print("------------------------Vaccination Centre 1------Vaccination Centre 2--------Total---")
    print("--------------------------------------------------------------------------------------")
    print("Number of            |")
    print("peoples who are\t\t |\t\t\t" + str(VaccinationStatusRecord("VC1", "D0")[0])+"\t\t\t\t\t\t\t"
                                        + str(VaccinationStatusRecord("VC2", "D0")[0]) + "\t\t\t\t\t"
                                        + str(vaccinationRecord("", "D0")[1]))
    print("waiting for dose 1   |")
    print("--------------------------------------------------------------------------------------")
    print("Number of            |")
    print("peoples who are\t\t |\t\t\t" + str(VaccinationStatusRecord("VC1", "D1")[0]) + "\t\t\t\t\t\t\t"
                                        + str(VaccinationStatusRecord("VC2", "D0")[0]) + "\t\t\t\t\t"
                                        + str(vaccinationRecord("", "D1")[1]))
    print("waiting for dose 2   |  ")
    print("--------------------------------------------------------------------------------------")
    print("Number of            | ")
    print("peoples who have\t |\t\t\t" + str(VaccinationStatusRecord("VC1", "D2")[0])+"\t\t\t\t\t\t\t"
                                        + str(VaccinationStatusRecord("VC2", "D2")[0]) + "\t\t\t\t\t"
                                        + str(vaccinationRecord("", "D2")[1]))
    print("completed vaccination|")
    print("--------------------------------------------------------------------------------------")
    print("Total\t\t\t\t |\t\t\t "+ str(VaccinationStatusRecord("VC1", "")[1]) + "\t\t\t\t\t\t\t"
                                    + str(VaccinationStatusRecord("VC2", "")[1]) +"\t\t\t\t\t"
                                    + str(VaccinationStatusRecord("", "")[2]))
    print("--------------------------------------------------------------------------------------")
    input("(Press enter to continue)")
    print("----------Redirecting Back To Home Page----------")

def printAdmin():
    with open("admin.txt","r") as file:
        for lines in file:
            lines = lines.strip()
            readlines = lines.split(",")
            print("-------------------------")
            print("Username:", readlines[0])
        print("-------------------------")

def registerAdmin():
    new_admin = []
    new_username = input("New Admin Username:")
    if getAdminRecord(new_username):
        input("Same Username Exist. Please try a new username.(Press enter to continue)")
    elif isUserOrPwdValid(new_username):
        new_password = input("New Admin Password:")
        confirm_password = input("Confirm your password:")
        if confirm_password != new_password:
            input("The password not matched!(Press enter to continue)")
        elif isUserOrPwdValid(new_password):
            new_admin.append(new_username)
            new_admin.append(new_password)
            with open("admin.txt","a") as file:
                file.write(",".join(new_admin) + "\n")
            input("Your user is created successfully!(Press enter to continue)")

def changePassword():
    printAdmin()
    print("Which username you want to change password?")
    username = input("Username:")
    if getAdminRecord(username):
        old_user = getAdminRecord(username)[0]
        counter = getAdminRecord(username)[1]
        print("---------------------------------------------------------")
        print("Please type  old password of this username.")
        print("----------------------------------------------------------")
        print("Username:", old_user[0])
        psw = input("Old Password:")
        if psw == old_user[1]:
            new_password = input("New Password:")
            old_user[1] = input("Confirm Password:")
            if new_password == old_user[1]:
                if isUserOrPwdValid(new_password):
                    line_array = ",".join(old_user) + "\n"
                    replaceRecord("admin.txt", counter, line_array)
                    input("Your password successfully change!(Press enter to continue)")
            else:
                input("Your password is not matched!(Press enter to continue)")
        else:
            input("Wrong Password!(Press enter to continue)")
    else:
        input("No username found(Press enter to continue)")

def deleteAdmin():
    printAdmin()
    print("!!!Warning!!! Username Admin is not deletable! Attempt to do so may result in cannot open the program!")
    print("Which username you which to delete?")
    username = input("Username:")
    if getAdminRecord(username):
        old_user = getAdminRecord(username)[0]
        counter = getAdminRecord(username)[1]
        print("---------------------------------------------------------")
        print("Please type password of this username to delete this admin.")
        print("----------------------------------------------------------")
        print("Username:", username)
        psw = input("Password:")
        if psw == old_user[1]:
            replaceRecord("admin.txt", counter, "")
            input("Username successfully delete.(Press enter to continue)")
        else:
            input("Wrong Password!(Press enter to continue)")
    else:
        input("No username found!(Press enter to continue)")

def Login_Page():
    print("--------------------------------------")
    print("-------------LOGIN PAGE---------------")
    print("--------------------------------------")
    username = input("Username:")
    password = input("Password:")
    if getAdminRecord(username):
        record = getAdminRecord(username)[0]
        if username == record[0] and password == record[1]:
            print("You successfully login!")
            print("-----Redirecting To Home Page-----")
            Home_Page()
            return username
        else:
            input("Invalid username or password!(Press enter to continue)")
    else:
        input("Invalid username or password!(Press enter to continue)")

def Home_Page():
    while True:
        print("-------------------------------------")
        print("-------------HOME PAGE---------------")
        print("-------------------------------------")
        print("1. New Patient Registration")
        print("2. Vaccine Administration(For admin only)")
        print("3. Exit")
        print("-------------------------------------")
        opt = input("Your choice:")
        if opt == "1":
            New_Patient_Registration_Page()
        elif opt == "2":
            username = input("Username:")
            password = input("Password:")
            if getAdminRecord(username):
                record = getAdminRecord(username)[0]
                if username == record[0] and password == record[1]:
                    print("You successfully login!")
                    print("---Redirecting To Vaccine Administration Page---")
                    Vaccine_Administration_Page()
                else:
                    input("Invalid username or password!(Press enter to continue)")
            else:
                input("Invalid username or password!(Press enter to continue)")
        elif opt == "3":
            return opt
        else:
            input("Invalid Option! Please only type number to choose.(Press enter to continue)")

def New_Patient_Registration_Page():
    medical_history = ""
    pationRegistrationRecord = []
    vaccinationRecord = []
    print("-----------------------------------------------------------------------------------------------------------")
    print("-------------------------------------NEW PATIENT REGISTRATION PAGE-----------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------IMPORTANT NOTE----------------------------------------------------")
    print("Welcome to New Patient Registration.")
    print("You will answer a series of following questions.")
    print("Please answer the following questions honestly, "
          "person failed to do it may result in unable to register successfully.")
    print("Please note that all questions is compulsory to answer.")
    print("Before the registration start. Please notice that only people age 12 above only can take vaccine")
    print("You can go back to previous question at any questio by enter single B or b.")
    while True:
        print("-----------------------------------------------------------------------------------------------------------")
        print("Are you sure you want to continue?(Y/N)")
        print("-----------------------------------------------------------------------------------------------------------")
        opt = str.upper(input("Your Choice:"))

        if opt == "Y":

            while True:
                print("-------------------------------------------Question 1 of 12-----------------------------------------------------")
                print("Please select your current vaccination centres(VC1/VC2):")
                vc = str.upper(input("Answer:"))
                if vc == "B":
                    break
                elif isVcValid(vc):
                    while True:
                        print("-------------------------------------------Question 2 of 12-----------------------------------------------------")
                        print("Please enter your name(All upper case as per ic):")
                        name = input("Answer:")
                        if name == "B" or name == "b":
                            break
                        elif isNameValid(name):
                            while True:
                                print("-------------------------------------------Question 3 of 12-----------------------------------------------------")
                                print("Please enter your Gender(M for male; F for female).:")
                                gender = str.upper(input("Answer:"))
                                if gender == "B":
                                    break
                                elif isGenderValid(gender):
                                    while True:
                                        print("-------------------------------------------Question 4 of 12-----------------------------------------------------")
                                        print("Please enter your identity card(IC) number without '-':")
                                        ic = input("Answer:")
                                        if ic == "B" or ic == "b":
                                            break
                                        elif isIcNumberValid(ic):
                                            while True:
                                                print("-------------------------------------------Question 5 of 12-----------------------------------------------------")
                                                print("Please enter your contact number(eg: 0123456789):")
                                                contact_number = input("Answer:")
                                                if contact_number == "B" or contact_number == "b":
                                                    break
                                                elif isContact_numberValid(contact_number):
                                                    while True:
                                                        print("-------------------------------------------Question 6 of 12-----------------------------------------------------")
                                                        print("Please enter your email address:")
                                                        email = str.lower(input("Answer:"))
                                                        if email == "b":
                                                            break
                                                        elif isEmailValid(email):
                                                            while True:
                                                                print("-------------------------------------------Question 7 of 12-----------------------------------------------------")
                                                                print("Please enter your height in centimeters(No need to type cm):")
                                                                height = input("Answer:")
                                                                if height == "B" or height == "b":
                                                                    break
                                                                elif isHeightValid(height):
                                                                    while True:
                                                                        print("-------------------------------------------Question 8 of 12-----------------------------------------------------")
                                                                        print("Please enter your weight(No need to type kg):")
                                                                        weight = input("Answer:")
                                                                        if weight == "B" or weight == "b":
                                                                            break
                                                                        elif isWeightValid(weight):
                                                                            while True:
                                                                                print("-------------------------------------------Question 9 of 12-----------------------------------------------------")
                                                                                print("Do you have any medical history(Y/N):")
                                                                                medical_option = str.upper(input("Answer:"))
                                                                                if medical_option == "B":
                                                                                    break
                                                                                elif isMedical_optionValid(medical_option):
                                                                                    if medical_option == "Y":
                                                                                        print("-------------------------------------------Question 10 of 12-----------------------------------------------------")
                                                                                        print("Please enter your details on your medical history:")
                                                                                        medical_history = input("Answer:")
                                                                                        if medical_history == "B" or medical_history == "b":
                                                                                            continue
                                                                                else:
                                                                                    continue

                                                                                while True:
                                                                                    print("-------------------------------------------Question 11 of 12-----------------------------------------------------")
                                                                                    print("Please enter your birthday(dd/mm/yyyy):")
                                                                                    birthday = input("Answer:")
                                                                                    if birthday == "B" or birthday == "b":
                                                                                        medical_history = ""
                                                                                        break
                                                                                    elif isBirthdayValid(birthday):
                                                                                        date_birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
                                                                                        age = calculate_age(date_birthday)
                                                                                        while True:
                                                                                            if age_and_vaccination(age):
                                                                                                if age >= 12 and age < 18:
                                                                                                    print("Please select your preference vaccine(AF/CZ/DM):")
                                                                                                    prefer_vc = str.upper(input("Answer:"))
                                                                                                    if prefer_vc == "B":
                                                                                                        break
                                                                                                    elif isFirstGroupPrefer_vcValid(prefer_vc):
                                                                                                        pass
                                                                                                    else:
                                                                                                        continue

                                                                                                elif age >= 18 and age <= 45:
                                                                                                    print("Please select your preference vaccine(AF/BV/CZ/DM/EC):")
                                                                                                    prefer_vc = str.upper(input("Answer:"))
                                                                                                    if prefer_vc == "B":
                                                                                                        break
                                                                                                    elif isSecondGroupPrefer_vcValid(prefer_vc):
                                                                                                        pass
                                                                                                    else:
                                                                                                        continue

                                                                                                elif age > 45:
                                                                                                    print("Please select your preference vaccine(AF/BV/DM/EC):")
                                                                                                    prefer_vc = str.upper(input("Answer:"))
                                                                                                    if prefer_vc == "B":
                                                                                                        break
                                                                                                    elif isThirdGroupPrefer_vcValid(prefer_vc):
                                                                                                        pass
                                                                                                    else:
                                                                                                        continue
                                                                                                Dose = "D0"
                                                                                                patient_id = patient_IDGenerator()


                                                                                                pationRegistrationRecord.append(patient_id)
                                                                                                pationRegistrationRecord.append(vc)
                                                                                                pationRegistrationRecord.append(name)
                                                                                                pationRegistrationRecord.append(gender)
                                                                                                pationRegistrationRecord.append(ic)
                                                                                                pationRegistrationRecord.append(contact_number)
                                                                                                pationRegistrationRecord.append(email)
                                                                                                pationRegistrationRecord.append(height)
                                                                                                pationRegistrationRecord.append(weight)
                                                                                                pationRegistrationRecord.append(medical_option)
                                                                                                pationRegistrationRecord.append(medical_history)
                                                                                                pationRegistrationRecord.append(birthday)
                                                                                                pationRegistrationRecord.append(prefer_vc)

                                                                                                vaccinationRecord.append(patient_id)
                                                                                                vaccinationRecord.append(Dose)
                                                                                                vaccinationRecord.append(prefer_vc)

                                                                                                showInRegisterPatient(pationRegistrationRecord)
                                                                                                while True:
                                                                                                    print("(Are you sure want to register.Y for yes; N for exit reigtsration; B for back)")
                                                                                                    cho = str.upper(input("Your choice:"))
                                                                                                    if cho == "Y":
                                                                                                        with open("patients.txt", "a") as file:
                                                                                                            file.write(",".join(pationRegistrationRecord) + "\n")

                                                                                                        with open("vaccination.txt", "a") as file:
                                                                                                            file.write(",".join(vaccinationRecord) + "\n")
                                                                                                        input("You successfully register! Please notes that your patient id is '" + patient_id + "(Press enter to continue)")
                                                                                                        print("----------Redirecting Back To Home Page----------")
                                                                                                        return opt
                                                                                                    elif cho == "N":
                                                                                                        return opt
                                                                                                    elif cho == "B":
                                                                                                        break
                                                                                                    else:
                                                                                                        input("Invalid option! Please only type Y or N or B.")
                                                                                            else:
                                                                                                break
        elif opt == "N":
            return opt
        else:
            print("Invalid Option! Please only type Y or N.")

def Vaccine_Administration_Page():
    while True:
        print("-------------------------------------")
        print("-----VACCINE ADMINISTRATION PAGE-----")
        print("-------------------------------------")
        print("1. Receive Vaccine")
        print("2. Search or Edit Patient's Record")
        print("3. List Record")
        print("4. Admin Menu")
        print("5. Back")
        print("-------------------------------------")
        opt = input("Your choice:")
        if opt == "1":
            Patient_Status_Page()
        elif opt == "2":
            Search_Edit_Patient_Page()
        elif opt == "3":
            List_Record_Page()
        elif opt == "4":
            Admin_Function_Page()
        elif opt == "5":
            return opt
        else:
            input("Invalid Option! Please only type number to choose.(Press enter to continue)")

def Patient_Status_Page():
    while True:
        print("-------------------------------------")
        print("--------Patient's Status Page--------")
        print("-------------------------------------")
        print("1. Receive dose 1 or dose 2")
        print("2. New patient")
        print("3. Back")
        print("-------------------------------------")
        opt = input("Your Choice:")
        if opt == '1':
            receiveVaccine()
        elif opt == '2':
            New_Patient_Registration_Page()
        elif opt == '3':
            return opt
        else:
            input("Invalid! Please enter correctly.(Press enter to continue)")

def Search_Edit_Patient_Page():
    while True:
        print("-------------------------------------")
        print("--Search/Edit Patient's Record Page--")
        print("-------------------------------------")
        print("1. Search Patient's Record")
        print("2. Edit Patient's Record")
        print("3. Delete Patient's Record")
        print("4. Back")
        print("-------------------------------------")
        opt = input("Your choice:")
        if opt == "1":
            patient_id = input("Enter Patient's ID(PAXXXXX):")
            if searchRecord(patient_id):
                showstatus(patient_id)
                input("Above is the record you search.(Press enter to continue)")
        elif opt == "2":
            Modification()
        elif opt == "3":
            deleteRecord()
        elif opt == "4":
            return opt
        else:
            input("Invalid Option! Please only type number to choose.(Press enter to continue)")

def List_Record_Page():
    while True:
        print("-----------------------------------------------------------------------------------------")
        print("--------------------------------List Patients Record Page--------------------------------")
        print("-----------------------------------------------------------------------------------------")
        print("1. List All Patients that may Vaccine Today or After")
        print("2. List All Registered Patients")
        print("3. List All Fully Vaccinated Patients")
        print("4. List All In-half vaccinated Patients(Patients who waiting dose 2)")
        print("5. List All No vaccinated Patients(Patients who waiting dose 1)")
        print("6. Show Number of Patients by Vaccination Centre")
        print("7. Show Number of Patients by Vaccine")
        print("8. Back to Home Page")
        print("-----------------------------------------------------------------------------------------")
        opt = input("Your choice:")
        if opt == "1":
            ShowAllPatientsVaccinatedTodayOrAfter()
        elif opt == "2":
            ShowAllRegisteredPatients()
        elif opt == "3":
            ShowAllVaccinatedPatients("D2")
        elif opt == "4":
            ShowAllVaccinatedPatients("D1")
        elif opt == "5":
            ShowAllVaccinatedPatients("D0")
        elif opt == "6":
            printStatisticalInformatonByVC()
        elif opt == "7":
            printStatisticalInformatonByVaccine()
        elif opt == "8":
            return opt
        else:
            input("Invalid Option! Please only type number to choose.(Press enter to continue)")

def Admin_Function_Page():
    while True:
        print("-------------------------------------")
        print("------------Admin Menu Page----------")
        print("-------------------------------------")
        print("1. Register New Admin")
        print("2. Change Password")
        print("3. Delete Admin")
        print("4. Back")
        print("-------------------------------------")
        opt = input("Your choice:")
        if opt == "1":
            registerAdmin()
        elif opt == "2":
            changePassword()
        elif opt == "3":
            deleteAdmin()
        elif opt == "4":
            return opt
        else:
            print("-----------------------------------------------------------------------------------------")
            input("Invalid Option! Please only type number to choose.(Press enter to continue)")

Login_Page()