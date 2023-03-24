# Import the xlrd module
import xlrd
import Case


def print_xlsx(filename, rows, cols):
    # Open the workbook
    book = xlrd.open_workbook(filename)

    # Get the first sheet
    sheet = book.sheet_by_index(0)

    # Read the rows and columns
    for i in range(rows):
        for j in range(cols):
            # Read the cell value
            cell_value = sheet.cell_value(i, j)
            print(cell_value)
            elements = cell_value.split(",")
            print(elements)
            case = case(j, i, elements[0], elements[1], elements[2], elements[3])



print_xlsx("maps/mapTest.xls", 10, 10)
