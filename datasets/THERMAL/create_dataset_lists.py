import os
from glob import glob
from posixpath import join
import numpy as np
from sklearn.model_selection import train_test_split
import re

PATH_VAL = 'D:/Licenta/Towards-Realtime-MOT/datasets/MOT17/images/train/MOT17-11-SDP'
PATH_TEST = 'D:/Licenta/Towards-Realtime-MOT/datasets/MOT17/images/train/MOT17-13-SDP'
PATHS_TRAIN =['D:/Licenta/Towards-Realtime-MOT/datasets/MOT17/images/train/MOT17-02-SDP',
              'D:/Licenta/Towards-Realtime-MOT/datasets/MOT17/images/train/MOT17-04-SDP',
              'D:/Licenta/Towards-Realtime-MOT/datasets/MOT17/images/train/MOT17-05-SDP',
              'D:/Licenta/Towards-Realtime-MOT/datasets/MOT17/images/train/MOT17-09-SDP',
              'D:/Licenta/Towards-Realtime-MOT/datasets/MOT17/images/train/MOT17-10-SDP']


if __name__ =='__main__':
    res_val = [y for x in os.walk(PATH_VAL) for y in glob(os.path.normpath(join(x[0], '*.jpg')))]
    res_test = [y for x in os.walk(PATH_TEST) for y in glob(os.path.normpath(join(x[0], '*.jpg')))]
    res_train = []
    for path in PATHS_TRAIN:
        res_train +=  [y for x in os.walk(path) for y in glob(os.path.normpath(join(x[0], '*.jpg')))]

    res_train += res_test
    print(res_train)


    # train, test = train_test_split(filtered, test_size=0.3, random_state=12, shuffle=True)
    # val, test = train_test_split(test, test_size=0.5, random_state=145, shuffle=True)
    with open(r'D:/Licenta/Towards-Realtime-MOT/data/mot17.train', 'w') as fp:
        for item in res_train:
            fp.write("%s\n" % item)
    with open(r'D:/Licenta/Towards-Realtime-MOT/data/mot17.val', 'w') as fp:
        for item in res_val:
            fp.write("%s\n" % item)
    with open(r'D:/Licenta/Towards-Realtime-MOT/data/mot17.test', 'w') as fp:
        for item in res_test:
            fp.write("%s\n" % item)
    # res = [print(y) for x in os.walk(PATH) for y in glob(os.path.normpath(join(x[0], '*.jpg')))]
    # res1 = [print(x) for x in os.walk(PATH)]