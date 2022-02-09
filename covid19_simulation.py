##26/12 3.40 AM
##########################################################################################################
#  * DATE       : 23-11-2021
#  * COURSE     : PROGRAMMING QUEST (CO2210)
#  * TITLE      : QUEST 09 - Simulating COVID-19 spread in a conceptual community
#  * AUTHOR     : GROUP11
#  ******************************************************************************************************
#  * MEMBERS    : 19/ENG/121-A.P.Maduwantha, 19/ENG/107-Virudaka  AND 18/ENG/002-C. Abeysinghe
##########################################################################################################
import random
import math
import matplotlib.pyplot as plt


AGE_TYPE_SENIOR = 3
AGE_TYPE_MIDDLE = 2
AGE_TYPE_CHILDREN = 1

totalInfected = 0
totalHospitalized = 0
totalRecovered = 0
totalDeath = 0
stillInHospital = 0
day = 1
# noOfFamilyMembers = 2
# wearingMask = 0

class Person:
    
    
    # totalProbability = 0
  
    global day
    def __init__(self, ageType, noOfFamilyMembers, wearingMask,familyNO,count):
        self.isInfected = False
        self.reduceProbability=0
        self.familyProbability=0
        self.suspiciousDays = 0
        self.infectedDays = 0 
        self.ageType = ageType
        self.noOfFamilyMembers = noOfFamilyMembers
        self.wearingMask = wearingMask
        self.familyNO = familyNO,
        self.id= count
        
        
        if ageType==3:
            self.ageProbability = random.randint(35,60)
        if ageType==2:
            self.ageProbability = random.randint(15,40)
        if ageType==1:
            self.ageProbability = random.randint(10,20)

        if wearingMask == 1:
            self.reduceProbability = random.randint(5,10)

    def positive():
      self.isInfected = True
      return self.isInfected

    def isFamilyMember(self,familyNumber):
        # family number 100001 does not belong to any family
        if familyNumber == self.familyNO and self.familyNO != 100001:
            self.familyProbability = random.randint(40,80)
            return True

    def increaseHospitalizeDays(self):
        self.infectedDays = self.infectedDays + 1
        return self.infectedDays

    def increaseDay(self):
        self.suspiciousDays = self.suspiciousDays + 1
        return self.suspiciousDays

    def printPerson(self):
        totalProbability = self.ageProbability + self.familyProbability - self.reduceProbability
        value = self.findInfected()
        if(value == 1):
            print('Infected') 
        else: 
            print('Not Infected')
        print('___________________')
        print('Infected Day : ',self.infectedDays)
        print('Age Type : ', self.ageType)
        print('Age Probability : ', self.ageProbability)
        print('Wearing Mask : ', self.wearingMask)
        print('Reduce Probability : ', self.reduceProbability)
        print('Family NO : ', self.familyNO)
        print('Family Probability : ', self.familyProbability)
        print('Total Probability : ', totalProbability)
        print('=============================================================')

    # totalProbability = ageProbability + familyProbability -reduceProbability
    def findInfected(self):
        totalProbability = self.ageProbability + self.familyProbability - self.reduceProbability
        # print('Total Probability : ', totalProbability)
        #take random no and check the person infected or not
        randomProbability = random.randint(1,100)
        # print('Random Probability : ', randomProbability)
        if totalProbability >= randomProbability:
        # if totalProbability >= 100:
            return 1

 #########################################################################################################  
objectArray = []    #families
indexList = []      #index of persons
idxLst = []
patientList = []
previousDayPatientList = [] 
finalList = []
wearingMask = 0
#there are 100000 families

count =0 
for family in range(0, 100000):
    noOfFamilyMembers = random.randint(2,7)
    for member in range(0, noOfFamilyMembers):
        ageType = random.randint(1,3)
        wearingMask = random.randint(0,1)
        objectArray.append(Person(ageType, noOfFamilyMembers, wearingMask, family,count))
        count = count+1

#family id 100001 means no family
for alone in range(0, 1000000-len(objectArray)):
    ageType = random.randint(1,3)
    wearingMask = random.randint(0,1)
    objectArray.append(Person(ageType, noOfFamilyMembers, wearingMask, 100001,count))
    count = count+1

