import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pathlib import Path
import os
from main import HDD, RAID

RESIZE = 8


RAID_LIST = []
hddList = []

# HDD1 = HDD('HDD01', 2)
# HDD2 = HDD('HDD02', 2)
# # HDD3 = HDD('HDD03', 2)
# # HDD4 = HDD('HDD04', 2)

# hddList.append(HDD1)
# hddList.append(HDD2)


# # hddList.append(HDD3)
# # hddList.append(HDD4)



R0 = RAID('RAID0', 0)
R1 = RAID('RAID1', 1)
R5 = RAID('RAID5', 5)
# R6 = RAID('RAID6', 6)

H1 = HDD('HDD1', 2)
H2 = HDD('HDD2', 2)
H3 = HDD('HDD3', 2)
H4 = HDD('HDD4', 1)

H5 = HDD('HDD5', 1)
H6 = HDD('HDD6', 1)
H7 = HDD('HDD7', 1)
H8 = HDD('HDD8', 2)

H9 = HDD('HDD9', 2)
H10 = HDD('HDD10', 1)
H11 = HDD('HDD11', 2)
H12 = HDD('HDD12', 1)

# H13 = HDD('HDD13', 2)
# H14 = HDD('HDD14', 2)
# H15 = HDD('HDD15', 2)
# H16 = HDD('HDD16', 2)

R0.addHDD(H1)
R0.addHDD(H2)
R0.addHDD(H3)
R0.addHDD(H4)

R1.addHDD(H5)
R1.addHDD(H6)
R1.addHDD(H7)
R1.addHDD(H8)

R5.addHDD(H9)
R5.addHDD(H10)
R5.addHDD(H11)
R5.addHDD(H12)

# R6.addHDD(H13)
# R6.addHDD(H14)
# R6.addHDD(H15)
# R6.addHDD(H16)




def has_duplicates(lst):
    return len(lst) != len(set(lst))



RAID_LIST.append(R0)
RAID_LIST.append(R1)
RAID_LIST.append(R5)
# RAID_LIST.append(R6)
# for i in R0.getRAIDLS():
#     print(f'NAME HDD : {i.getName()} CAPACITY : {i.getCapacity()}TB ')

# if isinstance(R0.getSUMcapacity(), int):
#     print(f'{R0.getSUMcapacity()}TB')
# else:
#     print(f'{R0.getSUMcapacity()}')


def on_raid_listbox_click(event):
    selected_index = RAID_Listbox.curselection()
    print(selected_index)
    if selected_index:
        for widget in LEFT_MID.winfo_children():
            widget.destroy()
        # for widget in RIGTH_FARME.winfo_children():
        #     widget.destroy()

        HHD_Listbox = tk.Listbox(LEFT_MID, width=50)
        HHD_Listbox.grid(rowspan=1, columnspan=2, sticky='nsew', padx=0)

        # Clear existing elements in the HHD_Listbox
        HHD_Listbox.delete(0, tk.END)
        #Raid  DATA
        index = 1
        print(selected_index[0])
        print(RAID_LIST[selected_index[0]].getRAIDLS())
        raid_index = selected_index[0]  # Get the selected RAID index

        if len(RAID_LIST[selected_index[0]].getRAIDLS()) != 0:
            for hdd in RAID_LIST[selected_index[0]].getRAIDLS():
                HHD_Listbox.insert(index, f'NAME HDD : {hdd.getName()} CAPACITY : {hdd.getCapacity()}TB ')
                index += 1

        else:
            HHD_Listbox.insert(1, "You need add HDD in RAID before Simulator ! ")
        # progress_bar = ttk.Progressbar(RIGTH_FARME, orient='horizontal', length=660, mode='determinate', variable=100)
        # progress_bar['value'] = 100
        # progress_bar.grid(row=0, column=0, padx=20, pady=30)
        # if isinstance(capacity, int):
        #     label_status = tk.Label(RIGTH_FARME,text=f'{capacity}TB')
        # else:
        #     label_status = tk.Label(RIGTH_FARME,text=f'{capacity}')

        #right frame show
# def show_left_info():
#    for i in RAID_LIST:
#         raid = i
#         capacity = raid.getSUMcapacity()
#         text_info = tk.Label(RIGTH_FARME, text=f'{i.name}')
#         text_info.pack(padx=5, pady=10)

#         if raid.getRAIDLS():
#             for hdd in raid.getRAIDLS():
#                 info_label = tk.Label(RIGTH_FARME, text=f'NAME HDD : {hdd.getName()} CAPACITY : {hdd.getCapacity()}TB')
#                 info_label.pack()
#         else:
#             info_label = tk.Label(RIGTH_FARME, text="You need to add HDDs in RAID before Simulator!")
#             info_label.pack()

