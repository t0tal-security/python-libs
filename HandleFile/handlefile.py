import os
import subprocess


'''
Basically a wrapper for most useful functions


set_file(file_name) - sets file name to operate on

get_metadata - in progress

copy_to(dest_path) - copies and checks whether was copied successfully ( based on sha256 ). also returns source and destination paths. additionally performs few logical checks
get_absolute - returns absolute path of current name set
get_sha256 - gets sha256 sum of current name set
exists - checks if the name exists
is_file - checks if name is file
is_dir - checks if name is dir
'''


class HandleFile:
    def __init__(self, m_file_name: str=""): # assigns self.file_name with given value or "None" if empty
        if m_file_name == "":
            self.file_name = "None"
        else:
            self.file_name = str(m_file_name)


    def __str__(self): # -> returns self.file_name
        return self.file_name

    
    def set_file(self, m_file_name: str="") -> None: # -> set self.file_name to given value or "None" if empty
        if m_file_name == "":
            self.file_name = "None"
        else:
            self.file_name = str(m_file_name)



    def get_metadata(self) -> list: # TO DO: -> return list with file's metadata
        return []



    def copy_to(self, m_destination: str="") -> list: # -> copy self.file_name to destination
        if self.is_dir():
            print("can not copy directories")
            return []
        
        if not self.exists():
            print("source file to copy doesn't exist")
            return []

        
        dest = HandleFile(m_destination) # dir, but I know. Had to use it for the sake of below if's
        
        if dest.file_name == "None":
            print("dir path can not be empty")
            return []
        
        if not dest.exists():
            print("dir path doesn't exist")
            return []
        
        if not dest.is_dir():
            print("dir path must be leading to a directory")
            return []
            

        src = self.get_absolute()
        dst = f'{dest.get_absolute()}/{self.file_name}'

        subprocess.check_output(["cp", src, dst])
        
        checksum = HandleFile(dst)
        copied_sha256 = checksum.get_sha256()
        
        if self.get_sha256() != copied_sha256:
            print("copying failed")
            return []
        
        return [src, dst]


    def get_absolute(self) -> str: # return absolute path of self.file_name
        if os.path.isabs(self.file_name):
            return self.file_name
        else:
            return str(os.path.abspath(self.file_name))


    def get_sha256(self) -> str: # -> get sha256 sum of self.file_name
        if not self.exists():
            return "n/a"
 
        if not self.is_file():
            return "n/a"
            
        result = str(subprocess.check_output(["sha256sum", self.get_absolute()]))
        checksum = result.split("'")[1].split(" ")[0] # raw sha256
            
        return checksum
                

    def exists(self) -> bool: # true if file exists, false if doesn't
        return os.path.exists(self.get_absolute())


    def is_file(self) -> bool: # true if is file, false if doesn't
        return os.path.isfile(self.get_absolute())

    
    def is_dir(self) -> bool: # true if is dir, false if doesn't
        return os.path.isdir(self.get_absolute())

