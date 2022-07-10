import os

n = -1


class Record:
    index = []
    name = []
    rank = []
    branches = []
    city = []
    el_rank = []
    for i in range(50):
        index.append(-1)
        name.append('')
        rank.append(-1)
        branches.append(-1)
        city.append('')
        el_rank.append(-1)


rec = Record()


class College:
    arr = []
    num = -1
    col_rank, col_name, col_br, col_city, col_el = -1, '', -1, '', -1

    @staticmethod
    def add_record():
        global n
        n = int(input("Enter the number of colleges : "))
        print("Enter college name, college rank, no.of branches, city, eligibility rank")
        temp_num = 0
        if os.path.exists("nC.txt"):
            with open("nC.txt", 'r') as nf:
                if os.stat("nC.txt").st_size == 0:
                    nf.write('0')
                else:
                    temp_num = int(nf.read())
        else:
            with open("nC.txt", 'w') as temp_file:
                temp_file.write('0')
        k = n + temp_num
        for i in range(temp_num, k):
            print(f"College {i + 1}")
            temp_in = input().split()
            rec.name[i], rec.rank[i], rec.branches[i], rec.city[i], rec.el_rank[i] = temp_in[0], temp_in[1], temp_in[2], \
                                                                                     temp_in[3], temp_in[4]

    @staticmethod
    def create_file():
        global n
        with open("nC.txt", 'r') as nf:
            temp_num = nf.read()
        k = n + int(temp_num)
        with open("nC.txt", 'w') as nf_temp:
            nf_temp.write(str(k))
        j = int(k)
        with open("record.txt", 'a') as f:
            for i in range(int(temp_num), j):
                temp_f = f"{i + 1} {rec.rank[i]} {rec.name[i]} {rec.branches[i]} {rec.city[i]} {rec.el_rank[i]}\n"
                f.write(temp_f)

    @staticmethod
    def display():
        if os.stat("record.txt").st_size == 0:
            print("\nNo Colleges to display\n")
            return
        with open("record.txt", 'r') as f:
            for i in f:
                lines = i.split()
                print(
                    f"College Name : {lines[2]}\t\tRank : {lines[1]}\t\tNumber Of Branches : {lines[3]}\t\tCity : {lines[4]}\t\tEligible Rank : {lines[5]}")

    def delete_record(self):
        if os.stat("record.txt").st_size == 0:
            print("\nNo Colleges to delete\n")
            return
        self.arr = []
        self.num = -1
        name = input("Enter the name of the college you want to delete : ")
        with open("record.txt", 'r') as f:
            for i in f:
                self.arr.append(i)
        flag = False
        for i in range(len(self.arr)):
            temp = self.arr[i].split()
            for j in temp:
                if j == name:
                    flag = True
                    self.num = i
        if flag:
            self.delete()
            print("\nCollege deleted successfully\n")
        else:
            print("\nCollege Does not Exist\n")

    def delete(self):
        with open("record.txt", 'w') as f:
            j = 0
            for i in range(len(self.arr)):
                temp = self.arr[i].split()
                if i == self.num:
                    continue
                else:
                    temp_f = f"{j} {temp[1]} {temp[2]} {temp[3]} {temp[4]} {temp[5]}\n"
                    f.write(temp_f)
                    j += 1
        with open("nC.txt", 'r') as f:
            a = f.read()
        a = int(a) - 1
        if a == -1:
            a = 0
        with open("nC.txt", 'w') as f:
            f.write(str(a))

    def modify(self):
        if os.stat("record.txt").st_size == 0:
            print("\nNo Colleges to modify\n")
            return
        name = input("Enter the name of the College to modify : ")
        self.arr = []
        self.num = -1
        with open("record.txt", 'r') as f:
            for i in f:
                self.arr.append(i)
        flag = False
        for i in range(len(self.arr)):
            temp = self.arr[i].split()
            if name == temp[2]:
                flag = True
                self.num = i
                self.col_name, self.col_rank, self.col_br, self.col_city, self.col_el = temp[2], temp[1], temp[3], temp[
                    4], temp[5]
        if flag:
            print(f'''Choose an option
            1. Modify Name
            2. Modify Rank
            3. Modify Branches
            4. Modify Eligibility Rank
            5. Exit''')
            ch = int(input("Enter your choice : "))
            if ch == 1:
                self.col_name = input("Enter the new Name : ")
                print("Name Changed Successfully")
            elif ch == 2:
                self.col_rank = input("Enter the new Rank : ")
                print("Rank Changed Successfully")
            elif ch == 3:
                self.col_br = input("Enter the new Branches number : ")
                print("Branch Changed Successfully")
            elif ch == 4:
                self.col_el = input("Enter the new Eligibility Rank : ")
                print("Eligibility Changed Successfully")
            elif ch == 5:
                return
            else:
                print("\nInvalid Choice\n")
                return
            with open("record.txt", 'w') as f:
                j = 0
                for i in range(len(self.arr)):
                    temp = self.arr[i].split()
                    if i == self.num:
                        continue
                    else:
                        temp_f = f"{j} {temp[1]} {temp[2]} {temp[3]} {temp[4]} {temp[5]}\n"
                        f.write(temp_f)
                        j += 1
                temp_ff = f"{j} {self.col_rank} {self.col_name} {self.col_br} {self.col_city} {self.col_el}"
                f.write(temp_ff)
                print()
        else:
            print("\nCollege Does not exist\n")

    @staticmethod
    def search_college_rank():
        rank = input("Enter the College Rank : ")
        temp_rank = []
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp_rank.append(line)
        for i in range(len(temp_rank)):
            if temp_rank[i][1] == rank:
                print("\nCollege found\n")
                print(
                    f"College Name : {temp_rank[i][2]}\t\tRank : {temp_rank[i][1]}\t\tNumber Of Branches : {temp_rank[i][3]}\t\tCity : {temp_rank[i][4]}\t\tEligible Rank : {temp_rank[i][5]}")
                return
        print(f"\nCollege with the rank {rank} does not exist")

    @staticmethod
    def search_college_name():
        name = input("Enter the College Name : ")
        temp = []
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp.append(line)
        for i in range(len(temp)):
            if temp[i][2].lower() == name.lower():
                print("\nCollege found\n")
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")
                return
        print(f"\n{name} does not exist")

    @staticmethod
    def search_college_city():
        city = input("Enter the City Name : ")
        temp = []
        count = True
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp.append(line)
        for i in range(len(temp)):
            if temp[i][4].lower() == city.lower():
                count = False
                print("\nCollege found")
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")
        if count:
            print(f"\nCollege does not exist in {city}")

    @staticmethod
    def search_college_eRank():
        eRank = input("Enter the Eligible Rank : ")
        temp = []
        count = True
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp.append(line)
        for i in range(len(temp)):
            if temp[i][5] == eRank:
                count = False
                print("\nCollege found")
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")
        if count:
            print(f"\nCollege with Eligible rank {eRank} does not exist")

    @staticmethod
    def sort_college_rank():
        order = input("Sort by Ascending or Descending\nEnter A or D : ").lower()
        temp = College.bubble_sort(1)
        if order == 'a':
            for i in range(len(temp)):
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")
        elif order == 'd':
            for i in range(len(temp) - 1, -1, -1):
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")
        else:
            for i in range(len(temp)):
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")

    @staticmethod
    def sort_college_eRank():
        order = input("Sort by Ascending or Descending\nEnter A or D : ").lower()
        temp = College.bubble_sort(3)
        if order == 'a':
            for i in range(len(temp)):
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")
        elif order == 'd':
            for i in range(len(temp) - 1, -1, -1):
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")
        else:
            for i in range(len(temp)):
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")

    @staticmethod
    def sort_college_name():
        order = input("Sort by Ascending or Descending\nEnter A or D : ").lower()
        temp = College.bubble_sort(2)
        if order == 'a':
            for i in range(len(temp)):
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")
        elif order == 'd':
            for i in range(len(temp) - 1, -1, -1):
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")
        else:
            for i in range(len(temp)):
                print(
                    f"College Name : {temp[i][2]}\t\tRank : {temp[i][1]}\t\tNumber Of Branches : {temp[i][3]}\t\tCity : {temp[i][4]}\t\tEligible Rank : {temp[i][5]}")

    @staticmethod
    def bubble_sort(ch):
        if ch == 1:
            col = 1
        elif ch == 2:
            col = 2
        elif ch == 3:
            col = 5
        temp = []
        with open("record.txt", 'r') as f:
            for i in f:
                line = i.split()
                temp.append(line)
        if col == 2:
            for j in range(len(temp)):
                for i in range(0, len(temp) - j - 1):
                    if temp[i][col].lower() > temp[i + 1][col].lower():
                        temp[i], temp[i + 1] = temp[i + 1], temp[i]
        else:
            for j in range(len(temp)):
                for i in range(0, len(temp) - j - 1):
                    if int(temp[i][col]) > int(temp[i + 1][col]):
                        temp[i], temp[i + 1] = temp[i + 1], temp[i]
        return temp


