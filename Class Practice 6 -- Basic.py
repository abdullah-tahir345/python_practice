class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []
        print(f'Your name is {self.name} and it is your portal...')
        
    def enroll(self, course):
        course = course.lower()
        self.courses.append(course.title())
        return f"Your course {course.title()} is enrolled."
    
    def drop(self, course):
        course = course.lower()
        self.courses.remove(course.title())
        return f"Your course {course.title()} is dropped."
    
    def list_courses(self):
        return self.courses
    
    def student_info(self):
        return f"Student Information : \nName : {self.name}\nAge : {self.age}\nCourses : {self.courses}"
    
if __name__ == "__main__":
    std1 = Student('John Abraham', 25)
    print(std1.enroll('Applied Programming'))
    print(std1.enroll('Databases'))
    print(std1.enroll('Data Sciences'))
    print(std1.enroll('Mid Level Programming'))
    print(std1.enroll('Information Security'))
    print()
    print(std1.courses)
    
    print()
    print(std1.drop('mid level programming'))
    print(std1.list_courses())
    
    print()
    print(std1.student_info())
    
    print('-------------------------------------------------------------------------------')
    
    std2 = Student('Hritik Roshan', 26)
    print(std2.enroll('Applied Programming With Python'))
    print(std2.enroll('Data Analysis Part 1'))
    print(std2.enroll('Data Bases'))
    print(std2.enroll('Information Security'))
    
    print()
    print(std2.student_info())
    
    
    