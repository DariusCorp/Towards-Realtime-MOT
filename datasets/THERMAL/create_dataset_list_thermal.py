import os
from glob import glob
from os.path import isfile
from posixpath import join
import numpy as np
from sklearn.model_selection import train_test_split
import re

PATH = './images'
PATH_TRANS = '../datasets/THERMAL/images'

if __name__ == '__main__':
    res = [join(PATH_TRANS, f) for f in os.listdir(PATH) if isfile(join(PATH, f))]

    res_train, res_test_val = train_test_split(res, test_size=0.3, train_size=0.7, shuffle=False)
    res_test, res_val = train_test_split(res_test_val, test_size=0.5, train_size=0.5, shuffle=False)

    # train, test = train_test_split(filtered, test_size=0.3, random_state=12, shuffle=True)
    # val, test = train_test_split(test, test_size=0.5, random_state=145, shuffle=True)
    with open(r'../../data/thermal.train', 'w') as fp:
        for item in res_train:
            fp.write("%s\n" % item)
    with open(r'../../data/thermal.val', 'w') as fp:
        for item in res_val:
            fp.write("%s\n" % item)
    with open(r'../../data/thermal.test', 'w') as fp:
        for item in res_test:
            fp.write("%s\n" % item)
    # res = [print(y) for x in os.walk(PATH) for y in glob(os.path.normpath(join(x[0], '*.jpg')))]
    # res1 = [print(x) for x in os.walk(PATH)]