#         capacity_label = tk.Label(RIGTH_FARME, text=f'Total Capacity: {capacity}TB')
#         capacity_label.pack(padx=20, pady=10)
def show_right_info():
    # Counter for managing the grid layout
    row_count = 0
    col_count = 0

    for i, raid in enumerate(RAID_LIST):
        capacity = raid.getSUMcapacity()
        # Create labels for RAID name and total capacity
        text_info = tk.Label(RIGTH_FARME, text=f'{raid.name}   LEVEL : {raid.getLevel()}',bg='#9290C3',fg="white",font="bold")
        text_info.grid(row=row_count, column=col_count, padx=5)

        capacity_label = tk.Label(RIGTH_FARME, text=f'Total Capacity: {capacity}TB',bg='#5F5D9C',fg="white")
        capacity_label.grid(row=row_count + 1, column=col_count, padx=20, pady=10)

        # Check if there are HDDs in the RAID
        if raid.getRAIDLS():
            # Display HDD information in the same column
            last_row = 0
            last_cou = 0
            for j, hdd in enumerate(raid.getRAIDLS()):
                info_label = tk.Label(RIGTH_FARME, text=f'NAME HDD : {hdd.getName()} CAPACITY : {hdd.getCapacity()}TB',bg='#5F5D9C',fg="white")
                info_label.grid(row=row_count + j + 2, column=col_count, padx=5)
                last_row = row_count + j + 2
                last_cou = col_count
            info_label = tk.Label(RIGTH_FARME, text=f'Read Speed : {raid.readSpeed()}X   Write Speed : {raid.writeSpeed()}X \n',bg='#5F5D9C',fg="white")
            info_label.grid(row=last_row+1, column=last_cou, padx=5)
        else:
            # If no HDDs, display a message
            info_label = tk.Label(RIGTH_FARME, text="You need to add HDDs in RAID before Simulator!")
            info_label.grid(row=row_count + 2, column=col_count, padx=5)

        # Increment column count for every RAID
        col_count += 1

        # Reset column count and increment row count every third RAID
        if (i + 1) % 3 == 0:
            col_count = 0
            row_count += 10  # Adjust as needed for proper spacing between RAID entries




def on_add_driver_click():
    def validate_capacity(new_value):
        if new_value.isdigit() or new_value == "":
            return True
        else:
            return False

    def create_hdd():
        hdd_name = name_entry.get()
        hdd_capacity = capacity_entry.get()
        # Validate input and create HDD object
        if hdd_name and hdd_capacity.isdigit():
            try:
                # Check if the HDD name already exists in the list
                if hdd_name not in [hdd.getName() for hdd in hddList]:
                    new_hdd = HDD(hdd_name, int(hdd_capacity))
                    status_label.config(
                        text=f"New HDD created: {new_hdd.getName()} with capacity {new_hdd.getCapacity()}TB",
                        fg="green")

                    # Clear the input boxes
                    name_entry.delete(0, tk.END)
                    capacity_entry.delete(0, tk.END)

                    hddList.append(new_hdd)
                    HDD_Listbox.insert(tk.END, f'NAME : {new_hdd.getName()}  CAPACITY : {new_hdd.getCapacity()}TB')
                    print("Added HDD")
                else:
                    status_label.config(text="Please use a different name", fg="red")
            except ValueError:
                status_label.config(text="Invalid capacity. Please provide a valid capacity.", fg="red")
        else:
            status_label.config(text="Invalid input. Please provide a valid name and capacity.", fg="red")

    popup_window = tk.Toplevel(window)
    popup_window.title("Add Driver")
    popup_window.geometry('400x500')

    # Top Frame for Image
    top_frame = tk.Frame(popup_window)
    top_frame.pack(side=tk.TOP, pady=10)

    # Use the resized_image_hardDisk in the top frame
    label = tk.Label(top_frame, image=resized_image_hardDisk)
    label.pack(pady=5)

    # Bottom Frame for Inputs
    bottom_frame = tk.Frame(popup_window)
    bottom_frame.pack(side=tk.TOP, pady=10)

    # Create an Entry widget for the name
    name_label = tk.Label(bottom_frame, text="Name:")
    name_label.pack(pady=5)

    name_entry = tk.Entry(bottom_frame)
    name_entry.pack(pady=5)
    name_entry.bind('<Return>', lambda event: create_hdd())  # Bind <Return> key to create_hdd function

    # Create an Entry widget for the capacity with validation
    capacity_label = tk.Label(bottom_frame, text="Capacity:")
    capacity_label.pack(pady=5)

    vcmd = (popup_window.register(validate_capacity), '%P')
    capacity_entry = tk.Entry(bottom_frame, validate="key", validatecommand=vcmd)
    capacity_entry.pack(pady=5)
    capacity_entry.bind('<Return>', lambda event: create_hdd())  # Bind <Return> key to create_hdd function

    # Status Label for success or failure message
    status_label = tk.Label(bottom_frame, text="", fg="black")
    status_label.pack(pady=5)

    # Add your other widgets and logic for the pop-up window here


