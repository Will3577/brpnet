# from PIL import Image
# import os

# in_dir = '/Users/will/Downloads/kumar/train/Tissue_Images/'
# out_dir = '/Users/will/Downloads/kumar/train/test/'
# yourpath = os.listdir(in_dir)
# print(yourpath)
# for i in yourpath:
#     im = Image.open(in_dir+i)
#     im.save(out_dir+i.split('.')[0]+'.png')


import scipy.io
import numpy as np
from tempfile import TemporaryFile
outfile = TemporaryFile()
mat = scipy.io.loadmat('/Users/will/Downloads/MATLAB/data_generator_scripts/val/data_after_stain_norm_mm_ref1.mat')
print(type(mat))
np.save('/Users/will/Downloads/MATLAB/data_generator_scripts/val/data_after_stain_norm_mm_ref1.npy', mat)




# import scipy.io
# # mat = scipy.io.loadmat('file.mat')
# in_dir = '/Users/will/Downloads/kumar/train/Annotations0/'
# out_dir = '/Users/will/Downloads/kumar/train/Annotations/'
# yourpath = os.listdir(in_dir)
# print(yourpath)
# for i in yourpath:
#     mat = scipy.io.loadmat(in_dir+i)
#     print(mat)
#     break
#     im.save(out_dir+i.split('.')[0]+'.xml')

# for root, dirs, files in os.walk(yourpath, topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#         if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
#             if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
#                 print ("A jpeg file already exists for %s" % name)
#             # If a jpeg is *NOT* present, create one from the tiff.
#             else:
#                 outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
#                 try:
#                     im = Image.open(os.path.join(root, name))
#                     print ("Generating jpeg for %s" % name)
#                     im.thumbnail(im.size)
#                     im.save(outfile, "JPEG", quality=100)
#                 except Exception, e:
#                     print e