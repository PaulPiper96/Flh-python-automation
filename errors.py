# Defining custom error to be thrown once the SSH connection is established.
# This will get thrown if the grep command fails to find specific parameters inside the php.ini file.
class InvalidMemoryLimitException(Exception):
    def __init__(self, memparam, message="Trying to assess the memory limit failed after connecting via SSH"):
        self.memparam = memparam
        self.message = message
        super().__init__(self.message)
class InvalidPostmaxException(Exception):
    def __init__(self, memparam, message="Trying to assess the postmax failed after connecting via SSH"):
        self.memparam = memparam
        self.message = message
        super().__init__(self.message)

class InvalidUploadLimit(Exception):
    def __init__(self, memparam, message="Trying to assess the InvalidUploadLimit failed after connecting via SSH"):
        self.memparam = memparam
        self.message = message
        super().__init__(self.message)    

# Function to check if the string is empty and raise the exception if it is
def check_string(input_string):
    if not input_string:  # Change the condition to check if the string is empty
        raise InvalidMemoryLimitException("Provided string is empty")
    return f"String is valid: '{input_string}'"


