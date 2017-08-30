#!/usr/bin/env python

import os
import shutil
import subprocess
import time

modules = [
	("COMP110", "Principles of Computing"),
	("COMP120", "Creative Computing: Tinkering"),
	("COMP130", "Game Architecture"),
	("COMP140", "Creative Computing: Hacking"),
	("COMP150", "Game Development Practices"),
	("COMP160", "Software Engineering"),
	("COMP210", "Interfaces & Interaction"),
	("COMP220", "Graphics & Simulation"),
	("COMP230", "Game Development I: Pre-Production"),
	("COMP240", "Game Development I: Production"),
	("COMP250", "Artificial Intelligence"),
	("COMP260", "Distributed Systems")
]

sessions_per_module = 12

template_path = os.path.join("template", "template")
compile_commands = []

for module_code, module_name in modules:
	for session in xrange(1, sessions_per_module+1):
		dir_path = os.path.join(module_code, "%02i" % session)
		if os.path.exists(dir_path):
			print dir_path, "already exists -- skipping"
		else:
			print "creating", dir_path
			shutil.copytree(template_path, dir_path)
			
			info_file_path = os.path.join(dir_path, "sessioninfo.tex")
			with open(info_file_path, "wt") as info_file:
				info_file.write(r"\newcommand{\modulecode}{%s}" % module_code)
				info_file.write(r"\newcommand{\moduletitle}{%s}" % module_name.replace('&', r'\&'))
				info_file.write(r"\newcommand{\sessionnumber}{%i}" % session)

			for file_type in ("handout", "screen"):
				old_file_name = "main_%s.tex" % file_type
				new_file_name = "%s_%02i_%s.tex" % (module_code, session, file_type)
				
				old_path = os.path.join(dir_path, old_file_name)
				new_path = os.path.join(dir_path, new_file_name)
				os.rename(old_path, new_path)
				
				compile_commands.append((dir_path, new_file_name))

compile_commands = compile_commands * 4

# http://stackoverflow.com/a/12926181
DEVNULL = open(os.devnull, 'wb')

workers = [
	subprocess.Popen(["echo"], stdout=DEVNULL)
	for i in xrange(12)
]

while any(w is not None for w in workers):
	for i in xrange(len(workers)):
		if workers[i] is not None:
			code = workers[i].poll()
			if code is not None:
				if code != 0:
					raise InvalidOperationError("%r failed", processes[i])
				else:
					if len(compile_commands) > 0:
						(dir_path, file_name) = compile_commands.pop()
						print len(compile_commands), "remaining"
						workers[i] = subprocess.Popen(["pdflatex", file_name], stdout=DEVNULL, cwd=dir_path)
					else:
						workers[i] = None
	time.sleep(0.1)
