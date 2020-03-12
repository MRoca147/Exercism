class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")

    def row(self, index):
        row = [int(x) for x in self.matrix[index-1].split(" ")]
        return row

    def column(self, index):
        numbers = []
        result = []
        for x in self.matrix:
            numbers.append([int(i) for i in x.split(' ')])
        for row in numbers:
            result.append(row[index-1])
        return result
