import time
out = open("QUES6/q6_output.txt", "w")
out.write('''
Advantages of OOP:
    1) Allows user to create self defined data-types and classses
    2) Allows user to create operations of there choice on the objects, 
    this also allows clubbing various functions of a pirtucular data-type

Advantages of Dictionary:
    1) Allows mapping elements with familiar keys thus reducing cognitive load of the reader and editor of the code
    2) Nested dictionary or dictionary combined with lists, tuples allows us to store multitude of data easily and in a mappable format, similarly linking dictionaries opens variety
    of tasks that can be performed with dictionaries

Disadvantages of OOP:
    1) Makes syntax more complicated which troubles in debugging
    2) Increases the length of code

Disadvantages of Dictionary:
    1) Dictionaries are not indexed and ordered
    2) Keys are limited and we cant keep increasing like indexes in lists etc.
|-----------------------------------------------------------------------------------|
''')

print("CLASS METHOD")

f = 0
if f==0:
    #classes
    class Course:
        def __init__(self, name, cred, assesm, grads):
            self.name = name
            self.credits = cred
            self.assessments = assesm
            self.policy = grads

        def grading(self, scr):
            pol = self.policy
            if scr>=pol[0]: return "A"
            elif scr>=pol[1]: return "B"
            elif scr>=pol[2]: return "C"
            else: return "F"

    class Student:
        def __init__(self, roll, marks):
            self.roll = roll
            self.marks = marks

        def score_calc(self):
            return sum(self.marks)

        def assess(self):
            return self.marks

    #Function to compile data from file
    def data_std(add):
        std_data = {}
        inp = open(add, "r")
        lines = inp.readlines()
        for l in lines:
            temp = list(map(int, l.replace("\n", "").split(", ")))
            std_data[temp[0]] = Student(temp[0], temp[1:])

        return std_data

    #other functions
    def scores_of_all(d):
        total_scores = {}
        for k, v in d.items():
            total_scores[k] = v.score_calc()

        return total_scores

    def mid_val(l):
        delta = -1
        for i in range(len(l)-1):
            ch = l[i] - l[i+1]
            if ch>delta:
                delta = ch
                mid = (l[i] + l[i+1])/2
        return mid

    def normalizePolicy(pol, scores):
        final_scores = list(scores.values())
        for i in range(len(pol)):
            temp2 = [x for x in final_scores if (x>=pol[i]-2 and x<=pol[i]+2)]
            if not temp2:
                continue
            elif len(temp2) == 1:
                pol[i] = temp2[0]
            else:
                pol[i] = mid_val(temp2)

        return pol

    def grade_all(crs, scrs):
        grds = {}
        for k, v in scrs.items():
            grds[k] = [v, crs.grading(v)]

        return grds

    def gradeCounter(grds, g):
        count = 0
        for v in list(grds.values()):
            if v[1] == g: count +=1

        return count

    if __name__ == "__main__":
        assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
        assessments = dict(assessments)
        policy = [80, 65, 50, 40]

        oop_grade_t0 = time.time()
        for i in range(1000):
            data_marks = data_std("QUES4/marks.txt")
            data_scores = scores_of_all(data_marks)
            policy_new = normalizePolicy(policy, data_scores)

            ip = Course("IP", 4, assessments, policy_new)
            data_grades = grade_all(ip, data_scores)

        oop_grade_time = time.time() - oop_grade_t0

        oop_search_time  = 0
        while(True):
            print('''
            1. Generate summary
            2. Grades of all students
            3. Search for student records
            4. Close
            ''')

            task = int(input("Enter the task index: "))

            if task == 4: break
            elif task == 1:
                print(f'''

                Course: {ip.name}
                Credit: {ip.credits}
                Assessment: {ip.assessments}
                Cutoffs: {ip.policy}

                Counts:-
                A: {gradeCounter(data_grades, "A")}
                B: {gradeCounter(data_grades, "B")}
                C: {gradeCounter(data_grades, "C")}
                D: {gradeCounter(data_grades, "D")}
                F: {gradeCounter(data_grades, "F")}

                ''')
            
            elif task == 2:
                out = open("QUES4/grades.txt", "w")
                for r in data_grades:
                    tot = data_grades[r][0]
                    g = data_grades[r][1]
                    out.write(f"{r}, {tot}, {g}\n")
                out.close()

            elif task == 3:
                x = int(input("Enter the roll number: "))
                oop_search_t0 = time.time()
                for i in range(1000):
                    search_res = f'''

                    Roll no.: {x}
                    Assessments: {data_marks[x].assess()}
                    Total Marks and Grades: {data_grades[x]}

                    '''
                oop_search_time = time.time() - oop_search_t0

                print(search_res)
    f = 1
