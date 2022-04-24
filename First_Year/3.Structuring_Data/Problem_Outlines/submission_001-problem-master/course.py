

def create_outline():
   

    #step 1
    print("Course Topics:")
    course_topics = ["Introduction to Python","Tools of the Trade","How to make decisions","How to repeat code","How to structure data","Functions","Modules"]
    course_topics = set(course_topics)
    course_topics = list(set(course_topics))
    #sorted_course_topics = sorted(course_topics, key=str.lower)
    course_topics.sort()
    for topic in course_topics : 
        print("* " +topic)
        

    #step 2

    print("Problems:") 
    
    course_topics = list(set(course_topics))
    course_topics.sort()
    problem_dict = {"Problem 1" : 1, "Problem 2": 2, "Problem 3" : 3}
    problem_list = list(problem_dict)
    for topic in course_topics :
        print( "* " + topic + " : " + (", ") .join(problem_list))
    
    #Step 3

    print("Student Progress:")

    john = ("John", "Modules", "Problem 2","[GRADED]")
    david = ("David", "Tools of the Trade", "Problem 3", "[COMPLETED]")
    jacob = ("Jacob", "Functions", "Problem 1", "[COMPLETED]")
    eve = ("Eve","How to structure data","Problem 3","[STARTED]")
    anne = ("Anne", "How to make decision", "Problem 1", "[STARTED]")
   
    
    students = [john,david,jacob,eve,anne]
    students = sorted(students, key=lambda x: x[3], reverse=True)
    #students.sort(key=lambda x:x[3])
    i = 1
    while i < len(students):
    
        for student,topic,problems,status in students:
            print(f"{i}. {student} - {topic} - {problems} {status}")
            i += 1
        
    


    
if __name__ == "__main__":
    create_outline()
