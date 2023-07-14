import os
from collections import defaultdict

counts = defaultdict(int)
size = defaultdict(int)

def get_source_path():
   while True:
      source_path = input("Enter the path: ")
      if os.path.exists(source_path):
         return source_path
      else:
         print("Invalid path")

def bytes_to_mb(bytes):
    mb = "{:.2f}".format(round(bytes / 1000000))
    return mb
      
def analyse(source_path):
   for filenames in os.listdir(source_path):
      extention = str.lower(os.path.basename(filenames).split(".")[-1])
      file_size = os.path.getsize(os.path.join(source_path,filenames))
      if extention in ["jpg", "jpeg"]:
         counts["jpg"] += 1
         size["jpg"] += file_size
      elif extention in ["png"]:
         counts["png"] += 1
         size["png"] += file_size
      elif extention in ["heic"]:
         counts["heic"] += 1
         size["heic"] += file_size
      elif extention in ["avif"]:
         counts["avif"] += 1
         size["avif"] += file_size
      elif extention in ["gif"]:
         counts["gif"] += 1
         size["gif"] += file_size
      elif extention in ["mp4", "mkv", "mov", "3gp"]:
         counts["videos"] += 1
         size["videos"] += file_size
      else: 
         counts["other"] += 1
         size["other"] += file_size

def main():
   source_path = get_source_path()
   analyse(source_path)
   print("---------------------------------")
   print("No of JPG files:   {}     {} Mb".format(counts["jpg"],bytes_to_mb(size["jpg"])))
   print("No of PNG files:   {}     {} Mb".format(counts["png"],bytes_to_mb(size["png"])))
   print("No of HEIC files:  {}     {} Mb".format(counts["heic"],bytes_to_mb(size["heic"])))
   print("No of AVIF files:  {}     {} Mb".format(counts["avif"],bytes_to_mb(size["avif"])))
   print("No of GIF files:   {}     {} Mb".format(counts["gif"],bytes_to_mb(size["gif"])))
   print("No of video files: {}     {} Mb".format(counts["videos"],bytes_to_mb(size["videos"])))
   print("No of Other files: {}     {} Mb".format(counts["other"],bytes_to_mb(size["other"])))
   print("---------------------------------")

if __name__ == "__main__":
    main()