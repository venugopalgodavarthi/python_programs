import pymysql
dbconn = pymysql.connect(host='127.0.0.1', port=3306,
                         user='root', password='root', database='hoilday')
print(dbconn)
cur = dbconn.cursor()
print(cur)


def table_creating():
    dbconn = pymysql.connect(host='127.0.0.1', port=3306,
                             user='root', password='root', database='hoilday')
    print(dbconn)
    cur = dbconn.cursor()
    print(cur)
    cur.execute(
        "create table student(id int primary key, name varchar(50), phone bigint unique, email varchar(50) unique, age int)")
    print(cur.rowcount)
    dbconn.commit()
    dbconn.close()


class student:
    stud_count = 1

    def create(self, name, phone, email, age):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.stu_count_inc()
        self.id = self.stud_count
        n = int(
            input("choose the option\npress1: create a account\npress2: exit\noption:"))
        match n:
            case 1:
                self.createdetails(self.id, self.name,
                                   self.phone, self.email, self.age)
                print("Details created successfully")
            case 2:
                print("Thank you for visiting")

    @classmethod
    def stu_count_inc(cls):
        cls.stud_count += 1

    def createdetails(self, id, name, phone, email, age):
        val = [id, name, phone, email, age]
        cur.execute(
            "insert into student (id,name,phone,email,age) values (%s,%s,%s,%s,%s)", val)
        print(cur.rowcount)
        dbconn.commit()

    def getdetails(self):
        cur.execute("select * from student")
        print(cur.rowcount)
        res = cur.fetchall()
        for i in res:
            print(i)

    def details(self, pk):
        val = [pk]
        cur.execute("select * from student where id= %s", val)
        print(cur.rowcount)
        res = cur.fetchone()
        print(res)

    def update_phone(self, pk, phone):
        val = [phone, pk]
        cur.execute("update student set phone= %s where id= %s", val)
        print(cur.rowcount, 'row is affected')
        dbconn.commit()
        print("mobile number is updated")

    def delete_record(self, pk):
        val = [pk]
        cur.execute("delete from student where id= %s", val)
        print(cur.rowcount, 'row is affected')
        print("record is deleted")
        dbconn.commit()

    def closeconn(self):
        dbconn.close()
        print("sql conncetion is disable")


obj = student()
# obj.create('rani', 9988664422, 'rani@gmail.com', 23)
# obj.getdetails()
# obj.details(2)
# obj.update_phone(2, 9966332255)
# obj.delete_record(2)
obj.closeconn()
print(dbconn)
