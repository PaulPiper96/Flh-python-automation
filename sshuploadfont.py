
import subprocess,os
from fabric import Connection, Config
from pathlib import Path

def getallfilesindir(directory):
      # Expand and set the directory path
    textdirectory = Path(directory).expanduser()

    # Find all `.txt` files in the directory
    txt_files = list(textdirectory.glob("*"))
    
    # Initialize an empty list to store file paths
    arrayoffiles = []

    # Print and store paths of found files
    for file in txt_files:
        print(file)  # Print each file path
        arrayoffiles.append(str(file))  # Append file path as a string

    # Return the list of file paths
    return arrayoffiles


    
def openfontloc():
  subprocess.Popen(f'explorer {os.path.realpath(os.path.normpath(os.path.expanduser("~/Desktop"))+"/fontloc")}')


def createfontloc():
        parentpath=os.path.normpath(os.path.expanduser("~/Desktop"))
        os.mkdir(os.path.join(parentpath+"/fontloc"))
        subprocess.Popen(f'explorer {os.path.realpath(os.path.normpath(os.path.expanduser("~/Desktop"))+"/fontloc")}')
    
def sshconnect(REMOTE_HOST,project_number,password,files ):
    try:
        c = Connection(host=REMOTE_HOST, user=project_number, port=22,connect_kwargs={'password': password})
        fontpath ="/html/wordpress/wp-content/themes/divi-child/fonts"

        for file in files:
            c.put(file, fontpath)


        
    except Exception as e:
        
            print(f"Failed to connect or execute command: {e}")
    finally:
     if 'c' in locals():
            c.close()
            print("SSH connection closed.")

if __name__ == "__main__":
    fontloc_path = os.path.expanduser("~/Desktop/fontloc")

    # Check if the directory exists
    if os.path.exists(fontloc_path):
        openfontloc()  # Call this function if the directory exists
        print("fontloc created")
    else:
        createfontloc()  # Call this function if the directory does not exist
        print("fontloc open")


    project_number = input("Enter ProjectNumber: ")
    print ("you entered " + project_number) 

    password =input("Enter Passwrord: ")
    print(password)


    REMOTE_HOST = project_number+'.mittwaldserver.info'
    REMOTE_USER = project_number # Replace with your actual SSH username
    REMOTE_PORT = 22  # Default SSH port is 22

    print(REMOTE_HOST)
    input("press enter to continue")
    files=getallfilesindir(fontloc_path)
    if not files:
         print("no files provided")
    else: 
        sshconnect(REMOTE_HOST, project_number, password, files)
        