

inorder to check the output and accuracy of the dataset of images just run the following command

          python assignment.py --train_path images/train/ --test_path images/test/



This assignment consists of the following folders and files


*********** folders **********

images ---->  consists two folders test and train which consists of folders of testing and training images.

output ---->  consists of predicted object name as the filename for every test image.


*********** files ************

assignment.py        ---->  Main assignment file that consists of BOW representation of the SIFT features.

KMeans.py            ---->  Uses the sklearn's KMeans algorithm

helpers.py           ---->  Consists of all the helpers classes

confusion_matrix.py  ---->  Representation of the confusion_matrix




Report.pdf           ---->  Describes about the conclusions obtained by varying the parameters such as the
                            size of the training data, and k in k-means. The confusion matrix obtained.
