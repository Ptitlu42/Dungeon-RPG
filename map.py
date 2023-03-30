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
        self.rows = rows
        self.cols = cols
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
        print(self.actual_map)

    def get_cell_by_xy(self, x, y):
        id = x + self.cols * y
        cell = self.actual_map[id]
        return cell