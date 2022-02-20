from tkinter import *
from PIL import ImageTk, Image
# ----------------------------Classes With Tkinder GUI ----------------------------------
import mysql.connector
from PIL.Image import ID
import time
from mysql.connector import Error, cursor
from pywin.framework.editor import frame
root = Tk()
root.title("Data Validator")
root.geometry("600x400")
root.configure(background='yellow2')

# Create the class with Database function
class MySqlloadFromDatafiles():
    def __init__(self, master):
        # Variables delcaration
        self.mydb = None
        self.mydbhost = None  
        self.mydbuser = None 
        self.mydbpwd = None 
        self.mydbname = None 
        # self.myUserData = None #'E:\\PythonCode\\Extra\\DDBValues_New2.csv'
        self.mydbquery = None
        self.timestus_label = None
        # "LOAD DATA LOCAL INFILE 'E:/PythonCode/Extra/DDBValues_New3.dat' INTO TABLE datavalidator.userinfo FIELDS TERMINATED BY '|' IGNORE 1 LINES;"
        # File Menu Creation
        frame = LabelFrame(master, text="MySQL-Export Data into Tables", padx=150, pady=75)
        frame.pack(padx=10, pady=10)
        # frame.grid(row=0, column=0, columnspan=2)
        frame.configure(background='light goldenrod')
        my_menu = Menu(frame)
        root.config(menu=my_menu)
        file_menu = Menu(my_menu)
        my_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_cascade(label='Quit', command=root.quit)
        # DBNAME
        dbname_labl = Label(frame, text='DB NAME:')
        dbname_labl.grid(row=1, column=0)
        dbname = Entry(frame, width=30)
        dbname.grid(row=1, column=1)
        # DBHOST
        dbhost_labl = Label(frame, text='DB HOST:')
        dbhost_labl.grid(row=2, column=0)
        dbhost = Entry(frame, width=30)
        dbhost.grid(row=2, column=1)
        # DBUSER
        dbuser_labl = Label(frame, text='DB USER:')
        dbuser_labl.grid(row=3, column=0)
        dbuser = Entry(frame, width=30)
        dbuser.grid(row=3, column=1)
        # DBPassCode
        dbpwd_labl = Label(frame, text='DB PASS CODE:')
        dbpwd_labl.grid(row=4, column=0)
        dbpwd = Entry(frame, width=30)
        dbpwd.grid(row=4, column=1)
        # DBQUERY
        dbqry_labl = Label(frame, text='DB QUERY Or FILE INFO:')
        dbqry_labl.grid(row=5, column=0)
        dbqry = Entry(frame, width=30)
        dbqry.grid(row=5, column=1)
        # Get all the text box values
        fdbname = dbname.get()
        fdbhost = dbhost.get()
        fdbuser = dbuser.get()
        fdbpwd = dbpwd.get()
        fdbqry = dbqry.get()
        print(f'self:-{fdbname},{fdbhost},{fdbuser},{fdbpwd},{fdbqry}')
        # Button Creation
        submit_btn = Button(frame, text="Submit", command=lambda: self.submit(dbname.get(), dbhost.get(), dbuser.get(), dbpwd.get(),dbqry.get()))
        submit_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=50)
        #timestus_label=Label(frame)
        #timestus_label.grid(row=8, column=0)
    # pass
    def submit(self, fdbname, fdbhost, fdbuser, fdbpwd, fdbqry):
        print(f'Def Output:- {fdbname},{fdbhost},{fdbuser},{fdbpwd},{fdbqry}')
        self.mydb = mysql.connector.connect(host=fdbhost, user=fdbuser, password=fdbpwd, database=fdbname,
                                            allow_local_infile=True)
        #mydbquery = ("SELECT ID,FName,LName INTO OUTFILE 'E:/PythonCode/Extra/file_1.csv' FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' FROM datavalidator.userinfo;")
        fdbquery = ("SELECT ID,FName,LName INTO OUTFILE '"+fdbqry+"' FIELDS TERMINATED BY '|' LINES TERMINATED BY '\n' FROM datavalidator.userinfo;")
        #fdbquery = ("LOAD DATA LOCAL INFILE  '" + fdbqry + "'INTO TABLE datavalidator.userinfo FIELDS TERMINATED BY '|' IGNORE 1 LINES;")
        print(fdbquery)
        self._start_time = time.perf_counter()
        #self.mysqldbCon(fdbhost,fdbuser,fdbpwd,fdbname,fdbquery)
        try:
            mysqlConString = self.mydb.get_server_info()
            print('Connected to MySQL Server!',mysqlConString)
            if (self.mydb.is_connected()):
                #object.close()
                #return mydb
                cursor_1 = self.mydb.cursor()
                cursor_1.execute(fdbquery)
                # record_1 = cursor_1.fetchone()
                # print("Row Values----->",record_1)
                # cursor_1.commit()
                """#for i in rowcount:
                record_1=cursor_1.fetchone()
                #print(type(record_1))

                #print("Row Values----->",record_1)
                while record_1 is not None:
                    #print(record_1)
                    record_1=cursor_1.fetchone()
                    print("Row Values----->", record_1)"""
                #mysqldbConRecord(mydb,mydbquery)
                self.mydb.commit()
                #print(self.mydb.fetch_eof_status())
                print("DB Data Exported")
            else:
                print("DB isn't Established")
        except Error as e:
            print("DB Connection Error",e)
        finally:
            if (self.mydb.is_connected()):
                self.mydb.close()
                print("DB Connection is Closed!!!")

    #def displaytimer(self):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
# end of the function
myclass = MySqlloadFromDatafiles(root)
root.mainloop()