import os, shutil
import sys

"""
需要满足以下条件：
1. 在JPEGImages中准备好图片
2. 在labels中准备好labels
3. 以下代碼會创建好如下所示的文件目录：
    - images
        - train0712
        - val0712
        - test0712
    - labels(由于voc格式中有labels文件夹，所以重命名为label)
        - train2014
        - val2014
        - test0712
"""
def make_dir(image_dir):
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

def make_for_torch_yolov3(dir_image,
                                 dir_label,
                                 dir1_train,
                                 dir1_val,
                                 dir1_test,
                                 dir2_train,
                                 dir2_val,
                                 dir2_test,
                                 main_trainval,
                                 main_train,
                                 main_val,
                                 main_test):
    make_dir(dir1_train)
    make_dir(dir1_val)
    make_dir(dir1_test)

    make_dir(dir2_train)
    make_dir(dir2_val)
    make_dir(dir2_test)

    with open(main_train, "r") as f1:
        for line in f1:
            print(line[:-1], '\r', end="")
            sys.stdout.flush()
            shutil.copy(os.path.join(dir_image, line[:-1] + ".jpg"),
                    os.path.join(dir1_train, line[:-1] + ".jpg"))
            shutil.copy(os.path.join(dir_label, line[:-1] + ".txt"),
                    os.path.join(dir2_train, line[:-1] + ".txt"))


    with open(main_val, "r") as f2:
        for line in f2:
            print(line[:-1], '\r', end="")
            sys.stdout.flush()
            shutil.copy(os.path.join(dir_image, line[:-1] + ".jpg"),
                    os.path.join(dir1_val, line[:-1] + ".jpg"))
            shutil.copy(os.path.join(dir_label, line[:-1] + ".txt"),
                    os.path.join(dir2_val, line[:-1] + ".txt"))


    with open(main_test, "r") as f3:
        for line in f3:
            print(line[:-1], '\r', end="")
            sys.stdout.flush()
            shutil.copy(os.path.join(dir_image, line[:-1]+".jpg"),
                        os.path.join(dir1_test, line[:-1]+".jpg"))
            shutil.copy(os.path.join(dir_label, line[:-1]+".txt"),
                        os.path.join(dir2_test, line[:-1]+".txt"))

if __name__ == "__main__":
    '''
    https://github.com/ultralytics/yolov3
    这个pytorch版本的数据集组织
    - images
        - train2014 # dir1_train
        - val2014 # dir1_val
        - test2014 #dir1_test
        
    - labels
        - train2014 # dir2_train
        - val2014 # dir2_val
        - test2014 # dir2_test
    trainval.txt,train.txt,val.txt, test.txt 是由create_main.py构建的
    '''

    dir_image = "./JPEGImages"
    dir_label = "./voc_labels"

    dir1_train = "./images/train0712"
    dir1_val = "./images/val0712"
    dir1_test = "./images/test0712"

    dir2_train = "./label/train0712"
    dir2_val = "./label/val0712"
    dir2_test = "./label/test0712"

    main_trainval = "./ImageSets/Main/trainval.txt"
    main_train = "./ImageSets/Main/train.txt"
    main_val = "./ImageSets/Main/val.txt"
    main_test = "./ImageSets/Main/test.txt"



    make_for_torch_yolov3(dir_image,
                            dir_label,
                            dir1_train,
                            dir1_val,
                            dir1_test,
                            dir2_train,
                            dir2_val,
                            dir2_test,
                            main_trainval,
                            main_train,
                            main_val,
                            main_test)
