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

            elements = cell_value.split(",")

            case = Case.Case(j, i, elements[0], elements[1], elements[2], elements[3])
            #print(case.__repr__())
            #print(f"print {case}")
            actual_map.append(case)
            cell += 1
    return actual_map

# def get_number_of_columns_and_rows(rows, cols):
#     nbr_cols = ()
#     nbr_rows = ()
    
#     for i in range (cols):
#         nbr_cols + 1
        
#     for i in range (rows):
#         nbr_rows + 1
        
#     print (nbr_cols)
#     print (nbr_rows)
    
# get_number_of_columns_and_rows(rows, cols)