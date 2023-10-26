'''
import tkinter as tk
from datetime import datetime

begin_time = ""
end_time = ""

def add_message():
    project = project_entry.get()
    task = task_entry.get()
    comment = comment_entry.get()
    
    if custom_begin_time.get():
        global begin_time
        begin_time = custom_begin_time.get()
    if custom_end_time.get():
        global end_time
        end_time = custom_end_time.get()

    if begin_time and end_time:
        try:
            begin_timestamp = datetime.strptime(begin_time, '%H:%M')
            end_timestamp = datetime.strptime(end_time, '%H:%M')
            time_difference = end_timestamp - begin_timestamp
            hours_difference = time_difference.total_seconds() / 3600
            time_diff_str = f"{hours_difference:.2f} hours"
        except ValueError:
            time_diff_str = "Invalid time format"

        timestamp = datetime.now().strftime('%H:%M:%S')
        message = f"[{timestamp}] Project: {project}, Task: {task}, Comment: {comment}, Time difference: {time_diff_str}"

        display_text.config(state=tk.NORMAL)
        display_text.insert(tk.END, message + "\n")
        display_text.config(state=tk.DISABLED)

        # Clear input fields after adding message
        project_entry.delete(0, tk.END)
        task_entry.delete(0 ,tk.END)
        comment_entry.delete(0, tk.END)
        custom_begin_time.set("")
        custom_end_time.set("")


def record_begin_time():
    global begin_time
    begin_time = datetime.now().strftime('%H:%M')
    begin_label.config(text=f"Begin Time: {begin_time}")
    
def record_end_time():
    global end_time
    end_time = datetime.now().strftime('%H:%M')
    end_label.config(text=f"Begin Time: {end_time}")

# Create the main window
root = tk.Tk()
root.title("Time Tracker")

custom_begin_time = tk.StringVar()
custom_end_time = tk.StringVar()

# Create the input fields for project and comment
project_label = tk.Label(root, text="Project:")
project_label.grid(row=0, column=0, padx=5, pady=5)
project_entry = tk.Entry(root, width=50)
project_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

# task_label = tk.Label(root, text="Project:")
# task_label.grid(row=0, column=0, padx=5, pady=5)
# task_entry = tk.Entry(root, width=50)
# task_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

comment_label = tk.Label(root, text="Comment:")
comment_label.grid(row=1, column=0, padx=5, pady=5)
comment_entry = tk.Entry(root, width=50)
comment_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# Create buttons to record begin and end time
begin_time_button = tk.Button(root, text="Record Begin Time", command=record_begin_time)
begin_time_button.grid(row=2, column=0, padx=5, pady=5)

end_time_button = tk.Button(root, text="Record End Time", command=record_end_time)
end_time_button.grid(row=2, column=1, padx=5, pady=5)

# Entry fields for custom start and end times
custom_begin_label = tk.Label(root, text="Custom Begin Time (HH:MM):")
custom_begin_label.grid(row=3, column=0, padx=5, pady=5)
custom_begin_entry = tk.Entry(root, textvariable=custom_begin_time)
custom_begin_entry.grid(row=3, column=1, padx=5, pady=5)

custom_end_label = tk.Label(root, text="Custom End Time (HH:MM):")
custom_end_label.grid(row=4, column=0, padx=5, pady=5)
custom_end_entry = tk.Entry(root, textvariable=custom_end_time)
custom_end_entry.grid(row=4, column=1, padx=5, pady=5)

# Labels to display the recorded times
begin_label = tk.Label(root, text="Begin Time:")
begin_label.grid(row=5, column=0, padx=5, pady=5)

end_label = tk.Label(root, text="End Time:")
end_label.grid(row=5, column=1, padx=5, pady=5)

# Create the button to add messages
add_button = tk.Button(root, text="Add Message", command=add_message)
add_button.grid(row=6, column=0, padx=5, pady=5, columnspan=2)

# Create the text widget to display messages
display_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, height=20, width=80)
display_text.grid(row=7, column=0, padx=5, pady=5, columnspan=4)

root.mainloop()
'''

#%%

import tkinter as tk
from datetime import datetime
import pandas as pd

begin_time = ""
end_time = ""
data = []

def update_display_text():
    display_text.config(state=tk.NORMAL)
    display_text.delete("1.0", tk.END)

    for entry in data:
        date, begin, end, diff, hours, project, task, comment = entry
        display_text.insert(tk.END, f"Date: {date}, Start Time: {begin}, End Time: {end}, Time Difference: {diff}, Hours: {hours}, Project: {project}, Task: {task}, Comment: {comment}\n")

    display_text.config(state=tk.DISABLED)

def add_message():
    project = project_entry.get()
    task = task_entry.get()
    comment = comment_entry.get()

    if custom_begin_time.get():
        global begin_time
        begin_time = custom_begin_time.get()
    if custom_end_time.get():
        global end_time
        end_time = custom_end_time.get()

    if begin_time and end_time:
        try:
            begin_timestamp = datetime.strptime(begin_time, '%H:%M')
            end_timestamp = datetime.strptime(end_time, '%H:%M')
            time_difference = end_timestamp - begin_timestamp
            hours_difference = time_difference.total_seconds() / 3600
            time_diff_str = f"{hours_difference:.2f} hours"
        except ValueError:
            time_diff_str = "Invalid time format"

        timestamp = datetime.now().strftime('%H:%M:%S')
        message = f"[{timestamp}] Project: {project}, Task: {task}, Comment: {comment}, Time difference: {time_diff_str}"

        display_text.config(state=tk.NORMAL)
        display_text.insert(tk.END, message + "\n")
        display_text.config(state=tk.DISABLED)

        # Save the data into the list
        data.append([datetime.now().strftime('%Y-%m-%d'), begin_time, end_time, time_diff_str, hours_difference, project, task, comment])

        # Clear input fields after adding message
        project_entry.delete(0, tk.END)
        task_entry.delete(0, tk.END)
        comment_entry.delete(0, tk.END)
        custom_begin_time.set("")
        custom_end_time.set("")

def record_begin_time():
    global begin_time
    begin_time = datetime.now().strftime('%H:%M')
    begin_label.config(text=f"Begin Time: {begin_time}")

def record_end_time():
    global end_time
    end_time = datetime.now().strftime('%H:%M')
    end_label.config(text=f"End Time: {end_time}")

def save_to_excel():
    if data:
        df = pd.DataFrame(data, columns=["Date", "Start Time", "End Time", "Time Difference", "Hours", "Project", "Task", "Comment"])
        df.to_excel("time_tracker_data.xlsx", index=False, engine='openpyxl')
        print("Data saved to 'time_tracker_data.xlsx'")

# Create the main window
root = tk.Tk()
root.title("Time Tracker")

custom_begin_time = tk.StringVar()
custom_end_time = tk.StringVar()

# Rest of the code remains the same

# Create the input fields for project and comment
project_label = tk.Label(root, text="Project:")
project_label.grid(row=0, column=0, padx=5, pady=5)
project_entry = tk.Entry(root, width=50)
project_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

task_label = tk.Label(root, text="Task:")
task_label.grid(row=1, column=0, padx=5, pady=5)
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

comment_label = tk.Label(root, text="Comment:")
comment_label.grid(row=2, column=0, padx=5, pady=5)
comment_entry = tk.Entry(root, width=50)
comment_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

# Rest of the code remains the same
