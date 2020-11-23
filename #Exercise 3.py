#Exercise 3 

class Person:
    
    def __init__(self, name, address):
        self._name = name
        self._address = address 

    def getName(self):
        return self._name 

    def getAddress(self):
        return self._address

    def setAddress(self):
        self._address = address

    def __str__(self):
        return {self._name}{(self._address)}

    def printGrades(self):
        print(self._grades)

class Student(Person):
    
    def __init__(self, name, address, numCourses = 0, courses=[], grades =[]):
        super().__init__(name,address)
        self._numCourses = numCourses
        self._courses = courses 
        self._grades = grades 
    
    def addCourseGrades(self):
         self.__courses.append(course)
         self.__grades.append(grade)
    
    def getAverageGrade(self):
        return sum(self._grades) / len(self._grades)
        
    def __str__(self):
        return "Student: " + self.getName() + '(" + self.getAddress() + ')'


class Teacher(Person):

    def __init__ (self, name, address, numcourses = 0, courses=[]):
        super()._init__(name, address)
        self._numcourses = numcourses
        self._courses = courses 

    def __str__(self):
        return "Teacher:" + self.getName() + "(" + self.getAddress() + "")"

   
    def addCourse(self, courses):
        if course in self._courses:
            return False
        else:
            self._courses.append(courses)
            self._numcourses +=1

    def removeCourse(self, courses):
        if course not in self._courses:
            return False
        else:
            self._courses.remove(courses)
            self._numcourses -= 1



    


