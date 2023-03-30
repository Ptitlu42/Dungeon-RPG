# import
import xlrd
import Case

# variables
actual_map = []


# functions
def load_map(filename, rows, cols):
    # Open the workbook
    book = xlrd.open_workbook(filename)
    # Get the first sheet
    sheet = book.sheet_by_index(0)
    cell = 0
    # Read the rows and columns
    for i in range(rows):
        for j in range(cols):
            # Read the cell value
            cell_value = sheet.cell_value(i, j)

            elements = cell_value.split(",")

            case = Case.Case(j, i, elements[0], elements[1], elements[2], elements[3])
            #print(case.__repr__())
            #print(f"print {case}")
            actual_map.append(case)
            cell += 1
    print(f"debug:{actual_map}")
    
    return actual_map

'''def load_map2(map):
    nb_line = 0
    for line in map.:
        nb_element = 0
        for element in line:
            nb_element += 1
            case = Case.case(nb_element, nb_line, )'''
