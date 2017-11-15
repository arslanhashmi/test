import cv2
import time
import io
import bson      # this is installed with the pymongo package
import pandas as pd
import matplotlib.pyplot as plt
from skimage.data import imread   # or, whatever image library you prefer
import multiprocessing as mp      # will come in handy due to the size of the data
data = bson.decode_file_iter(open('dataset/train_example.bson', 'rb'))

prod_to_category = dict()

print (data[0])

for c, d in enumerate(data):
    
    product_id = d['_id']
    category_id = d['category_id'] # This won't be in Test data
    prod_to_category[product_id] = category_id
    

    #print (d['imgs'])
    for e, pic in enumerate(d['imgs']):
        #print (str(e))
        time.sleep(2)
        picture = imread(io.BytesIO(pic['picture']))
        #print(picture)
        cv2.imwrite(str(product_id)+"X"+str(category_id)+'.jpg', picture)
        #cv2.imshow('Color image', picture)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        # do something with the picture, etc
        

prod_to_category = pd.DataFrame.from_dict(prod_to_category, orient='index')
prod_to_category.index.name = '_id'
prod_to_category.rename(columns={0: 'category_id'}, inplace=True)


prod_to_category.head()
