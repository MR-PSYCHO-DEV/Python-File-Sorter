import os 
from pathlib import Path

class FolderFiles():
    def Folder(dir):
        dir = FolderFiles.IsFolder(dir)
        
        path_file = []
        for current_path, _, files in os.walk(dir, topdown=False):
            path_file += [(Path(current_path), file) for file in files]  
        
        return path_file

    #cheeking for subfolders and adding them to the list 
    def FindSubfolders(dir):
        subfolders = [ Path(f.path) for f in os.scandir(dir) if f.is_dir() ]
        for dir in list(subfolders):
            subfolders.extend(FolderFiles.FindSubfolders(dir))
        return subfolders

    #cheeking if the dir exist 
    def IsFolder(dir):
        dir = Path(dir)
        if not os.path.isdir(dir):
            raise FileNotFoundError(f"Directory {str(dir)} does not exist")
        return dir