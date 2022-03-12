from PIL import Image
import os
def should_delete(img, minimum_content):
    
    img = Image.open(img)
    pixels = img.load()
    
    bg_color = 0
    values = []
    print(img.height, img.width)
    for y in range(0, img.height):
        
        for x in range(0, img.width):
            pixel = pixels[x, y]
            if x == 0 and y == 0:
                values.append(pixel[0])
                values.append(pixel[1])
                values.append(pixel[2])
            
            
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if r == values[0] and g == values[1] and b == values[2]:
                bg_color += 1
    content = (img.width*img.height) - bg_color
    if content < minimum_content:
        print("[locate_bad_images] bad image found \n")
        return True
    else:
        print("[locate_bad_images] good image \n")
        return False
def delete_file(img_dir, json_dir, filename_img, filename_json):
    if should_delete(f"{img_dir}/{filename_img}", 4500):
        os.remove(f"{img_dir}/{filename_img}")
        os.remove(f"{json_dir}/{filename_json}")
        print("Removed file")

def rename_directories(dir1, dir2):
    current_file = 0
    path, dirs, files = next(os.walk(dir1))
    for file in files:
        new_image_name = f"{current_file}.png"
        os.rename(f"{dir1}/{file}", f"{dir1}/{new_image_name}")

        new_json_name = f"{current_file}.json"
        json_file_name = file[:len(file)-4] + ".json"
        os.rename(f"{dir2}/{json_file_name}", f"{dir2}/{new_json_name}")
        print("Renamed")

        current_file += 1
    print("Completed")

