import os
import io
import argparse
import datetime

def create_new_completenote(filename):
    filename=str(filename)
    
    newfile=open(filename,'x')
    print('sucessful')


def add_to_existingnote(existingfile,text,duedate,time):
    duedate=str(duedate)
    time=str(time)
    complete=str('Not completed')
    if  isinstance(existingfile,str):
        with open(existingfile,'a')as file:
            file.write(f"{text} | {duedate} | {time} |{complete}\n")
            file.close()
            print('sucessfully added 1')
    
    else:
    
        existingfile.write(f"{text} | {duedate} | {time} \n")
        existingfile.close()
        print('sucessfully added 2')


def update_note_text(existingfile, updatetext, newtext, date='none', time='none'):
    updated_lines = []
    
    with open(existingfile, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            if updatetext in line:
                parts = line.strip().split('|')
                if len(parts) >= 3:
                    existing_date = parts[1].strip()
                    existing_time = parts[2].strip()
                    existing_complete=parts[3].strip()
                    
                    if date != 'none':
                        existing_date = str(date)
                    
                    if time != 'none':
                        existing_time = str(time)
                    
                    updated_line = f"{newtext} | {existing_date} | {existing_time}|{existing_complete}\n"
                    updated_lines.append(updated_line)
            else:
                updated_lines.append(line)

    # Write the updated content back to the file
    with open(existingfile, 'w') as file:
        file.writelines(updated_lines)
    
    print(f'successfully updated {updatetext} to {newtext}')
    
def delete_complete_note(notename):
    notename=str(notename)
    os.remove(notename)
    print(f"succsfully deleted {notename}")
    
def delete_note_content(existingfile,deletetext):
    with open(existingfile, 'r') as file:
        lines = file.readlines()
        updated_lines= [line for line in lines if deletetext not in line]

    # Write the updated content back to the file
    with open(existingfile, 'w') as file:
        file.writelines(updated_lines)
    
        print(f'sucessfully deleted {deletetext}')

def listall(textfile):
    with open(textfile,'r') as file:
        lines=file.readlines()
        print(lines)

def mark_complete(filename,taskname):
    completedtask=[]
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if taskname in line:
                parts = line.strip().split('|')
                if len(parts) >= 3:
                    complete=parts[3].strip()
                    if complete=='Not completed':
                        complete='Completed'
                        date=datetime.date.today()
                        existing_date = f"Task completed on {date} "
                        current_time = datetime.datetime.now().time()
                        existing_time = f"Task completed on {current_time} "
                        tasknm=parts[0].strip()
                        completed_line = f"{tasknm} | {existing_date} | {existing_time}|{complete}\n"
                        completedtask.append(completed_line)
            else:
                completedtask.append(line)

    # Write the updated content back to the file
    with open(filename, 'w') as file:
        file.writelines(completedtask)
        file.close()
    
    print(f'sucessfully marked task {taskname} as  completed')
                        
                        
                        
        
parser = argparse.ArgumentParser(description="Jafr - Just a friendly reminder")
parser.add_argument("command", choices=["create", "modifynote_content","addtonote", "delete_completenote","delete_notecontent", "list","markcomplete"], help="Command to perform")
parser.add_argument("--filename", help="Name of the file for the 'create' command")
parser.add_argument("--task", help="Task description")
parser.add_argument("--index", type=int, help="Index of the task to update/delete")
parser.add_argument("--updatetext", help="Text to be updated in the note")
parser.add_argument("--newtext", help="New text to replace the updated text")
parser.add_argument("--date", help="Due date (YYYY-MM-DD) for note modification")
parser.add_argument("--time", help="Due time in 24-hour format (HH:MM) for note modification")
parser.add_argument("--delete_notecontent", help="Text to be deleted in the note")
parser.add_argument("--complete_taskname", help="Task to be marked complete")


args = parser.parse_args()
if args.command == "create":
    if args.filename is None:
        print("Please provide a filename using the --filename option for the 'create' command.")
    else:
        filename=str(args.filename)
        extention='.txt'
        if extention not in filename:
            filename += extention

        task = str(args.task)
        due_date = input("Due date (YYYY-MM-DD): ")
        due_time = input("Due time in 24 hour format (0000): ")

        create_new_completenote(filename)
        add_to_existingnote(filename,task,due_date,due_time)
elif args.command=="addtonote":
    if args.filename is None:
        print("Please provide a filename using the --filename option for the 'create' command.")
    else:
        filename=str(args.filename)
        extention='.txt'
        if extention not in filename:
            filename += extention

        task = str(args.task)
        due_date = input("Due date (YYYY-MM-DD): ")
        due_time = input("Due time in 24 hour format (0000): ")
        add_to_existingnote(filename,task,due_date,due_time)
        
        
        
        
elif args.command == "modifynote_content":
    if args.filename is None:
        print("Please provide a filename using the --filename option for the 'create' command.")
    else:
        filename=str(args.filename)
        extention='.txt'
        if extention not in filename:
            filename += extention

        updatetext = str(args.updatetext)
        newtext = str(args.newtext)
        date = args.date if args.date else 'none'
        time = args.time if args.time else 'none'

        update_note_text(filename, updatetext, newtext, date, time)
        
    
elif args.command == "delete_completenote":
    if args.filename is None:
        print("Please provide a filename using the --filename option for the 'create' command.")
    else:
        filename=str(args.filename)
        extention='.txt'
        if extention not in filename:
            filename += extention
    delete_complete_note(filename)
        
elif args.command == "delete_notecontent":
    if args.filename is None:
        print("Please provide a filename using the --filename option for the 'create' command.")
    else:
        filename=str(args.filename)
        extention='.txt'
        if extention not in filename:
            filename += extention
        deletecontext=args.delete_notecontent
        delete_note_content(filename,deletecontext)
        
    # Call your function to
elif args.command == "list":
    if args.filename is None:
        print("Please provide a filename using the --filename option for the 'create' command.")
    else:
        filename=str(args.filename)
        extention='.txt'
        if extention not in filename:
            filename += extention
    listall(filename)
elif args.command == "markcomplete":
    if args.filename is None:
        print("Please provide a filename using the --filename option for the 'create' command.")
    else:
        filename=str(args.filename)
        extention='.txt'
        if extention not in filename:
            filename += extention
        taskname=str(args.complete_taskname)
    
    mark_complete(filename,taskname)
    
else:
    print("Invalid command")
