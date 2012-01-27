#!/usr/bin/env python

# This small python script contains the code which displays a window with a textbox,
# where the task description is typed in. The user might add tags like @home or @computer
# to define the context (i.e. folder) in which the task (i.e. file) is saved to.

# version 0.1
# author mazlo (github account name)
# date 27.01.2012

import pygtk
import gtk
pygtk.require('2.0')

import re
import os
import ConfigParser

class BrainFlushWindow:

	tagExpr = re.compile( "@[\w,\s]+" )	# matches the tags, might be more than one
	textExpr = re.compile( "^[\w,\s]+[@|#]?" )	# matches the task description

	# closes the window
	def destroy(self, widget, data=None):
		gtk.main_quit()

	# handles the key-event "Enter"
	def enter_callback(self, widget, textfield):

		# check and prepare directory path first       
		try:
			path = self.properties.get("Repository","path")
		except ConfigParser.NoOptionError:
			self.on_error(widget, "Error loading path from app.properties.")
			return

		if path.endswith("/"):
			path = path.rstrip("/ ")

		# the text the user typed in
		text = textfield.get_text()

		# initialization
		tags = ""
		taskDescription = text

		# apply regular expressions to find the annotations        
		if "@" or "#" in text:
			tags = BrainFlushWindow.tagExpr.findall( text )
			taskDescription = BrainFlushWindow.textExpr.findall( text )[0]
			taskDescription = taskDescription.rstrip( "@ #") # removes all trailing characters like the specified ones including white space

		tagDirectory = path	# root directory

		# creates the folder structure
		for tag in tags:
			tag = tag.rstrip()	# removes the trailing white spaces
			tagDirectory = tagDirectory +"/"+ tag	# path to repository plus the tag directory name
			
			# create the tag directory
			if not os.path.exists(tagDirectory):
				os.makedirs(tagDirectory)
		  
		# create the file finally
		FILE = open(tagDirectory +"/"+ taskDescription +".ibx","w")
		FILE.close()

	def __init__(self):
		# the property file
		self.properties = ConfigParser.ConfigParser()
		self.properties.read("app.properties")

		# create the window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy", self.destroy)

		# window properties
		self.window.set_border_width(10)
		self.window.set_size_request(450,50)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_title("Type in your task description")

		# the textfield
		textfield = gtk.Entry(0)
		textfield.connect("activate", self.enter_callback, textfield)
		textfield.connect("activate", self.destroy)
		textfield.connect("key-press-event", self.keypressed)

		self.window.add(textfield)

		# display
		textfield.show()
		self.window.show()

	# handles key pressed events
	def keypressed(self, widget, event):
		if event.keyval == gtk.keysyms.Escape:
			gtk.main_quit()

	# handles errors
	def on_error(self, widget, message):
		md = gtk.MessageDialog(self.window, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_WARNING, gtk.BUTTONS_CLOSE, message)
		md.run()
		md.destroy()

	# main method
	def main(self):
		gtk.main()

if __name__ == "__main__":
	mybrain = BrainFlushWindow()
	mybrain.main()
