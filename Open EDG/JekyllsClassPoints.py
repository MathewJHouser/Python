from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line_num, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


students = {}
line_number = 1

try:
    file = input("Enter file name: ")
    stream = open(file, "rt")
    l = stream.readlines()
    stream.close()

    if len(l) == 0:
        raise FileEmpty()

    for i in range(len(l)):
        line = l[i]
        entry = line.split()
        if len(entry) != 3:
            raise BadLine(i + 1, line)
        name = entry[0] + " " + entry[1]
        try:
            if name not in students.keys():
                students[name] = float(entry[2])
            else:
                students[name] += float(entry[2])
        except ValueError:
            raise BadLine(i + 1, line)

    final = sorted(students.keys())
    message = ""

    for key in final:
        message += key + "\t\t" + str(students[key]) + "\n"

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except BadLine as e:
    print("Issue in line #" + str(e.line_number) + " of source file:\n" + e.line_string)
except FileEmpty:
    print("File is empty.")
except Exception as e:
    print("Error has occurred,", e)
else:
    print(message)
