import numpy as np
import cv2
img = cv2.imread('../images/typewriter.jpg')
#print(img.shape)

# read files of classes
all_rows = open('../model/synset_words.txt').read().strip().split("\n")

# gets descriptions not including ID
classes = [r[r.find(' ') + 1:] for r in all_rows]

# reads in files
net = cv2.dnn.readNetFromCaffe('../model/bvlc_googlenet.prototxt','../model/bvlc_googlenet.caffemodel')

# creates blob
blob = cv2.dnn.blobFromImage(img, 1, (224, 224))

# set as input to network
net.setInput(blob)

# forward pass to get predictions/probability for all 1000 classes
outp = net.forward()
#print(outp)

# top 5 predictions for the image
# sorts in descending order of probability and gets top 5 classes
idx = np.argsort(outp[0])[::-1][:5]

# displays predictions, associated labels, & their predicted probability
for (i,id) in enumerate(idx):
    print('{}. {} ({}): Probability {:.3}%'.format(i+1, classes[id], id, outp[0][id]*100))

# for (i,c) in enumerate(classes):
#     if i==4:
#         break
#     print(i,c)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# RETURNS
# 1. typewriter keyboard (878): Probability 85.4%
# 2. space bar (810): Probability 5.45%
# 3. radiator (753): Probability 2.01%
# 4. switch, electric switch, electrical switch (844): Probability 0.888%
# 5. stove (827): Probability 0.873%