# ...
def on_add_raid_click():
    Comboboxes = []
    def create_raid():
        global i
        raid_name = raid_name_entry.get()
        raid_level = raid_level_entry.get()
        Hdd_names = []
        for i in Comboboxes:
            Hdd_names.append(i.get())

        # Validate input and create RAID object
        if raid_name and raid_level.isdigit() and Hdd_names:

            if has_duplicates(Hdd_names):
                status_label.config(text="Invalid input. Please provide a Valid hdd input", fg="red")
                print("Duplicated")
                for i in Comboboxes:
                    i.delete(0, tk.END)

            else:
                new_raid = RAID(raid_name, int(raid_level))
                print(Hdd_names)
                for i in Hdd_names:
                    for j in hddList:
                        print(j.getName())
                        if i == j.getName():
                            new_raid.addHDD(j)
                            hddList.remove(j)
                RAID_LIST.append(new_raid)
                RAID_Listbox.insert(tk.END, new_raid.getName())
                status_label.config(
                    text=f"New RAID created: {new_raid.getName()} with RAID level {new_raid.getLevel()}",
                    fg="green")
                HDD_Listbox.delete(0,tk.END)
                popup_window.destroy()

                for widgets in RIGTH_FARME.winfo_children():
                    widgets.destroy()

                show_right_info()
                for i in hddList:
                    HDD_Listbox.insert(len(hddList)+1, f'NAME : {i.getName()}  CAPACITY : {i.getCapacity()}TB')

        else:
            status_label.config(text="Invalid input. Please provide a valid name and RAID level.", fg="red")


    def add_More_ComboBox():
        hdd_label = tk.Label(scroll_frame, text="HDD Name:")
        hdd_label.pack()

        hdd_names = [hdd.getName() for hdd in hddList]
        hdd_combobox = ttk.Combobox(scroll_frame, values=hdd_names)
        hdd_combobox.pack()
        Comboboxes.append(hdd_combobox)

    popup_window = tk.Toplevel(window)
    popup_window.title("Add RAID")
    popup_window.geometry('400x600')

    # Create a Canvas widget with a scrollbar
    canvas = tk.Canvas(popup_window)
    scroll_frame = tk.Frame(canvas)

    scrollbar = tk.Scrollbar(popup_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw", tags="scroll_frame")

    def on_canvas_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", on_canvas_configure)

    # Create an Entry widget for the RAID name
    raid_name_label = tk.Label(scroll_frame, text="RAID Name:")
    raid_name_label.pack(pady=5)

    raid_name_entry = tk.Entry(scroll_frame)
    raid_name_entry.pack(pady=5)

    # Create an Entry widget for the RAID level
    raid_level_label = tk.Label(scroll_frame, text="RAID Level:")
    raid_level_label.pack(pady=5)

    raid_level_entry = tk.Entry(scroll_frame)
    raid_level_entry.pack(pady=5)

    more_hdd_label = tk.Label(scroll_frame, text="+")
    more_hdd_btn = tk.Button(scroll_frame, text="+", command=add_More_ComboBox)
    more_hdd_btn.pack(side=tk.RIGHT)

    # Status Label for success or failure message
    status_label = tk.Label(scroll_frame, text="", fg="black")
    status_label.pack(pady=5)

    # Create a button to confirm the RAID creation
    add_raid_button = tk.Button(scroll_frame, text="Add RAID", command=create_raid)
    add_raid_button.pack(side=tk.BOTTOM, pady=10)


def on_delete_raid_click():
    selected_index = RAID_Listbox.curselection()

    if selected_index:
        # Delete selected item(s) from RAID_Listbox
        for index in selected_index[::-1]:  # Iterate in reverse order to avoid index issues
            RAID_Listbox.delete(index)

        # Optionally, you may want to update RAID_LIST and the right frame here
        # For example, if RAID_LIST is a list of RAID objects, you can delete the corresponding RAID objects:
        for index in selected_index[::-1]:
            del RAID_LIST[index]
        for widgets in RIGTH_FARME.winfo_children():
                    widgets.destroy()
        for widgets in LEFT_MID.winfo_children():
                    widgets.destroy()
        show_right_info()  # Update the right frame if needed

    else:
        tk.messagebox.showwarning("Select RAID", "Please select a RAID to delete.")





window = tk.Tk()
window.maxsize(1024, 800)
window.config(bg='gray')
window.title('RAID SIMULATION')
path = os.getcwd()
print(f'{path}\\..\\image\\addDriver.png')
photo_addDriver = tk.PhotoImage(file=f'{path}\\..\\image\\addDriver.png')
photo_addRAID = tk.PhotoImage(file=f'{path}\\..\\image\\addRAID.png')
photo_addRAID = tk.PhotoImage(file=f'{path}\\..\\image\\addRAID.png')
photo_deleteDriver = tk.PhotoImage(file=f'{path}\\..\\image\\deleteDriver.png')
# photo_setting = tk.PhotoImage(file=f'{path}\\..\\image\\settings.png')
photo_hardDisk = tk.PhotoImage(file=f'{path}\\..\\image\\hard-disk.png')

resized_image_addDriver = photo_addDriver.subsample(RESIZE, RESIZE)
resized_image_addRAID = photo_addRAID.subsample(RESIZE, RESIZE)
resized_image_deleteDriver = photo_deleteDriver.subsample(RESIZE, RESIZE)
# resized_image_setting = photo_setting.subsample(RESIZE, RESIZE)
resized_image_hardDisk = photo_hardDisk.subsample(RESIZE, RESIZE)


TOP_FARME = tk.Frame(window, width=1024, height=80, bg='#1B1A55', highlightbackground='#070F2B', highlightthickness=2)
LEFT_FARME = tk.Frame(window, width=300, height=720, bg='#535C91', highlightbackground='#070F2B', highlightthickness=2)
RIGTH_FARME = tk.Frame(window, width=774, height=720, bg='#9290C3')


LEFT_UPPER = tk.Frame(LEFT_FARME, width=300, height=250, bg='white', highlightbackground='black', highlightthickness=2)
LEFT_MID = tk.Frame(LEFT_FARME, width=300, height=250, bg='white', highlightbackground='black', highlightthickness=2)
LEFT_LOWER = tk.Frame(LEFT_FARME, width=300, height=250, bg='white', highlightbackground='black', highlightthickness=2)


Button_AddDriver = tk.Button(TOP_FARME, image=resized_image_addDriver, bg='#9290C3', command=on_add_driver_click)
Button_AddRAID = tk.Button(TOP_FARME, image=resized_image_addRAID, bg='#9290C3', command= on_add_raid_click)
Button_DeleteDriver = tk.Button(TOP_FARME, image=resized_image_deleteDriver, bg='#9290C3', command=on_delete_raid_click)
# Button_Setting = tk.Button(TOP_FARME, image=resized_image_setting, bg='#9290C3')


Button_AddDriver.grid(row=0, column=0, sticky='nsew', padx=20, pady=10)
Button_AddRAID.grid(row=0, column=1, sticky='nsew', padx=20, pady=10)
Button_DeleteDriver.grid(row=0, column=2, sticky='nsew', padx=20, pady=10)
# Button_Setting.grid(row=0, column=3, sticky='nsew', padx=20, pady=10)


TOP_FARME.grid(row=0, columnspan=3, sticky='nsew')
LEFT_FARME.grid(row=1, column=0, sticky='nsew')
RIGTH_FARME.grid(row=1, column=2, sticky='nsew')

LEFT_UPPER.grid(row=0, columnspan=2, sticky='nsew', pady=10)
LEFT_MID.grid(row=1, columnspan=2, sticky='nsew', pady=10)
LEFT_LOWER.grid(row=2, columnspan=2, sticky='nsew', pady=10)

index = 1
HDD_Listbox = tk.Listbox(LEFT_LOWER , width=50)
HDD_Listbox.grid(rowspan=1, columnspan=3, sticky='nsew')

for i in hddList:
    HDD_Listbox.insert(len(hddList) + 1, f'NAME : {i.getName()}  CAPACITY : {i.getCapacity()}TB')

RAID_Listbox = tk.Listbox(LEFT_UPPER, width=50)
RAID_Listbox.grid(rowspan=1, columnspan=3, sticky='nsew')
index = 1
for raid in RAID_LIST:
    RAID_Listbox.insert(index, raid.getName())
    index += 1

show_right_info()

RAID_Listbox.bind('<ButtonRelease-1>', on_raid_listbox_click)


LEFT_FARME.pack_propagate(False)
RIGTH_FARME.pack_propagate(False)
LEFT_UPPER.pack_propagate(False)
LEFT_LOWER.pack_propagate(False)


window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)

window.geometry('1024x800')
window.mainloop()




