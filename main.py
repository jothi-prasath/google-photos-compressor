import os
from PIL import Image
import pillow_heif
import numpy as np
import multiprocessing

images = []

def get_source():
  while True:
    source_path = input("Enter the path where images are located: ")
    if os.path.exists(source_path):
       return source_path
    else:
       print("Invalid path")
   
def get_target():
  while True:
    target_path = input("Enter the path where images to save: ")
    if os.path.exists(target_path):
      if os.access(target_path, os.W_OK):
        return target_path
      else:
        print("You dont have write permission for this path")
    else:
      try: 
        os.makedirs(target_path)
        return target_path
      except:
        print("You dont have right permission for this path")

def get_threads():
  threads = input("Number of threads (don't know leave it blank): ")
  if threads == "":
    threads=1
    int(threads)
    return int(threads)
  else:
    return int(threads)

def fetch_images(source_path):
  for file in os.listdir(source_path):
    extention = str.lower(os.path.basename(file).split(".")[-1])
    if extention in ["jpg", "jpeg", "png"]:
      images.append(file)

def convert(source_path, target_path, images):
  pillow_heif.register_avif_opener()
  total_count=(len(images))
  count=1
  for image in images:
    temp_image = Image.open(os.path.join(source_path, image))
    print("Converting {} out of {}".format(count,total_count) )
    temp_image.save(os.path.join(target_path, image.strip(image.split(".")[-1]) +"avif"),"avif")
    count += 1

def main():
  source_path = get_source()
  target_path = get_target()
  threads = get_threads()
  fetch_images(source_path)
  jobs = []
  splitted_array = np.array_split(images, threads)
  for i in range(threads):
    p = multiprocessing.Process(target=convert, args=(source_path,target_path,splitted_array[i],))
    jobs.append(p)
    p.start()
  print("Conversion completed successfully")

if __name__ == "__main__":
    main()