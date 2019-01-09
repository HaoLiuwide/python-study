class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def gpa(self):
        return self.qpoints/self.hours


def makeStudent(infoStr):
    try:
        name, hours, qpoints = infoStr.split(',')
    except ValueError:
        pass
    return Student(name, hours, qpoints)


def readStudents(filename):
    infile = open(filename, 'r')
    student = []
    for line in infile:
        try:
            student.append(makeStudent(line))
        except ValueError:
            pass
    infile.close()
    return student


def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print('{0}\t{1}\t{2}'.format(s.name, s.hours, s.qpoints), file=outfile)
    outfile.close()


def main():
    filename = input('Enter the name of the data file: ')
    data = readStudents(filename)
    data.sort(key=Student.gpa)
    filename = input('Enter a name for the output file: ')
    writeStudents(data, filename)
    print('the data has been written to', filename)


if __name__ == '__main__':
    main()
