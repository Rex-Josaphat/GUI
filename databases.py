from tkinter import *
import sqlite3

root = Tk()
root.title('Accessing Databases')
root.geometry('400x400')

# create or connect to database
'''when the dtabases is not yet created kinter creates 
   it and saves it in the directory we are working in.'''
con = sqlite3.connect('addres_log.db')

# Creating a cursor
''' A cursor is sth you just send to some stuff with the database.
   you send it and it comes back with the result'''
c = con.cursor()

# create a database table
# c.execute('''CREATE TABLE addreses(
#             first_name text,
#             last_name text,
#             addres text,
#             city text,
#             town text,
#             zipcode integer
#             )''')

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='addreses' ''')

# if the count is 1, then table exists
if c.fetchone()[0] == 1:
    print('Table exists.')


    # create submit function
    def submit():
        '''You need to connect to the data base fist and create a cursor inside the function, commit and close the connection'''
        con = sqlite3.connect('address_log.db')
        c = con.cursor()

        # Insert into table
        '''Here instead of doctype strings use placeholder variables'''
        c.execute('INSERT INTO addreses VALUES(:f_name, :l_name, :addres, :city, :town, :zipcode)',
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'addres': addres.get(),
                      'city': city.get(),
                      'town': town.get(),
                      'zipcode': zipcode.get()

                  })

        con.commit()
        con.close()

        # Clear text boxes
        f_name.delete(0, END)
        l_name.delete(0, END)
        addres.delete(0, END)
        city.delete(0, END)
        town.delete(0, END)
        zipcode.delete(0, END)


    def delete():
        con = sqlite3.connect('address_log.db')
        c = con.cursor()

        # Delete a record
        c.execute('DELETE from addreses WHERE oid = ', delete_box.get())
        delete_box.delete(0, END)

        con.commit()
        con.close()


    def query():
        '''You need to connect to the data base fist and
            create a cursor inside the function, commit and close the connection'''
        con = sqlite3.connect('address_log.db')
        c = con.cursor()

        # query the database
        c.execute('SELECT *, oid FROM addreses')
        records = c.fetchall()  # retuns the elements in the query
        # print records
        print(records)

        # Loop through results
        print_results = ''
        for record in records:
            print_results += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'

        con.commit()
        con.close()

    def save():
        con = sqlite3.connect('address_log.db')
        c = con.cursor()

        record_id = delete_box.get()
        c.execute('''UPDATE addreses SET
            first_name = :first,
            last_name = :last,
            addres = :addres,
            city = :city,
            town = :town,
            zipcode = :zipcode
            
            WHERE oid = :oid''',
            {'first': f_name_editor.get(),
             'last': l_name_editor.get(),
             'addres': addres_editor.get(),
             'city': city_editor.get(),
             'town': town_editor.get(),
             'zipcode': zipcode_editor.get(),
             'oid': record_id
            })

        con.commit()
        con.close()

        editor.destroy()

    # Create edit function
    def edit():
        global editor
        editor = Tk()
        editor.title('Change records')
        editor.geometry('400x300')

        '''You need to connect to the data base fist and
                    create a cursor inside the function, commit and close the connection'''
        con = sqlite3.connect('address_log.db')
        c = con.cursor()

        record_id = delete_box.get()

        # query the database
        c.execute('SELECT * FROM addreses WHERE oid = ' + record_id)
        records = c.fetchall()  # retuns the elements in the query

        # Create global variables for the new text boxes
        global f_name_editor
        global l_name_editor
        global addres_editor
        global city_editor
        global town_editor
        global zipcode_editor


        # creating text boxes
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1, padx=20)

        addres_editor = Entry(editor, width=30)
        addres_editor.grid(row=2, column=1, padx=20)

        city_editor = Entry(editor, width=30)
        city_editor.grid(row=3, column=1, padx=20)

        town_editor = Entry(editor, width=30)
        town_editor.grid(row=4, column=1, padx=20)

        zipcode_editor = Entry(editor, width=30)
        zipcode_editor.grid(row=5, column=1, padx=20)

        # Entry box labels
        f_name_label = Label(editor, text='First name:', anchor=W).grid(row=0, column=0, pady=(10, 0))
        l_name_label = Label(editor, text='Last name:', anchor=W).grid(row=1, column=0)
        addres_label = Label(editor, text='addres:', anchor=W).grid(row=2, column=0)
        city_label = Label(editor, text='City:', anchor=W).grid(row=3, column=0)
        town_label = Label(editor, text='town:', anchor=W).grid(row=4, column=0)
        zipcode_label = Label(editor, text='Zipcode:', anchor=W).grid(row=5, column=0)
        quit = Button(editor, text='Exit!', command=root.quit).grid(row=14, column=0, columnspan=3)

        # Loop through result
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            addres_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            town_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

        # Create button to save new records
        save_btn = Button(editor, text='Save Record', command=save)
        save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=10)

    # creating text boxes
    f_name = Entry(root, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name = Entry(root, width=30)
    l_name.grid(row=1, column=1, padx=20)

    addres = Entry(root, width=30)
    addres.grid(row=2, column=1, padx=20)

    city = Entry(root, width=30)
    city.grid(row=3, column=1, padx=20)

    town = Entry(root, width=30)
    town.grid(row=4, column=1, padx=20)

    zipcode = Entry(root, width=30)
    zipcode.grid(row=5, column=1, padx=20)

    delete_box = Entry(root, width=30)
    delete_box.grid(row=9, column=1, padx=20, pady=7)

    # Entry box labels
    f_name_label = Label(root, text='First name:', anchor=W).grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(root, text='Last name:', anchor=W).grid(row=1, column=0)
    addres_label = Label(root, text='addres:', anchor=W).grid(row=2, column=0)
    city_label = Label(root, text='City:', anchor=W).grid(row=3, column=0)
    town_label = Label(root, text='town:', anchor=W).grid(row=4, column=0)
    zipcode_label = Label(root, text='Zipcode:', anchor=W).grid(row=5, column=0)
    delete_box_label = Label(root, text='Select ID:').grid(row=9, column=0, pady=5)

    # Create query button
    '''Button that will get what in the database and put it on the screen'''
    query_btn = Button(root, text='Show Records', command=query).grid(row=7, column=0, columnspan=2, padx=10, pady=10,
                                                                      ipadx=30)

    # Create a delete button to delete records
    del_btn = Button(root, text='Delete Record', command=delete).grid(row=10, column=0, columnspan=2, padx=10, pady=7,
                                                                      ipadx=30)

    # Create an update button
    '''Butoon that will allow us to edit data inside database table'''
    edit_btn = Button(root, text='Edit Record', command=edit).grid(row=11, column=0, columnspan=2, padx=10, pady=7,
                                                                   ipadx=30)

    # SUbmitt button
    btn = Button(root, text='Submit', command=submit).grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=50)

    quit = Button(root, text='Exit!', command=root.quit).grid(row=14, column=0, columnspan=3)

else:
    lab = Label(root,
                text='The database table stated does not exist!\n Create it first and be able to access the database!').grid(
        row=0, column=0)

# commit changes
con.commit()

# automatically close database
con.close()

root.mainloop()
