# TO ADD ADMINISTRATIVE OFFICER AND DOCTOR
print("1.REGISTER PATIENT")
print("2.record his complains and preliminary diagnosis")
print("3.ATTACH LAB REPORTS")
print("4.COMPLETE TREATMENT")
print("5.IF THE PATIENT COMES AGAIN VIEW THE TREATMENT HISTORY WITH THEIR FILES ACCORDINGLY")
print("ROLES:ADMINS CAN CREATE A PATIENT AND ASSIGN IT TO A DOCTOR")
print("ONLY DOCTOR CAN INCLUDE:patient complaints and diagnostics,SCAN INFO")
print("ONLY DOCTORS AND LAB TECHNICIANS CAN UPLOAD SCAN REPORTS")
while True :
    print("NOTE : Everything should be inputed in caps")
    print("1. ADMINISTRATIVE OFFICER" )
    print("2. DOCTOR")
    print("3. EXIT")
    z = {"T_01" : "SRIVATSSEN","T_02" : "THARUN"}
    y = {"SRIVATSSEN" : "T_01","THARUN" : "T_02"}
    z1 = z.get ("T_01")
    z2 = z.get ("T_02")
    y1 = y.get ("SRIVATSSEN")
    y2 = y.get ("THARUN")
    a = int(input("ENTER CHOICE (1,2 OR 3) : " )) # TO PROVE ARE YOU A DOCTOR OR A ADMINISTRATIVE OFFICER
    if a == 1 :
        print ("**********WELCOME ADMINISTRATIVE OFFICER.**********") # 3 ATTEMPTS TO LOGIN USING YOUR USERNAME AND PASSWORD
        for i in range (3) :
            a1 = input("ENTER USERNAME : ")
            if a1  :
                pass
            a2 = input("ENTER PASSWORD : ")
            if z1 == a1 and a2 == y1 :
                print ("LOADING....")
                print ("ACCESS CODE ACCEPTED")
                break
            elif z2 == a1 and a2 == y2 :
                print ("LOADING....")
                print ("ACCESS CODE ACCEPTED")
                break
            else :
                print ("INVALID USERNAME OR PASSWORD")
        if i==2:
            break
        else:
            DE = input("ENTER WHAT DO YOU WANT,PATIENT DETAILS OR DOCTOR DETAILS  :").upper()
            if DE == "DOCTOR":
                n = int(input("HOW MANY DOCTORS DO YOU WANT TO ADD ? :"))  # NUMBER OF DOCTOR'S
                d = []
                for j in range(n):
                    u = []
                    u.append(input("ENTER NAME OF THE DOCTOR : "))
                    u.append(input("ENTER TITLE OF THE DOCTOR (RADIOLOGIST/CARDIOLOGIST/PATHOLOGIST) : "))
                    u.append(input("ENTER GENDER OF THE DOCTOR (M - MALE / F - FEMALE) : "))
                    u.append(input("ENTER D.O.B OF THE DOCTOR (dd/mm/yyyy) : "))
                    u.append(input("ENTER QUALIFICATION OF THE DOCTOR (PG,M.S,PH.D) : "))
                    u.append(input("ENTER MEDICAL LISCENSE NUMBER OF THE DOCTOR : "))
                    u.append(input("ENTER  SCAN CENTRE ID OF THE DOCTOR : "))
                    u.append(input("ENTER ADDRESS OF THE DOCTOR : "))
                    u.append(input("ENTER CONTACT NUMBER OF THE DOCTOR (+91 **********) : "))
                    u.append(input("EMAIL ID OF THE DOCTOR (*************@GMAIL.COM) : "))
                    d.append(u)
                print(d)
                while True:
                    print("**********1. SEARCH DETAILS ON DOCTOR***************")
                    print("**********2. MODIFY DETAILS OF THE DOCTOR***********")
                    print("**********3. ADD NEW TITLE'S FOR THE DOCTOR**********")
                    print("**********************4. EXIT*************************")
                    a3 = int(input("ENTER CHOICE(1,2,3 OR 4) : "))  # ADDING DOCTOR'S
                    if a3 == 1:
                        while True:
                            print("1. SEARCHING THROUGH MEDICAL LICENSE NUMBER AND  SCAN CENTRE-ID")
                            print("2. SEARCHING THROUGH NAME AND CONTACT NUMBER")
                            print("3. EXIT")
                            v = int(input("ENTER CHOICE (1,2 OR 3) : "))
                            if v == 1:
                                h = input("ENTER MEDICAL LICENSE NUMBER OF THE DOCTOR : ")
                                w = input("ENTER  SCAN CENTRE ID OF THE DOCTOR : ")
                                for t in d:
                                    if h == t[5] and w == t[6]:
                                        print(t)
                                        break
                                    elif h == t[5] and w != t[6]:
                                        print("========THE SCAN CENTRE ID IS NOT IN OUR DATABASE========")
                                        break
                                    elif w == t[6] and h != t[5]:
                                        print("========THE MEDICAL LICENSE NUMBER IS NOT IN OUR DATABASE========")
                                        break
                                else:
                                    print(
                                        "========BOTH THE MEDICAL LICENSE NUMBER AND SCAN CENTRE ID IS NOT IN OUR DATABASE========")
                                    break
                            elif v == 2:
                                m = input("ENTER NAME OF THE DOCTOR : ")
                                o = input("ENTER CONTACT NUMBER OF THE DOCTOR : ")
                                for p in d:
                                    if m == p[0] and o == p[8]:
                                        print(p)
                                        break
                                    elif m == p[0] and o != p[8]:
                                        print(
                                            "========THE NAME OF THE DOCTOR IS CORRECT BUT CONTACT NO. IS NOT IN OUR DATABASE :(========")
                                        break
                                    elif o == p[8] and m != p[0]:
                                        print(
                                            "========THE CONTACT NO. IS IN OUR DATABASE BUT NAME IS NOT IN THE DATABASE :(========")
                                        break
                                else:
                                    print("========BOTH THE NAME AND CONTACT NO. IS NOT IN OUR DATABASE ;( ========")
                                    break
                            else:
                                break
                    elif a3 == 2:
                        while True:
                            print("1. NAME")
                            print("2. TITLE")
                            print("3. GENDER")
                            print("4. D.O.B")
                            print("5. QUALIFICATION")
                            print("6. MEDICAL LICENSE NUMBER")
                            print("7. TERESA SCAN CENTRE-ID")
                            print("8. ADDRESS")
                            print("9. CONTACT NUMBER")
                            print("10. EMAIL ID")
                            print("11. EXIT")
                            l = int(input("ENTER CHOICE (1,2,3,4,5,6,7,8,9,10 OR 11) : "))
                            if l == 1:
                                h1 = input("ENTER THE MODIFIED NAME : ")
                                h2 = input("ENTER THE CURRENT NAME : ")
                                for t1 in d:
                                    if h2 == t1[0]:
                                        t1.pop(0)
                                        t1.insert(0, h1)
                                        print(t1)
                                        break
                                else:
                                    print("========THE NAME YOU WANTED TO MODIFY IS NOT IN OUR DATABASE:========")
                                    break
                            elif l == 2:
                                h3 = input("ENTER THE MODIFIED TITLE : ")
                                h4 = input("ENTER THE CURRENT TITLE : ")
                                for t2 in d:
                                    if h4 == t2[1]:
                                        t2.pop(1)
                                        t2.insert(1, h3)
                                        print(t2)
                                        break
                                else:
                                    print("========THE TITLE YOU WANTED TO MODIFY IS NOT IN OUR DATABASE ;(======== ")
                                    break
                            elif l == 3:
                                h5 = input("ENTER THE MODIFIED GENDER : ")
                                h6 = input("ENTER THE CURRENT GENDER : ")
                                for t3 in d:
                                    if h6 == t3[2]:
                                        t3.pop(2)
                                        t3.insert(2, h5)
                                        print(t3)
                                        break
                                else:
                                    print("========THE GENDER YOU WANTED TO MODIFY IS NOT IN OUR DATABASE ;(========")
                                    break
                            elif l == 4:
                                h7 = input("ENTER THE MODIFIED D.O.B : ")
                                h8 = input("ENTER THE CURRENT D.O.B : ")
                                for t4 in d:
                                    if h8 == t4[3]:
                                        t4.pop(3)
                                        t4.insert(3, h7)
                                        print(t4)
                                        break
                                else:
                                    print("========THE DOB YOU WANTED TO MODIFY IS NOT IN OUR DATABASE ;(========")
                                    break
                            elif l == 5:
                                h9 = input("ENTER THE MODIFIED QUALIFICATION : ")
                                h10 = input("ENTER THE CURRENT QUALIFICATION : ")
                                for t5 in d:
                                    if h10 == t5[4]:
                                        t5.pop(4)
                                        t5.insert(4, h9)
                                        print(t5)
                                        break
                                else:
                                    print("========THE QUALIFICATION OF THE DOCTOR IS NOT IN OUR DATABASE:(========")
                                    break
                            elif l == 6:
                                h11 = input("ENTER THE MODIFIED MEDICAL LISCENSE NUMBER : ")
                                h12 = input("ENTER THE CURRENT MEDICAL LISCENSE NUMBER : ")
                                for t6 in d:
                                    if h12 == t6[5]:
                                        t6.pop(5)
                                        t6.insert(5, h11)
                                        print(t6)
                                        break
                                else:
                                    print(
                                        "========THE MEDICAL LISCENSE NUMBER YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                    break
                            elif l == 7:
                                h13 = input("ENTER THE MODIFIED TERESA SCAN CENTRE ID : ")
                                h14 = input("ENTER THE CURRENT TERESA SCAN CENTRE ID : ")
                                for t7 in d:
                                    if h14 == t7[6]:
                                        t7.pop(6)
                                        t7.insert(6, h13)
                                        print(t7)
                                        break
                                else:
                                    print("========THE SCAN CENTRE ID  IS NOT IN OUR DATABASE :(========")
                                    break
                            elif l == 8:
                                h15 = input("ENTER THE MODIFIED ADDRESS : ")
                                h16 = input("ENTER THE CURRENT ADDRESS : ")
                                for t8 in d:
                                    if h16 == t8[7]:
                                        t8.pop(7)
                                        t8.insert(7, h15)
                                        print(t8)
                                        break
                                else:
                                    print("========THE ADDRESS YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                    break
                            elif l == 9:
                                h17 = input("ENTER THE MODIFIED CONTACT NUMBER : ")
                                h18 = input("ENTER THE CURRENT CONTACT NUMBER : ")
                                for t9 in d:
                                    if h18 == t9[8]:
                                        t9.pop(8)
                                        t9.insert(8, h17)
                                        print(t9)
                                        break
                                else:
                                    print(
                                        "========THE CONTACT NO. YOU WANTED TO MODIFY IS NOT IN OUR DATABASE:(========")
                                    break
                            elif l == 10:
                                h19 = input("ENTER THE MODIFIED EMAIL ID : ")
                                h20 = input("ENTER THE CURRENT EMAIL ID : ")
                                for t10 in d:
                                    if h20 == t10[9]:
                                        t10.pop(9)
                                        t10.insert(9, h19)
                                        print(t10)
                                        break
                                else:
                                    print("=========THE EMAIL ID IS NOT IN OUR DATABASE:(======== ")
                            else:
                                break
                    elif a3 == 3:
                        g2 = input("ENTER CURRENT TITLE : ")
                        g3 = []
                        g4 = input("ENTER THE SCAN CENTRE ID : ")
                        j3 = int(input("HOW MANY TITLE'S DO YOU WANT TO ADD ? : "))
                        for j in range(j3):
                            g1 = input("ENTER NEW TITLE : ").upper()
                            g3.append(g1)
                        for f1 in d:
                            if g2 == f1[1] and g4 == f1[6]:
                                g3.append(g2)
                                f1.pop(1)
                                f1.insert(1, g3)
                                print(d)
                                break
                        else:
                            print("========THE CURRENT TITLE OR SCAN CENTRE ID IS NOT IN OUR DATABASE:(========")
                    else:
                        break
            elif DE == "PATIENT":
                L2 = int(input("HOW MANY PATIENT'S DO YOU WANT TO ADD ? :"))
                L3 = []
                for j in range(L2):
                    L4 = []
                    L4.append(input("ENTER REGISTRATION NUMBER OF THE PATIENT (RE-********) : "))
                    L4.append(input("ENTER REGISTRATION DATE OF THE PATIENT (dd/mm/yyyy) : "))
                    L4.append(input("ENTER NAME OF THE PATIENT : "))
                    L4.append(input("ENTER GENDER OF THE PATIENT (M - MALE/F - FEMALE) : "))
                    L4.append(input("ENTER D.O.B OF THE PATIENT (dd/mm/yyyy) : "))
                    L4.append(input("ENTER ADDRESS OF THE PATIENT : "))
                    L4.append(input("ENTER CONTACT NUMBER OF THE PATIENT (+91 **********) : "))
                    L4.append(input("ENTER TEST DATE OF THE PATIENT (dd/mm/yyyy) : "))
                    L4.append(input("ENTER TEST TYPE OF THE PATIENT (X-RAY/ECG/CT SCAN/MRI SCAN/CARDIAC CT) : "))
                    L4.append(input("ENTER DOCTOR'S NAME OF THE PATIENT : "))
                    L4.append(input("ENTER FEE'S OF THE PATIENT (IN RS.) : "))
                    L3.append(L4)
                print(L3)
                while True:
                    print("1. ADD MORE TESTS")
                    print("2. MODIFY PATIENT DETAILS")
                    print("3. SEARCH DETAILS ON THE PATIENT")
                    print("4. EXIT")
                    AD = int(input("ENTER CHOICE (1,2,3 OR 4) : "))
                    if AD == 1:
                        E2 = input("ENTER CURRENT TEST FOR THE PATIENT : ")
                        E3 = []
                        E4 = input("ENTER REGISTRATION NUMBER OF THE PATIENT : ")
                        J3 = int(input("HOW MANY TEST'S DO YOU WANT TO ADD ? : "))
                        for T in range(J3):
                            E6 = input("ENTER NEW TITLE : ")
                            E3.append(E6)
                        for T1 in L3:
                            if E2 == T1[8] and E4 == T1[0]:
                                E3.append(E2)
                                T1.pop(8)
                                T1.insert(8, E3)
                                print(L3)
                                break
                        else:
                            print("==========THE REGISTRATION NUMBER OR THE TEST IS NOT IN OUR DATABASE==========")
                    elif AD == 2:
                        while True:
                            print("1. REGISTRATION NUMBER")
                            print("2. REGISTRATION DATE")
                            print("3. NAME")
                            print("4. GENDER")
                            print("5. D.O.B")
                            print("6. ADDRESS")
                            print("7. CONTACT NUMBER")
                            print("8. TEST DATE")
                            print("9. TEST TYPE")
                            print("10. DOCTOR'S NAME")
                            print("11. FEES")
                            print("12. EXIT")
                            R2 = int(input("ENTER CHOICE (1,2,3,4,5,6,7,8,9,10,11,12): "))
                            if R2 == 1:
                                H1 = input("ENTER THE MODIFIED REGISTRATION NUMBER : ")
                                H2 = input("ENTER THE CURRENT REGISTRATION NUMBER : ")
                                for K1 in L3:
                                    if H2 == K1[0]:
                                        K1.pop(0)
                                        K1.insert(0, H1)
                                        print(K1)
                                        break
                                else:
                                    print("========THE REGISTRATION NO. IS NOT IN OUR DATABASE :(========")
                                    break
                            elif R2 == 2:
                                H3 = input("ENTER THE MODIFIED REGISTRATION DATE : ")
                                H4 = input("ENTER THE CURRENT REGISTRATION DATE : ")
                                for K2 in L3:
                                    if H4 == K2[1]:
                                        K2.pop(1)
                                        K2.insert(1, H3)
                                        print(K2)
                                        break
                                else:
                                    print("========THE REGISTRATION DATE IS NOT IN OUR DATABASE :(======== ")
                                    break
                            elif R2 == 3:
                                H5 = input("ENTER THE MODIFIED NAME : ")
                                H6 = input("ENTER THE CURRENT NAME : ")
                                for K3 in L3:
                                    if H6 == K3[2]:
                                        K3.pop(2)
                                        K3.insert(2, H5)
                                        print(K3)
                                        break
                                else:
                                    print("========THE NAME YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                    break
                            elif R2 == 4:
                                H7 = input("ENTER THE MODIFIED GENDER : ")
                                H8 = input("ENTER THE CURRENT GENDER : ")
                                for K4 in L3:
                                    if H8 == K4[3]:
                                        K4.pop(3)
                                        K4.insert(3, H7)
                                        print(K4)
                                        break
                                else:
                                    print("========INVALID GENDER========")
                                    break
                            elif R2 == 5:
                                H9 = input("ENTER THE MODIFIED D.O.B : ")
                                H10 = input("ENTER THE CURRENT D.O.B : ")
                                for K5 in L3:
                                    if H10 == K5[4]:
                                        K5.pop(4)
                                        K5.insert(4, H9)
                                        print(K5)
                                        break
                                else:
                                    print("========THE DOB YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                    break
                            elif R2 == 6:
                                H11 = input("ENTER THE MODIFIED ADDRESS : ")
                                H12 = input("ENTER THE CURRENT ADDRESS : ")
                                for K6 in L3:
                                    if H12 == K6[5]:
                                        K6.pop(5)
                                        K6.insert(5, H11)
                                        print(K6)
                                        break
                                else:
                                    print("========THE ADDRESS YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                    break
                            elif R2 == 7:
                                H13 = input("ENTER THE MODIFIED CONTACT PHONE NUMBER : ")
                                H14 = input("ENTER THE CURRENT CONTACT PHONE NUMBER : ")
                                for K7 in L3:
                                    if H14 == K7[6]:
                                        K7.pop(6)
                                        K7.insert(6, H13)
                                        print(K7)
                                        break
                                else:
                                    print(
                                        "========THE CONTACT PHONE NO. YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                    break
                            elif R2 == 8:
                                H15 = input("ENTER THE MODIFIED TEST DATE : ")
                                H16 = input("ENTER THE CURRENT TEST DATE : ")
                                for K8 in L3:
                                    if H16 == K8[7]:
                                        K8.pop(7)
                                        K8.insert(7, H15)
                                        print(K8)
                                        break
                                else:
                                    print("========THE TEST DATE IS NOT FOUND IN OUR DATABASE :(========")
                                    break
                            elif R2 == 9:
                                H17 = input("ENTER THE MODIFIED TEST TYPE : ")
                                H18 = input("ENTER THE CURRENT TEST TYPE : ")
                                for K9 in L3:
                                    if H18 == K9[8]:
                                        K9.pop(8)
                                        K9.insert(8, H17)
                                        print(K9)
                                        break
                                else:
                                    print("========THE TEST TYPE IS NOT IN OUR DATABASE :(========")
                                    break
                            elif R2 == 10:
                                H19 = input("ENTER THE MODIFIED DOCTOR'S NAME : ")
                                H20 = input("ENTER THE CURRENT DOCTOR'S NAME : ")
                                for K10 in L3:
                                    if H20 == K10[9]:
                                        K10.pop(9)
                                        K10.insert(9, H19)
                                        print(K10)
                                        break
                                else:
                                    print("========THE DOCTOR'S NAME IS NOT IN OUR DATABASE:(========")
                                    break
                            elif R2 == 11:
                                H21 = input("ENTER THE NEW FEES : ")
                                H22 = input("ENTER THE CURRENT FEES : ")
                                for K11 in L3:
                                    if H22 == K11[10]:
                                        K11.pop(10)
                                        K11.insert(10, H21)
                                        print(K11)
                                        break
                                else:
                                    print("========THE FEES IS NOT IN OUR DATABASE :(========")
                                    break
                            else:
                                break
                    elif AD == 3:
                        while True:
                            print("1. REGISTRATION NUMBER")
                            print("2. NAME AND CONTACT NUMBER ")
                            print("3. EXIT")
                            V = int(input("ENTER CHOICE (1,2 OR 3) : "))
                            if V == 1:
                                B = input("ENTER REGISTRATION NUMBER OF THE PATIENT : ")
                                for LP in L3:
                                    if B == LP[0]:
                                        print(LP)
                                        break
                                else:
                                    print("THE REGISTRATION NUMBER IS NOT IN OUR DATABASE :(")

                            elif V == 2:
                                Y = input("ENTER NAME OF THE PATIENT : ")
                                O = input("ENTER CONTACT NUMBER OF THE PATIENT : ")
                                for F in L3:
                                    if Y == F[2] and O == F[6]:
                                        print(F)
                                        break
                                else:
                                    print("THE NAME OR CONTACT NO. IS NOT IN OUR DATABASE :(")

                            else:
                                break
                    else:
                        break
    elif a == 2 :
        x = {"D_01" : "DR.RAGHU","D_02" : "DR.SUNDAR"}
        b = {"DR.RAGHU" : "D_01","DR.SUNDAR" : "D_02"}
        x1 = x.get ("D_01")
        x2 = x.get ("D_02")
        b1 = b.get ("DR.RAGHU")
        b2 = b.get ("DR.SUNDAR")
        print ("**********WELCOME DOCTOR**********")
        for N in range (3) :
            A1 = input("ENTER USERNAME : ")
            if A1  :
                pass
            A2 = input("ENTER PASSWORD : ")
            if x1 == A1 and A2 == b1 :
                print ("LOADING....")
                print ("ACCESS CODE ACCEPTED")
                break
            elif x2 == A1 and A2 == b2 :
                print ("LOADING....")
                print ("ACCESS CODE ACCEPTED")
                break
            else :
                print ("INVALID USERNAME OR PASSWORD")
        if N==2:
            break
        else:
            D2 = int(input("HOW MANY PATIENT'S DO YOU WANT TO ADD ? :"))
            D3 = []
            for YT in range(D2):
                D4 = []
                D4.append(input("ENTER REGISTRATION NUMBER OF THE PATIENT (RE-********) : "))
                D4.append(input("ENTER REGISTRATION DATE OF THE PATIENT (dd/mm/yyyy) : "))
                D4.append(input("ENTER NAME OF THE PATIENT : "))
                D4.append(input("ENTER GENDER OF THE PATIENT (M - MALE/F - FEMALE) : "))
                D4.append(input("ENTER D.O.B OF THE PATIENT (dd/mm/yyyy) : "))
                D4.append(input("ENTER ADDRESS OF THE PATIENT : "))
                D4.append(input("ENTER CONTACT NUMBER OF THE PATIENT (+91 **********) : "))
                D4.append(input("ENTER TEST DATE OF THE PATIENT (dd/mm/yyyy) : "))
                D4.append(input("ENTER TEST TYPE OF THE PATIENT (X-RAY/ECG/CT SCAN/MRI SCAN/CARDIAC CT) : "))
                D4.append(input("ENTER DOCTOR'S NAME OF THE PATIENT : "))
                D4.append(input("ENTER FEE'S OF THE PATIENT (IN RS.) : "))
                D3.append(D4)
            print(D3)
            while True:
                print("============DISORDERS============")
                print("1.STOMACH ACHE")
                print("2.FEVER")
                print("3.HEADACHE")
                print("4.DYSENTERY")
                print("5.VOMITING")
                print("6.COUGH AND COLD")
                print("7.BREATHING INCONVENIENCE")
                print("8.EXIT")
                ch1 = int(input("==========ENTER THE CHOICE OF THE DISORDER YOU HAVE=========="))
                if ch1 == 1:
                    print("1.INDIGESTION")
                    print("2.ACIDITY")
                    da1 = input("do you feel the above mentioned symptoms(yes/no)")
                    if da1 == "yes" or da1 == "YES" or da1 == "Yes":
                        print(
                            "=======================================TREATMENT PRESCRIPTION=======================================")
                        print("TAKE WARM WATER")
                        print("===>BEFORE FOOD  : PANTOPRAZOLE")
                        print("===>AFTER FOOD   : OMEZ")
                        print("===>INTAKE DAYS  : 3 DAYS(MORNING & NIGHT)")
                        print("===>DIET SCHEDULE: NO SPICY FOOD INTAKE")
                        break
                    else:
                        print("you're alright,immune your body more to stay healthy")
                elif ch1 == 2:
                    print("1.TEMPERATURE 100 DEGREE CELSIUS and above")
                    print("2.HUNGRY BUT NOT ABLE TO EAT")
                    da2 = input("do you feel the above mentioned symptoms(yes/no)")
                    if da2 == "yes" or da2 == "YES" or da2 == "Yes":
                        print(
                            "=======================================TREATMENT PRESCRIPTION=======================================")
                        print("TAKE WARM WATER")
                        print("===>BEFORE FOOD : PANTOPRAZOLE")
                        print("===>AFTER FOOD   : PARACETAMOL")
                        print("===>INTAKE DAYS  : 3 DAYS(MORNING & NIGHT)")
                        print("===>DIET SCHEDULE: NO SPICY FOOD INTAKE BUT YOU CAN TAKE BREAD AND ORS")
                        break
                    else:
                        print("you're alright,immune your body more to stay healthy")
                elif ch1 == 3:
                    print("1.FEELING PAIN IN FOREHEAD")
                    print("2.FEEL TIRED")
                    da3 = input("do you feel the above mentioned symptoms(yes/no)")
                    if da3 == "yes" or da3 == "YES" or da3 == "Yes":
                        print(
                            "=======================================TREATMENT PRESCRIPTION=======================================")
                        print("TAKE WARM WATER")
                        print("===>AFTER FOOD   : 1.CLAVAM")
                        print("===>                   2.PARACETAMOL")
                        print("===>INTAKE DAYS  : 3 DAYS(MORNING & NIGHT)")
                        print("===>DIET SCHEDULE: NORMAL DIET")
                        break
                    else:
                        print("you're alright,immune your body more to stay healthy")
                elif ch1 == 4:
                    print("1.6-7 TIMES HAD STOOLS")
                    print("FEEL TIRED")
                    da4 = input("do you feel the above mentioned symptoms(yes/no)")
                    if da4 == "yes" or da4 == "YES" or da4 == "Yes":
                        print(
                            "=======================================TREATMENT PRESCRIPTION=======================================")
                        print("TAKE WARM WATER")
                        print("===>BEFORE FOOD  : PANTOPRAZOLE")
                        print("===>AFTER FOOD   : PARACETAMOL")
                        print("===>INTAKE DAYS  : 3 DAYS(MORNING & NIGHT)")
                        print("===>DIET SCHEDULE: NO SPICY AND OUTSIDE FOOD INTAKE")
                        break
                    else:
                        print("you're alright,immune your body more to stay healthy")
                elif ch1 == 5:
                    print("NOT ABLE TO EAT ANYTHING")
                    print("FREQUENT VOMITING")
                    print("FOOD POISONING")
                    da5 = input("do you feel the above mentioned symptoms(yes/no)")
                    if da5 == "yes" or da5 == "YES" or da5 == "Yes":
                        print(
                            "=======================================TREATMENT PRESCRIPTION=======================================")
                        print("TAKE WARM WATER")
                        print("===>AFTER FOOD   : 1.EMESET")
                        print("                   2.OMEZ")
                        print("===>INTAKE DAYS  : 3 DAYS(MORNING & NIGHT)")
                        print("===>DIET SCHEDULE: YOU ARE ADVISED TO TAKE MORE OF ELECTROLYTES")
                        print("                   AVOID SPICY AND OUTSIDE FOOD INTAKE")
                        break
                    else:
                        print("you're alright,immune your body more to stay healthy")
                elif ch1 == 6:
                    print("FREQUENT COUGH")
                    print("THROAT PAIN")
                    da6 = input("do you feel the above mentioned symptoms(yes/no)")
                    if da6 == "yes" or da6 == "YES" or da6 == "Yes":
                        print(
                            "=======================================TREATMENT PRESCRIPTION=======================================")
                        print("TAKE WARM WATER")
                        print("===>AFTER FOOD   : 1.AZITHROMYCIN")
                        print("===>                           :2.SOMOFLAM")
                        print("===>INTAKE DAYS  : 3 DAYS(MORNING & NIGHT)")
                        print("===>DIET SCHEDULE: YOU ARE ADVISED TO TAKE BOILED RICE FLUID")
                        break
                    else:
                        print("you're alright,immune your body more to stay healthy")
                elif ch1 == 7:
                    print("BREATHING SUFFOCATION")
                    print("CHOLESTEROL")
                    da7 = input("do you feel the above mentioned symptoms(yes/no)")
                    if da7 == "yes" or da7 == "YES" or da7 == "Yes":
                        print(
                            "=======================================TREATMENT PRESCRIPTION=======================================")
                        print("TAKE WARM WATER")
                        print("NEUBULIZER FOR 3 DAYS")
                        print("AVOID DUST ALLERGY")
                        print("===>AFTER FOOD   : 1.IPRATROPIUM")
                        print("===>DIET SCHEDULE: HAVE SPROUTED GRAINS AND STREAMED FOOD")
                        break
                    else:
                        print("you're alright,immune your body more to stay healthy")
                elif ch1 == 8:
                    break
                else:
                    print("THE DISORDER IS NOT IN OUR DATABASE :(")
                    break
            while True:
                print("1. ADD MORE TEST'S FOR THE PATIENT")
                print("2. MODIFY DETAILS OF THE PATIENTS")
                print("3. SEARCH DETAILS OF THE PATIENT")
                print("4. EXIT")
                D1 = int(input("ENTER CHOICE(1,2,3 OR 4) : "))
                if D1 == 1:
                    G2 = input("ENTER CURRENT TEST FOR THE PATIENT : ")
                    G3 = []
                    G4 = input("ENTER REGISTRATION NUMBER OF THE PATIENT : ")
                    G5 = int(input("HOW MANY TEST'S DO YOU WANT TO ADD ? : "))
                    for S in range(G5):
                        G6 = input("ENTER NEW TITLE : ")
                        G3.append(G6)
                    for S1 in D3:
                        if G2 == S1[8] and G4 == S1[0]:
                            G3.append(G2)
                            S1.pop(9)
                            S1.insert(9, G3)
                            print(S1)
                            break
                    else:
                        print("========THE REGISTRATION NO. OR TEST IS NOT IN OUR DATABASE :(========")

                elif D1 == 2:
                    while True:
                        print("1. REGISTRATION NUMBER")
                        print("2. REGISTRATION DATE")
                        print("3. NAME")
                        print("4. GENDER")
                        print("5. D.O.B")
                        print("6. ADDRESS")
                        print("7. CONTACT NUMBER")
                        print("8. TEST DATE")
                        print("9. TEST TYPE")
                        print("10. DOCTOR'S NAME")
                        print("11. FEES")
                        print("12. EXIT")
                        P2 = int(input("ENTER CHOICE (1,2,3,4,5,6,7,8,9,10,11 OR 12) : "))
                        if P2 == 1:
                            Q1 = input("ENTER THE MODIFIED REGISTRATION NUMBER : ")
                            Q2 = input("ENTER THE CURRENT REGISTRATION NUMBER : ")
                            for M1 in D3:
                                if Q2 == M1[0]:
                                    M1.pop(0)
                                    M1.insert(0, Q1)
                                    print(M1)
                                    break
                            else:
                                print(
                                    "========THE REGISTRATION NO. YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                break
                        elif P2 == 2:
                            Q3 = input("ENTER THE MODIFIED REGISTRATION DATE : ")
                            Q4 = input("ENTER THE CURRENT REGISTRATION DATE : ")
                            for M2 in D3:
                                if Q4 == M2[1]:
                                    M2.pop(1)
                                    M2.insert(1, Q3)
                                    print(M2)
                                    break
                                else:
                                    print(
                                        "========THE REGISTRATION DATE YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                    break
                        elif P2 == 3:
                            Q5 = input("ENTER THE MODIFIED NAME : ")
                            Q6 = input("ENTER THE CURRENT NAME : ")
                            for M3 in D3:
                                if Q6 == M3[2]:
                                    M3.pop(2)
                                    M3.insert(2, Q5)
                                    print(M3)
                                    break
                            else:
                                print("========THE NAME YOU WANTED TO MODIFY IS NOT IN OUR DATABASE:(========")
                                break
                        elif P2 == 4:
                            Q7 = input("ENTER THE MODIFIED GENDER : ")
                            Q8 = input("ENTER THE CURRENT GENDER : ")
                            for M4 in D3:
                                if Q8 == M4[3]:
                                    M4.pop(3)
                                    M4.insert(3, Q7)
                                    print(M4)
                                    break
                            else:
                                print("========THE GENDER YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                        elif P2 == 5:
                            Q9 = input("ENTER THE MODIFIED D.O.B : ")
                            Q10 = input("ENTER THE CURRENT D.O.B : ")
                            for M5 in D3:
                                if Q10 == M5[4]:
                                    M5.pop(4)
                                    M5.insert(4, Q9)
                                    print(M5)
                                    break
                            else:
                                print("========THE DOB YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                        elif P2 == 6:
                            Q11 = input("ENTER THE MODIFIED ADDRESS : ")
                            Q12 = input("ENTER THE CURRENT ADDRESS : ")
                            for M6 in D3:
                                if Q12 == M6[5]:
                                    M6.pop(5)
                                    M6.insert(5, Q11)
                                    print(M6)
                                    break
                            else:
                                print("========THE ADDRESS YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                break
                        elif P2 == 7:
                            Q13 = input("ENTER THE MODIFIED CONTACT PHONE NUMBER : ")
                            Q14 = input("ENTER THE CURRENT CONTACT PHONE NUMBER : ")
                            for M7 in D3:
                                if Q14 == M7[6]:
                                    M7.pop(6)
                                    M7.insert(6, Q13)
                                    print(M7)
                                    break
                                else:
                                    print(
                                        "========THE  PHONE NO. YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                    break
                        elif P2 == 8:
                            Q15 = input("ENTER THE TEST DATE YOU WANTED TO MODIFY: ")
                            Q16 = input("ENTER THE CURRENT TEST DATE : ")
                            for M8 in D3:
                                if Q16 == M8[7]:
                                    M8.pop(7)
                                    M8.insert(7, Q15)
                                    print(M8)
                                    break
                            else:
                                print("========THE TEST TYPE YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                break
                        elif P2 == 9:
                            Q17 = input("ENTER THE MODIFIED TEST TYPE: ")
                            Q18 = input("ENTER THE CURRENT TEST TYPE: ")
                            for M9 in D3:
                                if Q18 == M9[8]:
                                    M9.pop(8)
                                    M9.insert(8, Q17)
                                    print(M9)
                                    break
                            else:
                                print("========THE TEST TYPE YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                break
                        elif P2 == 10:
                            Q19 = input("ENTER THE MODIFIED DOCTOR'S NAME : ")
                            Q20 = input("ENTER THE CURRENT DOCTOR : ")
                            for M10 in D3:
                                if Q20 == M10[9]:
                                    M10.pop(9)
                                    M10.insert(9, Q19)
                                    print(M10)
                                    break
                            else:
                                print("========THE DOCTOR YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                break
                        elif P2 == 11:
                            Q21 = input("ENTER THE MODIFIED FEES : ")
                            Q22 = input("ENTER THE CURRENT FEES: ")
                            for M11 in D3:
                                if Q22 == M11[10]:
                                    M11.pop(10)
                                    M11.insert(10, Q21)
                                    print(M11)
                                    break
                            else:
                                print("========THE FEES YOU WANTED TO MODIFY IS NOT IN OUR DATABASE :(========")
                                break
                        elif P2 == 12:
                            break
                        else:
                            print("=============>INAVLID CHOICE<============")
                            break
                elif D1 == 3:
                    while True:
                        print("1. REGISTRATION NUMBER")
                        print("2. NAME AND CONTACT NUMBER")  # SHOULD BE EDITED
                        print("3. EXIT")
                        V1 = int(input("ENTER CHOICE (1,2 OR 3) :"))
                        if V1 == 1:
                            B1 = input("ENTER REGISTRATION NUMBER OF THE PATIENT : ")
                            for KP in D3:
                                if B1 == KP[0]:
                                    print(KP)
                                    break
                            else:
                                print("THE REGISTRATION NO. IS NOT IN OUR DATABASE :(")
                                break
                        elif V1 == 2:
                            Y1 = input("ENTER NAME OF THE PATIENT :")
                            O1 = input("ENTER CONTACT NUMBER OF THE PATIENT : ")
                            for F1 in D3:
                                if Y1 == F1[2] and O1 == F1[6]:
                                    print(F1)
                                    break
                            else:
                                print("THE NAME OR CONTACT NO. IS NOT IN OUR DATABASE :(")
                                break
                        else:
                            break
                else:
                    break
    else:
        print("THANK YOU")
        print("VISIT ONCE AGAIN")
        break