f = 1
if f==1:
    print("WITHOUT CLASSES")

    #Function to compile data from file
    def data_std(add):
        std_data = {}
        inp = open(add, "r")
        lines = inp.readlines()
        for l in lines:
            temp = list(map(int, l.replace("\n", "").split(", ")))
            std_data[temp[0]] = temp[1:]

        return std_data

    #other functions
    def grading(scr, pol):
            pol = policy
            if scr>=pol[0]: return "A"
            elif scr>=pol[1]: return "B"
            elif scr>=pol[2]: return "C"
            else: return "F"

    def scores_of_all(d):
        total_scores = {}
        for k, v in d.items():
            total_scores[k] = sum(v)

        return total_scores

    def mid_val(l):
        delta = -1
        for i in range(len(l)-1):
            ch = l[i] - l[i+1]
            if ch>delta:
                delta = ch
                mid = (l[i] + l[i+1])/2
        return mid

    def normalizePolicy(pol, scores):
        final_scores = list(scores.values())
        for i in range(len(pol)):
            temp2 = [x for x in final_scores if (x>=pol[i]-2 and x<=pol[i]+2)]
            if not temp2:
                continue
            elif len(temp2) == 1:
                pol[i] = temp2[0]
            else:
                pol[i] = mid_val(temp2)

        return pol

    def grade_all(scrs, pol):
        grds = {}
        for k, v in scrs.items():
            grds[k] = [v, grading(v, pol)]

        return grds

    def gradeCounter(grds, g):
        count = 0
        for v in list(grds.values()):
            if v[1] == g: count +=1

        return count

    if __name__ == "__main__":
        name, credits = "IP", 4
        assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
        assessments = dict(assessments)
        policy = [80, 65, 50, 40]

        dict_grade_t0 = time.time()
        for i in range(1000):
            data_marks = data_std("QUES5/marksq5.txt")
            data_scores = scores_of_all(data_marks)
            policy_new = normalizePolicy(policy, data_scores)
            data_grades = grade_all(data_scores, policy_new)
        dict_grade_tf = time.time() - dict_grade_t0
        dict_search_tf = 0
        while(True):
            print('''
            1. Generate summary
            2. Grades of all students
            3. Search for student records
            4. Close
            ''')

            task = int(input("Enter the task index: "))

            if task == 4: break
            elif task == 1:
                print(f'''

                Course: {name}
                Credit: {credits}
                Assessment: {assessments}
                Cutoffs: {policy}

                Counts:-
                A: {gradeCounter(data_grades, "A")}
                B: {gradeCounter(data_grades, "B")}
                C: {gradeCounter(data_grades, "C")}
                D: {gradeCounter(data_grades, "D")}
                F: {gradeCounter(data_grades, "F")}

                ''')
            
            elif task == 2:
                out = open("QUES5/gradesq5.txt", "w")
                for r in data_grades:
                    tot = data_grades[r][0]
                    g = data_grades[r][1]
                    out.write(f"{r}, {tot}, {g}\n")
                out.close()

            elif task == 3:
                x = int(input("Enter the roll number: "))
                dict_search_t0 = time.time()
                for i in range(1000):
                    search_res2 = f'''

                    Roll no.: {x}
                    Assessments: {data_marks[x]}
                    Total Marks and Grades: {data_grades[x]}

                    '''
                dict_search_tf = time.time() - dict_search_t0
                print(search_res2)
fast_grade = "OOP" if oop_grade_time<dict_grade_tf else "DICTIONARY"
fast_search = "OOP" if oop_search_time<dict_search_tf else "DICTIONARY"
out.write(f'''
Performance comparison for grading operation:
1. N: 1000
2. Time by OO: {oop_grade_time}
3. Time by dictionary: {dict_grade_tf}
4. X is faster; fraction of time x took is: {fast_grade}, {min(oop_grade_time, dict_grade_tf)}; {min(oop_grade_time, dict_grade_tf)/max(oop_grade_time, dict_grade_tf)}

Performance comparison for search operation:
1. N: 1000
2. Time by OO: {oop_search_time}
3. Time by dictionary: {dict_search_tf}
4. X is faster; fraction of time x took is: {fast_search}, {min(oop_search_time, dict_search_tf)}; {min(oop_search_time, dict_search_tf)/max(oop_search_time, dict_search_tf)}
|-----------------------------------------------------------------------|
''')

out.close()