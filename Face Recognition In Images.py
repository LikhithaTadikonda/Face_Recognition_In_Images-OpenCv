#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install opencv-python')


# ### I learned and tried the script in google colab:
# ### Example1- For seeing it works or not on image with single face

# In[ ]:


from google.colab.patches import cv2_imshow
import cv2
img = cv2.imread('p2.jpg',0)


# In[ ]:


cv2_imshow(img)
cv2.waitKey()


# In[ ]:


img.shape


# In[ ]:


import matplotlib.pyplot as plt
img_1= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_1)


# In[ ]:


from google.colab.patches import cv2_imshow  #example1

#load cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#read img
img_1 = cv2.imread('p2.jpg')

#convert to greyscale of each frame
gray = cv2.cvtColor(img_1 , cv2.COLOR_BGR2GRAY)
    
#detects face of diff sizes in input
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h) in faces:
#To draw rectangle in a facee
    cv2.rectangle(img_1, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
cv2_imshow(img_1)
#wait for Esc key to stop
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
  


# ### Example 2 - Testing on an image withmultiple faces

# In[ ]:


img_1 = cv2.imread('multiplefaces.jpg')
cv2_imshow(img_1)


# In[ ]:


from google.colab.patches import cv2_imshow  #example2

#load cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#read img
img_1 = cv2.imread('multiplefaces.jpg')

#convert to greyscale of each frame
gray = cv2.cvtColor(img_1 , cv2.COLOR_BGR2GRAY)
    
#detects face of diff sizes in input
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h) in faces:
#To draw rectangle in a facee
    cv2.rectangle(img_1, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
cv2_imshow(img_1)
#wait for Esc key to stop
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
  


# In[ ]:





# In[ ]:




