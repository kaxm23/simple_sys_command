import subprocess

#for linux we add ,shell=true / windows u don't have to use it 

while True:
 try:
    
   command =input("command > ")
   if command.lower()=="stop":
    break
   subprocess.run([command], shell=True)
 except Exception:
    continue 
print("good bye!")
