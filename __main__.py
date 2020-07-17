import glob
import os

script_files=glob.glob('*.py')
print(script_files)
#script_files.remove(os.sys.argv[0])

for file in script_files:
    os.system('python %s'%file)
        
    
    
