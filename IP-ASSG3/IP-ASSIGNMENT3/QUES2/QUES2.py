data_file = open("QUES2/sorted_data_q2.txt", "r")
out = open("QUES2/out_q2.txt", "w")
out.write("-----------------\n")

#To make the nested dictionary
lines = data_file.readlines()
records = {}
for l in lines[1:]:
    l = l[:-1]
    name = l.split(", ")[0]
    temp = {}
    temp["crossing"], temp["gate"], temp["time"] = l.split(", ")[1:]
    if name not in records.keys():
        records[name] = []
        records[name].append(temp)
    else:
        if records[name][-1]["crossing"] == temp["crossing"]:
            if temp["crossing"] == "ENTER": continue
            else: records[name][-1] = temp
        else: records[name].append(temp)

open("QUES2/file_dict.txt", "w").write(str(records))

while(True):
    print('''
    1. Status and details of the student
    2. Number of students entered/exited the campus in a given time frame
    3. Number of students entered/exited from a specific gate'''
    )
    n = input("Enter the task index: ")

    if not n:
        out.close()
        break

    n = int(n)

    if n == 1:
        st = input("Enter the name of the student: ")
        t = int(input("Enter the time[HH:MM:SS]: ").replace(":", ""))
        for i in range(len(records[st]) - 1):
            lst = records[st]
            if (lst[i]["crossing"] == "ENTER" and t>=int(lst[i]["time"].replace(":", ""))) and  (lst[i+1]["crossing"] == "EXIT" and t<=int(lst[i+1]["time"].replace(":", ""))):
                status = "PRESENT"
                break
            else:
                status = "NOT PRESENT"
        out.write(str(records[st]) + "\n")
        out.write("Status: " + status + "\n")
        out.write("-----------------\n")

    elif n == 2:
        n_enter, n_exit = 0, 0
        start = int(input("Enter the start time[HH:MM:SS]: ").replace(":", ""))
        end = int(input("Enter the end time[HH:MM:SS]: ").replace(":", ""))

        for i in records.values():
            for j in i:
                if j["crossing"] == "ENTER" and start<=int(j["time"].replace(":", "")) and end>=int(j["time"].replace(":", "")): n_enter+=1
                if j["crossing"] == "EXIT" and start<=int(j["time"].replace(":", "")) and end>=int(j["time"].replace(":", "")): n_exit+=1
        out.write("No. of students entered: " + str(n_enter) + "\n")
        out.write("No. of students exited: " + str(n_exit) + "\n")
        out.write("-----------------\n")

    elif n == 3:
        n_enter, n_exit = 0, 0
        gt = input("Enter gate number: ")
        for i in records.values():
            for j in i:
                if j["gate"] == gt and j["crossing"] == "ENTER": n_enter+=1
                if j["gate"] == gt and j["crossing"] == "EXIT": n_exit+=1
        out.write("No. of students entered: " + str(n_enter) + "\n")
        out.write("No. of students exited: " + str(n_exit) + "\n")
        out.write("-----------------\n")


out.close()