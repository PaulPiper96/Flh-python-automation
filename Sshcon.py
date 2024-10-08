import getpass
from fabric import Connection, Config
import sys
from errors import InvalidPostmaxException, InvalidUploadLimit, InvalidMemoryLimitException

def checkformemorylimit(memorylimitstring):
    print(memorylimitstring)
    if memorylimitstring =="memory_limit =512M":
          print("Memory Limit Okay")
          return True
    else:
         return False 



def checkforuploadmax(uploadmaxstring):
    print(uploadmaxstring)
    if uploadmaxstring =="upload_max_filesize = 300M":

          
          return True
    else:
         print(uploadmaxstring =="upload_max_filesize = 300M")
         print("cause:" ,uploadmaxstring, "amd upload_max_filesize = 300M")
         return False

def checkforpostmax(uploadmaxstring):
    if uploadmaxstring =="post_max_size = 300M":
          print("post_max_size is Okay")
          return True
    else:
         return False


def connect_and_run_ls(REMOTE_HOST,project_number,password ):
    try:
        c = Connection(host=REMOTE_HOST, user=project_number, port=22,connect_kwargs={'password': password})
        remotefile_path = '/etc/php/php.ini'
        result = c.run(f'grep "memory_limit" { remotefile_path}', hide=True)

        postmax=""
        memorylimit=""
        uploadmax=""

        postmax = c.run(f'grep "post_max_size" { remotefile_path}', hide=True)
        memorylimit = c.run(f'grep "memory_limit" { remotefile_path}', hide=True)
        uploadmax= c.run(f'grep "upload_max_filesize" { remotefile_path}', hide=True)


            
        if postmax.stdout:
            print(postmax.stdout.strip())
            if not checkforpostmax(postmax.stdout.strip()):  # Simplified condition
                print("We have to check for postmax")
                c.run(f"sed -i 's/post_max_size *= *[0-9]\\+M/post_max_size = 300M/' {remotefile_path}")  # Allow for flexible spaces
            else:
                print("post_max_size seems alright")
        else:
            raise InvalidPostmaxException("post_max_size not found in php.ini")

        if memorylimit.stdout:
            print(memorylimit.stdout.strip())
            if not checkformemorylimit(memorylimit.stdout.strip()):  # Simplified condition
                print("We have to check for memory_limit")
                c.run(f"sed -i 's/memory_limit *= *[0-9]\\+M/memory_limit = 512M/' {remotefile_path}")  # Allow for flexible spaces
            else:
                print("memory_limit seems alright")
        else:
            raise InvalidMemoryLimitException("memory_limit not found in php.ini")

        if uploadmax.stdout:
            print(uploadmax.stdout.strip())
            if not checkforuploadmax(uploadmax.stdout.strip()):  # Simplified condition
                print("We have to check for upload_max_filesize")
                c.run(f"sed -i 's/upload_max_filesize *= *[0-9]\\+M/upload_max_filesize = 300M/' {remotefile_path}")  # Allow for flexible spaces
            else:
                print("upload_max_filesize seems alright")
        else:
            raise InvalidUploadLimit("upload_max_filesize not found in php.ini")

   


    except Exception as e:
        
            print(f"Failed to connect or execute command: {e}")


if __name__ == "__main__":

    project_number = input("Enter ProjectNumber: ")
    print ("you entered " + project_number) 

    password =input("Enter Passwrord: ")
    print(password)


    REMOTE_HOST = project_number+'.mittwaldserver.info'
    REMOTE_USER = project_number # Replace with your actual SSH username
    REMOTE_PORT = 22  # Default SSH port is 22

    print(REMOTE_HOST)
    connect_and_run_ls(REMOTE_HOST, project_number, password)