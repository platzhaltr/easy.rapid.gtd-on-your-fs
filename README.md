
Welcome to the gtd-on-fs aka 'brainflush'
=========================================

In this small project we want to introduce a strategy to *keep track of your ToDo’s without* the need of having *a third party application* to manage them. The approach *just uses files*, which are *stored on your filesystem* to manage things you need to get done and thoughts that you don’t want to lose. *WE DON’T use text-files* to stores things IN them. The underlying idea is the GTD approach of David Allen.

It tries to accomplish the idea of *being as simple as possible*, *as quick as possible*, and *as productive as possible* in your workflow. You don’t have to get used to handle a new application. *You are familiar with a file-browser* and the creation of files, so why not *use this ability* to manage our tasks?

Meanwhile, there are a lot of GTD applications out there and some of them are really good and intuitive in managing ToDo lists, but this idea is different and some kind of wired in the first place. Please feel free to comment and to contact us about what you think about it.

For beeing really as productive as possible please jump into section *3. Scripts*.

You'll find here:

1. **Basic Idea**

1.1 Workflow

1.2 Your File-Browser

2. **Improvements**

2.1 Context

2.2 Folder Structure

3. **Scripts**

3.1 Requirements and Installation

3.2 Usage

1. Basic Idea
---------------

Easy. The *basic idea is to create a folder* in your filesystem (e.g. /home/user/Inbox) in which you want to store your ToDo’s, thoughts, etc. We’ll call this folder *the INBOX-folder* as it is the *repository of all the things* your want to keep track of.

### 1.1 Workflow

Certainly, as you are browsing the web, programming, or doing something else at your computer, *there are thoughts and ideas that suddenly come* right into your brain without annoucement. So, as *you don’t want to waste much time* but *quickly come back to your current task*, the best thing to do would be to *store your idea* somewhere in a list and to *catch it up later*. But instead of navigating to the applications menu of your operating system, starting your GTD application, hitting the “New Task” button and filling out all the requirement fields, you *open your file-browser* (unless it isn’t open anyway) and hit the shortcut for the creation of a new text-file (or *use the script enclosed with this project*). You give the *file a name* which is short version of *your idea* or thing that you want to do later, e.g. “E-Mail to george”, and bam, you’re finished.

### 1.2 Your File-Browser

In this approach, the GTD application that manages your ToDo's is *your file-browser*. The file-browser is probably the application in your operating system that *you are the most familiar* with. You further can *create subfolders in your INBOX-folder*, e.g. to *represent contexts (“@home”)* and other things like projects (“Projects”), tasks that you want to do as soon as possible (“DoASAP”), or even things that you’ve already finished (“Done”). You only have to *navigate to the right folder* and you’ll see the things you have to get done. You don't have to open another application. Further, you even can *use the search function* etc. to find a file/ToDo or *sort by creation date*, which certainly are *integral parts of your file-browser*.

One more good thing is that *you don’t have to care about filetypes*, e.g. EXCEL-sheets, images, etc., can be stored in your INBOX-folder. You can access, look at, edit or delete them quickly. Furthermore, with your “GTD application”, i.e. file-browser, you *don’t have to worry about compatibility*. It is OS-indepentent. You can *synchronize your files* with an other hard drive and use *another operating system*, file-browser, *or even a terminal*, you want.

For simple text files we suggest to use the .ibx extension. For instance, a task called 'Do laundry' would be saved in '~/INBOX/Do laundry.ibx'.

2. Improvements
---------------

### 2.1 Contexts

While specifying your task, you already might know the context in which it needs to get done. We suggest to create special folders in your INBOX-repository to specify contexts. This can be done, for instance, by prefixing the folder with an @-symbol. For instance, tasks that you need to get done at home might be stored in '~/INBOX/@home'.

### 2.2 Folder Structure

If it needs to get more specific you can use a more sophisticated folder structure. For instance, if you want to put a task for washing your dishes you might use the following folder structure '~/INBOX/@home/@kitchen/wash the dishes.ibx'.

{3. Scripts}
------------

For being as productive as possible and getting the thought as quickly as possible out of you brain, we suggest using a small script, which basically pops up a window with a textfield, if you want to save a thought, and stores the file/ToDo automatically in the right context, i.e. folder on your filesystem. Connecting the executing of the script with a global shortcut makes you being very quick!

### 3.1 Requirements and Installation

To use the script you will need at least python 2.7 and the pyGtk module. There might be incompatibility problems with python 3.x, but we haven't checked. The script was tested on Fedora Linux 14 (Laughlin).

Just checkout the project somewhere in your home-directory. You will find the script in the folder called 'scripts'. You will see a single python script 'brainflush.py'. 

* cd ~/somewhere in your home-directory/
* git clone git@github.com:/platzhaltr/gtd-on-fs
* cd gtd-on-fs/
* adjust the properties-file in scripts/app.properties
* chmod 744 scripts/brainflush.py
* execute the script by typing './brainflush.py'
* put a global shortcut for that, e.g. ALT+N

