from PIL import Image
import os,errno,cv2
import numpy as np

brandlist=dict()

def cropImage(imgname,brandname,x1,y1,x2,y2):
    if brandname in brandlist.keys():
        brandlist[brandname]+=1
    else:
        brandlist.setdefault(brandname,0)
        print("Making Dir "+ "croppedimg/"+brandname)
        if not os.path.isdir( "croppedimg/"+brandname ):
            os.makedirs("croppedimg/"+brandname)
        else:
            pass
        try:
            brandlist.setdefault(brandname,0)
        except KeyError as k:
            print("handled")
    if os.path.isfile("flickr27images/"+imgname):
        try:
            img = cv2.imread("flickr27images/"+imgname)
            print("Processing:"+imgname+" of "+brandname)
            if(x2<x1):
                x1,x2=x2,x1
            if(y2<y1):
                y1,y2=y2,y1
            if y2>=np.size(img, 0):
                y2=np.size(img, 0)
            if x2>=np.size(img, 1):
                x2=np.size(img, 1)
        
            crop_img = img[int(y1):int(y2), int(x1):int(x2)]
            im=Image.fromarray(crop_img)
            print("Saving croppedimg/"+brandname+"/"+brandname+str(brandlist[brandname])+".jpg" )
            im.save("croppedimg/"+brandname+"/"+brandname+str(brandlist[brandname])+".jpg")
        except:
            pass
    else:
        return 

f=open("flickr27imglist.txt","r")
da=f.readlines()
count=0
for line in da:
    imgdesc = line.split()
    if(os.path.isfile("flickr27images/"+imgdesc[0])):
        area=(imgdesc[3],imgdesc[4],imgdesc[5],imgdesc[6])
        imgname=imgdesc[0]
        brandname=imgdesc[1]
        cropImage(imgname,brandname,int(imgdesc[3]),int(imgdesc[4]),int(imgdesc[5]),int(imgdesc[6]))
        count=count+1
print("count="+str(count))