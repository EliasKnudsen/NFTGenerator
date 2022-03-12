import generate_func as gf
import random
import os
import json
import numpy as np
import gen
def get_depth_and_func_rarity():
    probability = 0.7
    depth = 1
    rarity = 1
    while random.uniform(0, 1) <= probability:
        depth+=1
        rarity *= 0.3
    return [depth, rarity]

def generate_json(json_data):
    filename = get_filename("ImagesMetadata", ".json")
    f = open(f"ImagesMetadata/{filename}", "w")
    json.dump(json_data, f)
    f.close()
    
def get_filename(dir, filetype):
    path, dirs, files = next(os.walk(dir))
    file_count = len(files)
    return str(file_count) + filetype

def weighted_to_prob(attributes, index):
    weight_sum = sum(attributes[index]["probabilities"])
    
    prob = []
    for i in attributes[index]["probabilities"]:
        prob.append(i/weight_sum)
    return (prob, weight_sum)
def execute():

    metadata = {
    }

    depth_and_rarity_a = get_depth_and_func_rarity()
    depth_a = depth_and_rarity_a[0]
    rarity_a = depth_and_rarity_a[1]
    func_a = gf.generate_function(depth_a)
    depth_and_rarity_b = get_depth_and_func_rarity()

    depth_b = depth_and_rarity_b[0]
    rarity_b = depth_and_rarity_b[1]
    func_b = gf.generate_function(depth_b)
    
    attributes_file = open("attributes.json", "r")
    attributes = json.load(attributes_file)

    cmap_probs = weighted_to_prob(attributes, 1)
    cmap_weight_sum = cmap_probs[1]
    cmap = np.random.choice(attributes[1]['elements'], 1, p=cmap_probs[0])[0]
    cmap_prob = attributes[1]["probabilities"][attributes[1]["elements"].index(cmap)]/cmap_weight_sum


    projection_probs = weighted_to_prob(attributes, 0)
    projection_weight_sum = projection_probs[1]
    projection = np.random.choice(attributes[0]['elements'], 1, p=projection_probs[0])[0]
    projection_prob = attributes[0]["probabilities"][attributes[0]["elements"].index(projection)]/projection_weight_sum

    bg_probs = weighted_to_prob(attributes, 2)
    bg_weight_sum = bg_probs[1]
    bg_color = np.random.choice(attributes[2]['elements'], 1, p=bg_probs[0])[0]
    bg_color_prob = attributes[2]["probabilities"][attributes[2]["elements"].index(bg_color)]/bg_weight_sum


   
    metadata["function_1"] = func_a
    metadata["function_2"] = func_b
    metadata["function_1_prob"] = rarity_a
    metadata["function_2_prob"] = rarity_b
    metadata["projection"] = projection
    metadata["projection_probability"] = projection_prob
    if cmap[len(cmap)-2:] == "_r":
        cmap = cmap[0:len(cmap)-2]
    print(cmap)

    metadata["gradient"] = cmap
    metadata["gradient_probability"] = cmap_prob
    metadata["background_color"] = bg_color
    metadata["background_color_prob"] = bg_color_prob
    print(projection)
    

    with open("main.cpp", "r+") as cpp_file:
        cpp_content = cpp_file.readlines()
        

    with open("main.cpp", "r+") as cpp_file:
        cpp_content = cpp_file.readlines()

    def get_line_index(pattern):
        for idx, el in enumerate(cpp_content):
            if el.find(pattern) != -1:
                return idx
        return -1
    

    RNUM_LINE = get_line_index("INSERT_RNUM") + 1

    if RNUM_LINE:
        cpp_content[RNUM_LINE] = f"const double RNUM = {random.uniform(-10, 10)};\n"

    F1_LINE = get_line_index("INSERT_F1") + 1

    if F1_LINE:
        cpp_content[F1_LINE] = f"    return RNUM * {func_a};\n"

    F2_LINE = get_line_index("INSERT_F2") + 1

    if F2_LINE:
        cpp_content[F2_LINE] = f"    return RNUM * {func_b};\n"

    with open('main.cpp', 'w') as cpp_file:
        cpp_file.writelines(cpp_content)

    os.system("g++ main.cpp")
    os.system("./a.out > out.out")
    os.system('echo "[a.out] Executed a.out"')
    if(gen.gen(cmap, projection, bg_color)):
        generate_json(metadata)

    else:
        print(f"[gen.py] bad image found")

for i in range(0, 2000):
    execute()
