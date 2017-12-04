import os

from utils import misc_utils as mu

import sys
sys.path.append('/home/peter/byfield554@gmail.com/projects/stains')
import stainNorm_Vahadane as stain

data_dir = '/home/peter/datasets/ICIAR2018_BACH_Challenge/Photos'
save_dir = '/home/peter/datasets/ICIAR2018_BACH_Challenge/BACH_normalized'

classes = ('Benign', 'InSitu', 'Invasive', 'Normal')
prefixes = {'Benign': 'b', 'InSitu': 'is', 'Invasive': 'iv', 'Normal': 'n'}

target = mu.read_image(os.path.join(data_dir, 'Benign', 'b027.tif'))
n=stain.normalizer()
n.fit(target)

for c in classes:
    for i in range(100):
        filename = prefixes[c] + mu.i2str(i + 1) + '.tif'
        print('Doing Image {}'.format(filename))
        path = os.path.join(data_dir, c, filename)
        image = mu.read_image(path)

        normal = n.transform(image)

        save_filename = prefixes[c] + mu.i2str(i + 1) + '_normalized.png'
        save_path = os.path.join(save_dir, c, save_filename)

        mu.save_aspng(normal, save_path, compression=1)
