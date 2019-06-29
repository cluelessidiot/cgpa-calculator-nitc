from tabula import wrapper
import xlrd
import openpyxl
tables = wrapper.read_pdf("qw.pdf",multiple_tables=True,pages='all',encoding='utf-8',spreadsheet=True)

i=1
row_array = []
row_array2=[]
semesterCount=0
for table in tables:
    table.columns = table.iloc[0]
    table = table.reindex(table.index.drop(0)).reset_index(drop=True)
    table.columns.name = None
    #To write Excel
    table.to_excel('output'+str(i)+'.xlsx',header=True,index=False)
    workbook = xlrd.open_workbook('output'+str(i)+'.xlsx')
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
gradesArray = []
creditsArray = []
for i in range (len(row_array)):
    #print(row[i].split("'"))
    #k=string(row[i])
    if row_array[i].value!='':
        if row_array[i].value=='Grade':
            semesterCount+=1
            gradesArray.append(int(semesterCount))
            creditsArray.append('D')
        else:    
            print(row_array[i].value)
            gradeSingle=str(row_array[i].value)
            creditSingle=int(row_array2[i].value)
            gradesArray.append(gradeSingle)
            creditsArray.append(creditSingle)
    #gradesArray+=row_array[i].value
    #creditsArray+=row_array2[i].value
print(gradesArray)
print(creditsArray)
print(semesterCount)


#creates an array to store all the rows



#print(row_array)
#print(row_array2)