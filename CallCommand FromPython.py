import subprocess
cmdresult = "move 123.txt 456.txt"
subprocess.call(cmdresult.split(), shell=True)
cmd = 'move 456.txt 457.txt'
returncode = subprocess.Popen(cmd, shell=True)


#import os
#dirname, basename = os.path.split(target)
#save_dir=os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/Archive"
#if not os.path.exists(save_dir): 
#    os.makedirs(save_dir)
#[pri(d) for d in targets]

