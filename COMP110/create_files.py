import os

for i in range(3, 12+1):
	for session in ["lecture", "workshop"]:
		filename_base = os.path.join("%02i" % i, "2019-20-COMP110-%02i-%s-materials" % (i, session))
		
		with open(filename_base + ".tex", "wt") as f:
			f.writelines([
				r"\documentclass[handout, xcolor={dvipsnames}]{beamer}\usepackage{etoolbox}\newtoggle{printable}\togglefalse{printable}",
				r"\input{%s_main_body}" % session,
				""
			])
		
		with open(filename_base + "-screen.tex", "wt") as f:
			f.writelines([
				r"\documentclass[xcolor={dvipsnames}]{beamer}\usepackage{etoolbox}\newtoggle{printable}\togglefalse{printable}",
				r"\input{%s_main_body}" % session,
				""
			])
		
		with open(filename_base + "-screen.tcp", "wt") as f:
			f.write("""[FormatInfo]
Type=TeXnicCenterProjectInformation
Version=4

[ProjectInfo]
MainFile=2019-20-COMP110-%02i-%s-materials-screen.tex
UseBibTeX=0
UseMakeIndex=0
ProjectLanguage=en
ProjectDialect=US
""" % (i, session))
