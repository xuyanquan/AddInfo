import sublime, sublime_plugin

from datetime import *
import time

class AddInfoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("insert_snippet",
			{
				"contents": "/**""\n"
				" * @Author:	  Henry""\n"
				" * @DateTime:	"  "%s"  %datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
				" * @Description: Description""\n"
				" */"
			}
		)