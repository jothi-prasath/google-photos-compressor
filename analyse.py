import os
from collections import defaultdict

counts = defaultdict(int)

def get_source_path():
   while True:
      source_path = input("Enter the path: ")
      if os.path.exists(source_path):
         return source_path
      else:
         print("Invalid path")
      
def analyse(source_path):
   for filenames in os.listdir(source_path):
      extention = str.lower(os.path.basename(filenames).split(".")[-1])
      if extention in ["jpg", "jpeg"]:
         counts["jpg"] += 1
      elif extention in ["png"]:
         counts["png"] += 1
      elif extention in ["heic"]:
         counts["heic"] += 1
      elif extention in ["avif"]:
         counts["avif"] += 1
      elif extention in ["mp4", "mkv", "3gp"]:
         counts["videos"] += 1
      else: 
         counts["other"] += 1

def main():
   source_path = get_source_path()
   analyse(source_path)
   print("---------------------------------")
   print("No of JPG files: ", counts["jpg"])
   print("No of PNG files: ", counts["png"])
   print("No of HEIC files: ", counts["heic"])
   print("No of AVIF files: ", counts["avif"])
   print("No of video files: ", counts["videos"])
   print("No of Other files: ", counts["other"])
   print("---------------------------------")

if __name__ == "__main__":
    main()