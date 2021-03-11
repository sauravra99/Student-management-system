from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class student: 
	def __init__(self,root):
		self.root=root
		self.root.title("Student Management System")
		self.root.geometry("1350x700+0+0")

		title=Label(self.root, text="Student Management System",bd=10, relief=GROOVE, font=("Arial", 40, "bold"), bg="#000000", fg="#ffffff")
		title.pack(side=TOP, fill=X)

		title=Label(self.root, text="",bd=10, relief=GROOVE, font=("Arial", 15, "bold"), bg="#000000", fg="#ffffff")
		title.pack(side=BOTTOM, fill=X)

		#========variables=======

		self.Roll_no_var=StringVar()
		self.Name_var=StringVar()
		self.Email_var=StringVar()
		self.Gender_var=StringVar()
		self.Contact_var=StringVar()
		self.DOB_var=StringVar()
		self.Search_by=StringVar()
		self.Seach_txt=StringVar()
		

		#-------------Manage frame-----------------

		Manage_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="#33CFFF")
		Manage_Frame.place(x=20,y=100,width=450, height=580)

		m_title=Label(Manage_Frame, text="Manage Student", font=("Arial", 25, "bold"), bg="#33CFFF", fg="#000000")
		m_title.grid(row=0, columnspan=2, pady=20)

		#roll number
		lbl_roll=Label(Manage_Frame, text="Roll No.", font=("Arial", 15), bg="#33CFFF", fg="#000000")
		lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

		txt_Roll=Entry(Manage_Frame,font=("Arial", 12),textvariable=self.Roll_no_var, bd=5, relief=GROOVE, bg="#ffffff", fg="#000000")
		txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")


		#name
		lbl_name=Label(Manage_Frame, text="Name", font=("Arial", 15), bg="#33CFFF", fg="#000000")
		lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

		txt_Name=Entry(Manage_Frame,font=("Arial", 12),textvariable=self.Name_var, bd=5, relief=GROOVE, bg="#ffffff", fg="#000000")
		txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

		
		#E-mail
		lbl_email=Label(Manage_Frame, text="E-mail", font=("Arial", 15), bg="#33CFFF", fg="#000000")
		lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

		txt_Email=Entry(Manage_Frame,font=("Arial", 12),textvariable=self.Email_var, bd=5, relief=GROOVE, bg="#ffffff", fg="#000000")
		txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

		#phone number
		lbl_conatct=Label(Manage_Frame, text="Contact No.", font=("Arial", 15), bg="#33CFFF", fg="#000000")
		lbl_conatct.grid(row=4, column=0, pady=10, padx=20, sticky="w")

		txt_Contact=Entry(Manage_Frame,font=("Arial", 12),textvariable=self.Contact_var, bd=5, relief=GROOVE, bg="#ffffff", fg="#000000")
		txt_Contact.grid(row=4, column=1, pady=10, padx=20, sticky="w")

		#Gender
		lbl_gender=Label(Manage_Frame, text="Gender", font=("Arial", 15), bg="#33CFFF", fg="#000000")
		lbl_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")

		combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var, font=("Arial", 11))
		combo_Gender['values']=("Male", "Female", "Other")
		combo_Gender.grid(row=5, column=1, pady=10, padx=20, sticky="w")

		#D.O.B
		lbl_dob=Label(Manage_Frame, text="D.O.B(dd-mm-yyyy)", font=("Arial", 15), bg="#33CFFF", fg="#000000")
		lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

		txt_DOB=Entry(Manage_Frame,font=("Arial", 12), textvariable=self.DOB_var,bd=5, relief=GROOVE, bg="#ffffff", fg="#000000")
		txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")
		
		#Address
		lbl_add=Label(Manage_Frame, text="Address", font=("Arial", 15), bg="#33CFFF", fg="#000000")
		lbl_add.grid(row=7, column=0, pady=10, padx=20, sticky="w")

		self.txt_address=Text(Manage_Frame, width=27, height=3, font=("Arial", 10))
		self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

		#==============buttons================

		btn_Frame=Frame(Manage_Frame, bd=5, bg="black")
		btn_Frame.place(x=1, y=480, width=440)

		Addbtn=Button(btn_Frame, text="Add", width=10, command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
		deletebtn=Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=1, padx=10, pady=10)
		updatebtn=Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=2, padx=10, pady=10)
		clearbtn=Button(btn_Frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)


		#-----------detail frame-------------------
		Detail_Frame=Frame(self.root, bd=4, relief=RIDGE, bg="#33CFFF")
		Detail_Frame.place(x=500,y=100,width=800, height=580)

		lbl_search=Label(Detail_Frame, text="Search By", font=("Arial", 15), bg="#33CFFF", fg="#000000")
		lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

		combo_search=ttk.Combobox(Detail_Frame, textvariable=self.Search_by ,width=10, font=("Arial", 11))
		combo_search['values']=("Roll_no", "Name", "Contact")
		combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

		txt_search=Entry(Detail_Frame,width=15,textvariable=self.Seach_txt, font=("Arial", 12), bd=5, relief=GROOVE, bg="#ffffff", fg="#000000")
		txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

		Searchbtn=Button(Detail_Frame, text="Search", width=10, command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
		Showallbtn=Button(Detail_Frame, text="Show all", width=10, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
		
		#---------------table frame--------------
		Table_Frame=Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#ffffff")
		Table_Frame.place(x=20,y=50,width=750, height=500)
		
		scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
		self.Student_table=ttk.Treeview(Table_Frame, column=("Roll", "Name", "E-mail", "Gender", "Contact", "DOB", "Address"),
		 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM, fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)
		self.Student_table.heading("Roll", text="Roll no.")
		self.Student_table.heading("Name", text="Name")
		self.Student_table.heading("E-mail", text="E-mail")
		self.Student_table.heading("Gender", text="Gender")
		self.Student_table.heading("Contact", text="Contact")
		self.Student_table.heading("DOB", text="DOB")
		self.Student_table.heading("Address", text="Address")	
		self.Student_table['show']='headings'
		self.Student_table.column("Roll", width=100)
		self.Student_table.column("Name", width=100)
		self.Student_table.column("E-mail", width=100)
		self.Student_table.column("Gender", width=100)
		self.Student_table.column("Contact", width=100)
		self.Student_table.column("DOB", width=100)
		self.Student_table.column("Address", width=150)
		self.Student_table.pack(fill=BOTH, expand=1)
		self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
		self.fetch_data()	

		#=====functions=====

	def add_students(self):
		if self.Roll_no_var.get()=="" or self.Name_var.get()=="" and Email_var.get():
			messagebox.showerror("Error","All fields are required!!!!!")
		else:	
			con=mysql.connector.connect(host='localhost',user='root',password='pumaraja',database='stm')
			cur=con.cursor()
			cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",
			(
				self.Roll_no_var.get(),
				self.Name_var.get(),
				self.Email_var.get(),
				self.Gender_var.get(),
				self.Contact_var.get(),
				self.DOB_var.get(),
				self.txt_address.get('1.0', END)
				)
			)
			con.commit()
			self.fetch_data()
			con.close()
			messagebox.showinfo("Success","Record has been inserted")

	def fetch_data(self):
		con=mysql.connector.connect(host='localhost',user='root',password='pumaraja',database='stm')
		cur=con.cursor()
		cur.execute("select * from student")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('', END, values=row)
			con.commit()
		self.clear()
		con.close()

	def clear(self):
		self.Roll_no_var.set(""),
		self.Name_var.set(""),
		self.Email_var.set(""),
		self.Gender_var.set(""),
		self.Contact_var.set(""),
		self.DOB_var.set(""),
		self.txt_address.delete('1.0', END)

	def get_cursor(self, ev):
		cursor_row=self.Student_table.focus()
		content=self.Student_table.item(cursor_row)
		row=content['values']
		self.Roll_no_var.set(row[0]),
		self.Name_var.set(row[1]),
		self.Email_var.set(row[2]),
		self.Gender_var.set(row[3]),
		self.Contact_var.set(row[4]),
		self.DOB_var.set(row[5]),
		self.txt_address.delete('1.0', END)
		self.txt_address.insert(END, row[6])

	def update_data(self):
		con=mysql.connector.connect(host='localhost',user='root',password='pumaraja',database='stm')
		cur=con.cursor()
		cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s ",
		 (
		 	self.Name_var.get(),
		 	self.Email_var.get(),
		 	self.Gender_var.get(),
		 	self.Contact_var.get(),
		 	self.DOB_var.get(),
		 	self.txt_address.get('1.0', END),
		 	self.Roll_no_var.get()
		 	)
		 )
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

	def delete_data(self):
		con=mysql.connector.connect(host='localhost',user='root',password='pumaraja',database='stm')
		cur=con.cursor()
		cur.execute("delete from student where roll_no like '%"+str(self.Roll_no_var.get())+"%'" )
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()	

	def search_data(self):
		con=mysql.connector.connect(host='localhost',user='root',password='pumaraja',database='stm')
		cur=con.cursor()
		cur.execute("select * from student where " + str(self.Search_by.get())+" like '%"+str(self.Seach_txt.get() )+"%'" )
		rows=cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('', END, values=row)
			con.commit()
		self.clear()
		con.close()


root=Tk()
ob=student(root)
root.mainloop()