""" This programme creates a test source for Data & stores taht Data in a SQl FIle """

class student:
    def __init__ (self, name, SID, sub1, sub2, sub3, attn1, attn2, attn3, fees):
        self.name = name
        self.SID = SID
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.attn1 = attn1
        self.attn2 = attn2
        self.attn3 = attn3
        self.feesPaid = fees
        self.gradesObtained = "D"
        self.attendanceTaken = 0
        self.results = 0

    def grades (self):
        """ Compute grades on 3 subject marks """
        totalMarks = 300
        obtainedMarks = ((self.sub1+self.sub2+self.sub3)/totalMarks)*100
        print (obtainedMarks)

        if obtainedMarks > 90:
            self.gradesObtained = "A"

        elif obtainedMarks > 75 and obtainedMarks < 90:
            self.gradesObtained = "B"

        elif obtainedMarks > 50 and obtainedMarks < 75:
            self.gradesObtained = "C"

        else:
            self.gradesObtained = "D"

        return self.gradesObtained

    def attendance(self):
        """ Compute attendence based on number of days """
        totalDays = 300
        self.attendanceTaken = ((self.attn1+self.attn2+self.attn3)/totalDays)*100

        return self.attendanceTaken

    def result(self):
        """ based on Attendence and Grades, it will be declared if he passed or failed 
            Attendence > 75%
            Grades > C 
        """

        if self.attendanceTaken > 75 and self.gradesObtained == ("A" or "B" or "C"):
            self.results = "PAss"
        else:
            self.results = "FAil"

        return self.results

    def convertJson (self, object):
        """ Converts the result into jSon """
        print ("\n")
        print (object.name+":")
        object.attendance()
        print (object.attendanceTaken)
        object.grades()
        print (object.gradesObtained)
        object.result()
        print (object.results)
        print ("=====================================")
        


stu1 = student ("Sagar", "S01", 75, 85, 74, 50, 12, 78, 5000)
stu2 = student ("Sanjay", "S02", 12,96,47,25,87,63, 50000)
stu3 = student ("Deepti", "S03", 89,78,45,36,45,69,10000)
stu4 = student ("Riddhi", "S04", 45,89,12,89,87,65,98000)
stu5 = student ("Niyati", "S05", 89,78,54,3,56,98,99000)

stu1.convertJson(stu1)
stu2.convertJson(stu2)
stu3.convertJson(stu3)
stu4.convertJson(stu4)
stu5.convertJson(stu5)


#gradesObtained = stu1.grades()
#attendanceTaken = stu1.attendance()
#results = stu1.result()



