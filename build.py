import pygit2
repo = pygit2.Repository('.')
repo.lookup_reference("HEAD").resolve()
head = repo.head
head_name = head.shorthand

from pathlib2 import Path
import os
import subprocess

directory_list = [ d for d in Path('.').iterdir() if d.is_dir() ]
#print(directory_list)
for d in directory_list:
    sub_directory_list = [ s for s in Path(str(d)).glob("[0-9]*") if d.is_dir() ]
    #print(sub_directory_list)
    for s in sub_directory_list:
        working_directory = str(s)
        week_no = working_directory.split('/')[-1]
        module_name=working_directory.split('/')[0]
        file_name_prefix=module_name+"_"+week_no
        old_files = [ f for f in Path(working_directory).glob("*.pdf") if f.is_file() ]
        for f in old_files:
            print(f)
            os.remove(str(f))
        
        screen_file_name=file_name_prefix+'_screen'
        handout_file_name=file_name_prefix+'_handout'

        subprocess.Popen('pdflatex '+screen_file_name+'.tex', cwd=working_directory).wait() 

        #print(file_name_prefix)



"""         old_files = [ f for f in Path(working_directory).glob("*.pdf") if f.is_file() ]
        for f in old_files:
            os.remove(str(f))

        for i in range(2):
            subprocess.Popen('pdflatex build.tex -jobname=' + str(head_name) + '-' + str(d) + '-assignment-' +
                             assignment_number + '-' + 'brief', cwd = working_directory).wait()

        old_files = []
        for e in ['*.aux','*.out','*.nav','*.log','*.snm','*.toc']:
            temp = [ f for f in Path(working_directory).glob(e) if f.is_file() ]
            old_files.extend(temp)
        for f in old_files:
            os.remove(str(f)) """