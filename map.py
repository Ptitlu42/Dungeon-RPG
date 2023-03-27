# import
import xlrd
import Case

# variables
actual_map = []


# functions
def load_map(filename):
    # Open the workbook
    book = xlrd.open_workbook(filename)
    
    #Get number of cols and rows
    worksheet = book.sheet_by_index(0)
    nbr_cols = worksheet.ncols
    nbr_rows = worksheet.nrows
    
    # Get the first sheet
    sheet = book.sheet_by_index(0)
    cell = 0
    # Read the rows and columns
    for i in range(nbr_rows):
        for j in range(nbr_cols):
            # Read the cell value
            cell_value = sheet.cell_value(i, j)
            #print(f"Cell_value = \n {cell_value} \n")

            elements = cell_value.split(",")
            #print (f"Elements = \n {elements} \n")
            
            case = Case.Case(j, i, elements[0], elements[1], elements[2], elements[3])
            #print(f"Case = \n {case} \n")
            
            actual_map.append(case)
            cell += 1
    return actual_map

#Find an object in map
def find_object_case(filename, object_name):
   
    book = xlrd.open_workbook(filename)
    worksheet = book.sheet_by_index(0)
    
    for i in range(worksheet.nrows):
        for j in range(worksheet.ncols):
            cell_value = worksheet.cell_value(i, j)
            elements = cell_value.split(",")
            for element in elements:
                if element == object_name:
                    return True
                    