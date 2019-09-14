import pygit2
repo = pygit2.Repository('.')
repo.lookup_reference("HEAD").resolve()
head = repo.head
head_name = str(head.shorthand)

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
        
        module_name = str(working_directory.split('\\')[0])
        #print(module_name)
        
        week_no = str(working_directory.split('\\')[1])
        if len(week_no) != 2:
            if len(week_no) < 2:
                week_no = '0' + week_no
                
        #print(week_no)
        
        file_name_prefix = head_name + "-" + module_name + "-" + week_no + "-"
        #print(file_name_prefix)
		
        """
        old_files = [ f for f in Path(working_directory).glob("*.pdf") if f.is_file() ]
        for f in old_files:
            os.remove(str(f))
        
        screen_file_name=file_name_prefix+'_screen'
        handout_file_name=file_name_prefix+'_handout'
        """
        
        files_to_compile = [ f for f in Path(working_directory).glob("*_screen.tex") if f.is_file() ]
        
        for file in files_to_compile:
        
            new_name = file.parts[2]
            new_name = new_name.split('_')            
            new_name = ''.join(new_name[0:len(new_name)-1])
            #print(file_name_prefix + str(new_name) + '-materials')
 
            for i in range(2):
                subprocess.Popen('pdflatex ' + str(file.parts[2]) +' -jobname=' + file_name_prefix + str(new_name) + '-materials', cwd = working_directory).wait()
      
            old_files = []
            for e in ['*.aux','*.out','*.nav','*.log','*.snm','*.toc']:
                temp = [ f for f in Path(working_directory).glob(e) if f.is_file() ]
                old_files.extend(temp)
            for f in old_files:
                os.remove(str(f))

        