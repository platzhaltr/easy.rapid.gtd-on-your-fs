Welcome to the gtd-on-fs!
=========================

A straighforward approach to a GTD strategy on your filesystem. You don't need an application to manage your todo's and thoughts, just your filebrowser.

In this small project we want to introduce a strategy to keep track of your ToDo’s without the need of having a third party application to manage them. The approach just uses files, which are stored in your filesystem to manage things you need to get done and thoughts that you don’t want to lose. We DON’T use text-files to stores things IN them actually. The underlying idea is the GTD approach of David Allen.

Meanwhile, there are a lot of GTD applications out there and some of them are really good and intuitive in managing ToDo lists, but this idea is different and some kind of wired in the first place. Please feel free to comment and to contact us about what you think about it.

It tries to accomplish the idea of being as simple as possible, as quick as possible, and as productive as possible in your workflow. You don’t have to get used to handle a new application. Everyone is familiar with a file-browser and the creation of files, so why not use this ability to manage our tasks?

The Workflow Scenario
---------------------

The basic idea is to create a folder in your filesystem (e.g. /home/user/Inbox) in which you want to store your ToDo’s, thoughts, etc. We’ll call this folder the INBOX-folder as it is the repository of all the things your want to keep track of. Certainly, as you are browsing the web, programming, or doing something else at your computer, there are thoughts and ideas that suddenly come right into your brain without annoucement. So, as you don’t want to waste much time but quickly come back to your current task, the best thing to do would be to store your idea somewhere in a list and to catch it up later. But instead of navigating to the applications menu of your operating system, starting your GTD application, hitting the “New Task” button and filling out all the requirement fields, you open your file-browser (unless it isn’t open anyway) and hit the shortcut for the creation of a new text-file. You give the file the name of a short version of your idea or thing that you want to do later, e.g. “E-Mail to george”, and bam, you’re finished.

Your File-Browser
-----------------

In our approach, the GTD application that manages your ToDo list is your file-browser actually. The file-browser is probably the application in your operating system that you are the most familiar with. You further can create subfolders in your INBOX-folder, e.g. to represent contexts (“@home”) and other things like projects (“Projects”), tasks that you want to do as soon as possible (“DoASAP”), or even things that you’ve already finished (“Done”). You only have to navigate to the right folder and you’ll see the things you have to get done. Further, you can make use of such functions like searching for a file or sorting by creation date, which certainly are integral parts of your file-browser.

One more good thing is that you don’t have to care about filetypes, e.g. EXCEL-sheets, images, etc., can be stored in your INBOX-folder. You can access, look at, edit or delete them quickly. Furthermore, with your “GTD application”, i.e. file-browser, you don’t have to worry about compatibility. It is OS-indepentent. You can synchronize (you don’t even have to) your files with an other hard drive and use the operating system, file-browser, or even terminal, you want.

Improvements - Shell Scripts
----------------------------

For faster creation of files we created a small shell script which will help you to create ToDos more easily. Basically it will pop up a small dialog window in which you can type in your task. We used GNOME’s ‘zentiy’ to implement this. By closing the window the task will be stored in the INBOX-folder you’ve specified in the script. We recommend to make a global shortcut to that script in your desktop manager (like GNOME, KDE, etc) which invokes this script, e.g. Alt+Shift+n. Everytime you want to create a new task you just hit the shortcut, the dialog window will come up and you can type in your idea.

Automatic Context Assignment
----------------------------

While specifying the task you already might know the context in which it needs to get done. You can write it down with an annotation, e.g. “E-Mail to george @computer”. The task will then be created in the right context folder, provided that the context folder does exist in this manner. Pleace note that if the context-folder does not exist the task will not be created.
