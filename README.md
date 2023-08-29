# Command-line-taskmanager
 command-line task manager designed to help users efficiently manage their tasks and reminders using a simple and intuitive interface. The tool enables users to create, modify, delete, and list tasks, while also marking them as completed. 

## Features:

* Task Creation: Users can create new tasks with a description, due date, and optional due time. Tasks are saved in a text file for easy retrieval.
* Task Modification: Existing tasks can be modified, including updating the task description, due date, and due time.
* Task Deletion: Users can delete individual tasks or clear the entire list of tasks from the text file.
* Mark as Completed: Tasks can be marked as completed, and the tool records the date and time of completion.
* List Tasks: Users can view the list of tasks stored in the text file, displaying task details such as description, due date, and completion status.

Usage Instructions:

Creating a Task: To create a new task, use the "create" command along with the --filename, --task, --date, and --time options (optional).
```bash
python task_manager.py create --filename tasks.txt --task "Complete project" --date 2023-09-01 --time 1500
```
Modifying a Task: To modify an existing task, use the "modifynote_content" command along with the --filename, --updatetext, and --newtext options.
```bash
python task_manager.py modifynote_content --filename tasks.txt --updatetext "Complete project" --newtext "Review project documentation"
```
Deleting a Task: To delete a specific task, use the "delete_notecontent" command along with the --filename and --delete_notecontent options.
```bash
python task_manager.py delete_notecontent --filename tasks.txt --delete_notecontent "Review project documentation"
```
Marking a Task as Completed: To mark a task as completed, use the "markcomplete" command along with the --filename and --complete_taskname options.
```bash
python task_manager.py markcomplete --filename tasks.txt --complete_taskname "Complete project"
```
Listing Tasks: To view the list of tasks, use the "list" command along with the --filename option.
```bash
python task_manager.py list --filename tasks.txt
```
Deleting All Tasks: To delete all tasks stored in the text file, use the "delete_completenote" command along with the --filename option.
```bash
python task_manager.py delete_completenote --filename tasks.txt
```
