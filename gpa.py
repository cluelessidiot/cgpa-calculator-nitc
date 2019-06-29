from tabula import wrapper
import xlrd
import openpyxl
class Gpa(object):
    # data attributes
    "helps to calculate the Gpa and Cgpa"
    arg1 = None
    arg2 = None
    subData = None
    Scale = None
    credits = None
    initCourse = 0
    initgetCredit = 0
    totalCredits = 0
    temp = 0
    gradesArray = []
    creditsArray = []
    creditCount=0
    gradeCount=0
    semesterCount=0

    def getPdf(self):
        tables = wrapper.read_pdf("qw.pdf",multiple_tables=True,pages='all',encoding='utf-8',spreadsheet=True)
        i=1
        row_array = []
        row_array2=[]
        for table in tables:
            table.columns = table.iloc[0]
            table = table.reindex(table.index.drop(0)).reset_index(drop=True)
            table.columns.name = None
            #To write Excel
            table.to_excel('output'+str(i)+'.xlsx',header=True,index=False)
            workbook = xlrd.open_workbook('output2.xlsx')
            worksheet = workbook.sheet_by_name('Sheet1')
            num_rows = 5 #worksheet.nrows - 1
            curr_row = 4
            while curr_row < num_rows:
                row = worksheet.col(curr_row)
                #print(row)
                row2 = worksheet.col(curr_row-1)
                row_array += row
                row_array2+= row2
                curr_row += 1
                i=i+1

        for i in range (len(row_array)):
            #print(row[i].split("'"))
            #k=string(row[i])
            if row_array[i].value!='':
                if row_array[i].value=='Grade':
                    self.semesterCount+=1
                    self.gradesArray.append(int(self.semesterCount))
                    self.creditsArray.append('D')
                else:    
                    print(row_array[i].value)
                    gradeSingle=str(row_array[i].value)
                    creditSingle=int(row_array2[i].value)
                    self.gradesArray.append(gradeSingle)
                    self.creditsArray.append(creditSingle)
    #gradesArray+=row_array[i].value
    #creditsArray+=row_array2[i].value
        print(self.gradesArray)
        print(self.creditsArray)
    
    def parser(self):
        print(self.gradesArray[self.gradeCount])
        pass
        

    def getCourse(self):
        "get the value of the no of course you registered"
        self.arg1 = input("No of course you have registered: " )
        pass
    
    def getSubject(self,value):
        "get the subject value"
        self.arg2 = value
        pass
    
    def getScale(self):
        "To get the scale value"
        self.Scale = input("Enter the Scale value(Either 5 or 10): " )
        pass
        
        
    def getSubjectData(self):
        "get the subject Data in string"
        self.subData = raw_input("Enter the grade: " ) 
        pass              
    def getGradeData(self):
        # To calculate grade for two scale,one is for 5.0 and other one for 10.0
        grade1 = {'s':10,'a':9,'b':8,'c':7,'d':6,'e':5,'f':0}
        x=grade1[self.subData]
        return x 
    def getCredits(self):
        "get credit value"
        self.credits = input("Enter the credits for a subject:"  )
        pass
    
    def gpa(self):
        print "Calculate GPA:"
        sem = raw_input("Please Enter Semester: " )
        self.getCourse()
        
        pass
                
                
    def calculateGpa(self):
        "Method to calculate Gpa "
        while self.initCourse!=self.arg1:
            self.initCourse=self.initCourse+1
            self.getCredits()
            self.initgetCredit = self.credits
            self.getSubjectData()
            #type(self.getSubjectData())
            self.temp = self.initgetCredit*self.getGradeData()+self.temp
            self.totalCredits=self.totalCredits+self.initgetCredit
            
        gpa = round((self.temp+.0)/(self.totalCredits+.0),2)
        print "you have registered for total credits:"+" "+str(self.totalCredits)+" "+"and you have acquired GPA:\""+str(gpa)+"\""
        pass
    
    def cgpa(self):
        self.getPdf()
        self.parser()
        print "Calculate your cgpa: "
        f = open("a.txt", "r")
        semesters = f.readline()                    # input("Enter how many semester cgpa has to be found of: " )
        counter = 0
        tempInit = 0
        tempTotalCredits = 0
        while counter != semesters:
                counter = counter+1
                print "Please enter the details of the semester"+" "+str(counter)
                self.getCourse()
                self.calculateGpa()
                tempInit = self.temp+tempInit
                tempTotalCredits = tempTotalCredits + self.totalCredits
                # re-assigning
                self.arg1=0
                self.initCourse =0
                self.temp=0
                self.totalCredits=0
                print "\n"
                
        cgpa = round((tempInit+.0)/(tempTotalCredits+.0),2)
        print "you have registered for total credits:"+" "+str(tempTotalCredits)+" "+"and you have acquired CGPA:\""+str(cgpa)+"\" "    
        pass


if __name__ == '__main__': # main method
    #how to calculate it

    Init = Gpa() # Creating Instance

    # for calculation of Cgpa (cumulative grade point average)
    Init.cgpa()

    # In Order to calculate Gpa for single semester
    #Init.gpa()
