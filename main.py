import os, shutil, time
from tqdm import tqdm
from pathlib import Path
from folderFiles import FolderFiles as FF

class Sorter(): 
    def __init__(self, folder="./", dict_name_ext=None, name_other="Other", dont_move=['main.py', 'folderFiles.py']):
        
        self.name_other = name_other
        os.chdir(folder) #change cwd 
        path_files = FF.Folder(os.getcwd())
        
        
        if dict_name_ext == None: 
            self.dict_name_ext = {
            "Images" : [".jpeg",".png",".jpg",],
            "WebImages":[".webp"],
            "GIF": [".gif"],
            "Text" : [".doc",".txt",".pdf",".xlsx",".docx"], 
            "Videos" : [".mp4",".mkv",".mov"], 
            "Music & Sounds mp3" : [".mp3"],
            "Music & Sounds other" : [".wav",".m4a"],
            "EXE & Apps" : [".exe",".lnk"], 
            "Codding" : [".c",".py",".java",".cpp",".js",".html",".css",".php"] 
            }
            
        else: 
            self.dict_name_ext = dict_name_ext
    
        
        for key in self.dict_name_ext.keys():
            dont_move.append(key)
            if key not in os.listdir(os.getcwd()): 
                os.makedirs(key)
        
        if self.name_other not in os.listdir(os.getcwd()): 
            os.makedirs(self.name_other)

        for path_file in tqdm(path_files):
            if path_file[1] not in dont_move:
                self._MovingFile(path_file)
                                 
    def _MovingFile(self, path_file):
        for name, extions in self.dict_name_ext.items():
            for extion in extions: 
                if path_file[1].endswith(extion):
                    shutil.move(str(Path(path_file[0])/path_file[1]), str(name))
                    return  
        if not Path(self.name_other, path_file[1]).exists():    
            shutil.move(str(Path(path_file[0])/path_file[1]), self.name_other)
            return
        else:
            return

if __name__ == "__main__":
    Sorter("./") #put the path of the file you want to sort here