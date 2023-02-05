import os
import os.path as osp
import random
import shutil
from pathlib import Path

ROOT = 'E:/flower_dataset/'
MODE = {'train': 0.8, 'val': 0.2}

cls_names = os.listdir(ROOT)
# 1.create classes.txt
with open(osp.join(ROOT, 'classes.txt'), 'w') as f:
    for cls in cls_names:
        f.writelines(cls + '\n')
# 2.create train, val folders
for mode in MODE.keys():
    Path(osp.join(ROOT, mode)).mkdir(parents=True, exist_ok=True)
    for cls in cls_names:
        Path(osp.join(ROOT, mode, cls)).mkdir(parents=True, exist_ok=True)
# 3.prepare train, val images
cls_idx = 0
for cls in cls_names:
    # get all img original paths
    img_paths = [osp.join(ROOT, cls, img_name)
                 for img_name in os.listdir(osp.join(ROOT, cls))]
    # split all img original paths to train, val paths
    num_imgs = len(img_paths)
    print(f'{cls} total: {num_imgs}')
    num_train_imgs = int(num_imgs * MODE['train'])
    random.shuffle(img_paths)
    train_img_paths = img_paths[:num_train_imgs]
    val_img_paths = img_paths[num_train_imgs:]
    print(f'{cls} train: {num_train_imgs}')
    print(f'{cls} val: {num_imgs - num_train_imgs}')
    # copy files
    for i in train_img_paths:
        shutil.copy(i, osp.join(ROOT, 'train', cls))
    for i in val_img_paths:
        shutil.copy(i, osp.join(ROOT, 'val', cls))
    # write info into train.txt and val.txt
    with open(osp.join(ROOT, 'train.txt'), 'a') as f:
        for img_name in os.listdir(osp.join(ROOT, 'train', cls)):
            f.writelines(f'{cls}/{img_name} {cls_idx}\n')
    with open(osp.join(ROOT, 'val.txt'), 'a') as f:
        for img_name in os.listdir(osp.join(ROOT, 'val', cls)):
            f.writelines(f'{cls}/{img_name} {cls_idx}\n')
    cls_idx += 1