def main():
    c = College()
    print(f'''
+------------------------------------------------+
|                                                |
|                                                |
|               University Of Four               |
|                                                |
|                                                |
+------------------------------------------------+
    ''')
    while True:
        print(f'''\nChoose an option
        1. For Admin
        2. For User
        3. To Exit''')
        ans = int(input("Enter your choice : "))
        if ans == 1:
            password = input("Enter the password : ")
            if password == "admin":
                print("\nAccess Granted")
                print("Welcome Admin\n")
                print(f'''Choose an option
                1. Add Data
                2. Modify Data
                3. Delete Data
                4. Display
                5. Exit''')
                ch = int(input("Enter your choice : "))
                if ch == 1:
                    c.add_record()
                    c.create_file()
                elif ch == 2:
                    c.modify()
                elif ch == 3:
                    c.delete_record()
                elif ch == 4:
                    c.display()
                elif ch == 5:
                    break
                else:
                    print("\nInvalid Choice\n")
            else:
                print("\nInvalid Password\n")
        elif ans == 2:
            print(f'''Choose an option
            1. Display
            2. Search
            3. Exit''')
            ch = int(input("Enter your choice : "))
            if ch == 1:
                print(f'''Choose an option
                1. Display College's by Name
                2. Display College's by Rank
                3. Display College's by Eligible Rank
                4. Exit''')
                ch = int(input("Enter your choice : "))
                if ch == 1:
                    c.sort_college_name()
                elif ch == 2:
                    c.sort_college_rank()
                elif ch == 3:
                    c.sort_college_eRank()
                elif ch == 4:
                    break
                else:
                    print("\nInvalid Choice\n")
            elif ch == 2:
                print(f'''Choose an option
                1. Search by College rank
                2. Search by College name
                3. Search by City
                4. Search by Eligible Rank
                5. Exit''')
                ch = int(input("Enter your choice : "))
                if ch == 1:
                    c.search_college_rank()
                elif ch == 2:
                    c.search_college_name()
                elif ch == 3:
                    c.search_college_city()
                elif ch == 4:
                    c.search_college_eRank()
                elif ch == 5:
                    break
                else:
                    print("\nInvalid Choice\n")
            elif ch == 3:
                break
            else:
                print("\nInvalid Choice\n")
        elif ans == 3:
            print("\nSuccessfully Logged Out\n")
            break
        else:
            print("\nInvalid Choice\n")


main()