#Assume that the first person in the array is infected
#if travel restriction is there then the infected person will contact with 0-20 people out of family
Id = 0
indexList.append(Id)
previousDayPatientList = []
patientList.append(objectArray[Id])
previousDayPatientList.append(objectArray[Id])
objectArray[Id].positive
infectedAtDay = 0
totalHospitalizedAtDay = 0
contactOutsidePeopleUpperLimit = 20
##################################################################################################################
def simulate(patient):
    # global totalInfected
    # global totalHospitalized
    global contactOutsidePeopleUpperLimit
    outPeople = random.randint(5,contactOutsidePeopleUpperLimit)    #not family members
    familyNum = patient.familyNO
    #objects are sorted according to family number
    #maximum number of people in a family is 7
    #therefore we can check 7 objects forward and 7 objects backward if array allows

    objectId = objectArray.index(patient)
    if objectId-7 >= 0:
        for i in range(objectId-7, objectId):
            family=objectArray[i].isFamilyMember(familyNum)    #check if the person is family member and set the probability
            if family==True:
                if indexList.count(i)==0:
                    indexList.append(i)

    if objectId+7 < len(objectArray):
        for i in range(objectId+1, objectId+7):
            family=objectArray[i].isFamilyMember(familyNum)    #check if the person is family member and set the probability
            if family==True:
                if indexList.count(i)==0:
                    indexList.append(i)

    #remove duplicates
    # idxLst = list(dict.fromkeys(indexList))
    #take random list 
    randomOuterPeoples = []
    randomOuterPeoples = random.sample(range(0, len(objectArray)), outPeople)

    #check person can infected or not
    for person in randomOuterPeoples:
        personFamily = patient.familyNO
        isAMembers=patient.isFamilyMember(personFamily)
        if isAMembers==False:
            #family members are already taken to check
            if indexList.count(person)==0:
                indexList.append(person)
  
    global totalHospitalizedAtDay
    global infectedAtDay
    for check in indexList:
        # totalHospitalizedAtDay = 0
        #check the list once a day
        objectArray[check].increaseDay()
        #remove the index from the list which more than 10 days old
        if (len(indexList)>=1 and objectArray[check].suspiciousDays > 10):
            indexList.remove(check)
        isInfected = objectArray[check].findInfected()
        if isInfected == 1 or objectArray[check].isInfected:
            objectArray[check].positive
            # objectArray[check].printPerson()
            infectedAtDay = infectedAtDay + 1
            #assume that the person is infected, immediately go to hospital
            totalHospitalizedAtDay = totalHospitalizedAtDay + 1
            #if infected that person will not check any more because he/she has immunity for 6 to 7 months
            patientList.append(objectArray[check])  #add the person to the patient list
            # print(patientList)
            # objectArray.remove(objectArray[check])  #remove the patient from the object array
            # if indexList.count(check)>0:
            #     indexList.remove(check)

    return totalHospitalizedAtDay, infectedAtDay
            

dailyInfected = []
dailyHospitalized = [] 
dailyRecovered = []
dailyDeaths = []

for day in range(1,51):
    list3 = list(dict.fromkeys(patientList))
    # print("Previous Day patients at day begining",len(patientList))
    # patientList.clear()
    totalDeathAtDay = 0
    recoveredAtDay = 0 
    
    print("Are people enforced to wear masks in day  ",day)
    isWearingMask = input("Enter 1 if yes Enter any other number if no  : ")
    # isWearingMask=1
    print("Are there travelling restrictions in day ",day)
    travelling = input("Enter 1 if yes Enter any other number if no : ")
    # travelling=1

    if(isWearingMask == 1):
      wearingMask = 1
    else:
      wearingMask = 0

    if(travelling == 1):
      contactOutsidePeopleUpperLimit = 50
    else:
      contactOutsidePeopleUpperLimit = 20
    count = 0 
    for person in list3:
        totalHospitalizedAtDay, infectedAtDay = simulate(person)


    totalInfected = totalInfected + infectedAtDay
    totalHospitalized = totalHospitalized + totalHospitalizedAtDay
    dailyInfected.append(infectedAtDay)
    dailyHospitalized.append(totalHospitalizedAtDay)
    print('|Total Infected :         |', totalInfected) 
  
    #update pateint list daily
    count = 0 
    for patient in patientList:
        patient.increaseHospitalizeDays()   #INCREASE THE DAYS OF HOSPITALIZED
        count = count+1
        # patient.printPerson()
        if patient.infectedDays >=10:
            recoveredAtDay = recoveredAtDay + 1
            stillInHospital = totalHospitalized - 1


    #take 0.1 of hospitalized people die
    totalDeathAtDay = math.floor(stillInHospital*0.001)
    totalDeath = totalDeath + totalDeathAtDay
    totalRecovered = totalHospitalized - totalDeath
    dailyRecovered.append(totalRecovered)
    dailyDeaths.append(totalDeath)
    print('Day : ', day)
    
    dailyList = [infectedAtDay, totalHospitalizedAtDay, totalDeathAtDay, recoveredAtDay]
    finalList.append(dailyList)
    # print('|Total Infected :         |', totalInfected)
    print('Total infected at day : ', infectedAtDay)
    print('Total hospitalized at day : ', totalHospitalizedAtDay)
    # print('Total recovered at day : ', totalRecovered)
    # print('Total death at day : ', totalDeath)
    # infectedAtDay = 0
    # totalHospitalizedAtDay = 0
    print('#####################################################')
    # previousDayPatientList = patientList 
    # patientList.clear()

    
print('=====================================================')
print('|Total Infected :         |', totalInfected)
print('|Totals Hospitalized :    |', totalHospitalized)
print('|Total Recovered :        |', totalRecovered)
print('|Total Death :            |', totalDeath)
print('=====================================================')

plt.plot(dailyInfected)
plt.ylabel('Infected Per Day')
plt.show()

plt.plot(dailyHospitalized)
plt.ylabel('Hospitalized Per Day')
plt.show()

plt.plot(dailyRecovered)
plt.ylabel('Recovered Per Day')
plt.show()
plt.plot(dailyDeaths)
plt.ylabel('Deaths Per Day')
plt.show()