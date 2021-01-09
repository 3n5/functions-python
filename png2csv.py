"""pngをcsvに変換（相関係数をもとめるため）"""
import numpy as np
import imageio

file="900o"
def png2csv(file):
    img = (imageio.imread("{0}.png".format(file), as_gray=True))
    img = np.array(img)

    np.savetxt("{0}.csv".format(file), img, delimiter=",")

png2csv("z48mm_rot000_3")
png2csv("z40mm_rot004_3")

png2csv("z40mm_rot000_3")
png2csv("re_z48mm_00deg_phs")
png2csv("re_z48mm_00deg_amp")
png2csv("re_z40mm_04deg_phs")

png2csv("re_z40mm_04deg_amp")
png2csv("re_z40mm_00deg_phs")
png2csv("re_z40mm_00deg_amp")