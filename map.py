# import
import xlrd
import Case


# variables
class Map():

    def __init__(self, filename, rows, cols):

        self.actual_map = []
        # Open the workbook
        self.book = xlrd.open_workbook(filename)
        # Get the first sheet
        sheet = self.book.sheet_by_index(0)
        cell = 0
        # Read the rows and columns
        for i in range(rows):
            for j in range(cols):
                # Read the cell value
                cell_value = sheet.cell_value(i, j)

                elements = cell_value.split(",")

                self.case = Case.Case(j, i, elements[0], elements[1], elements[2], elements[3])
                # print(case.__repr__())
                # print(f"print {case}")
                self.actual_map.append(self.case)
                cell += 1
        print(self.actual_map)

    # functions
    '''def load_map(self, filename, rows, cols):
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

                self.case = Case.Case(j, i, elements[0], elements[1], elements[2], elements[3])
                # print(case.__repr__())
                # print(f"print {case}")
                self.actual_map.append(self.case)
                cell += 1
        return self.actual_map'''