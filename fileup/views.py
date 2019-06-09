from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import os
import time
import _thread
import requests
import random
 
IMAGE_URL='https://mdlzz.top/upload/1.png'
    
def index(request):
    _thread.start_new_thread( getImage, ("Thread-1", 0.25, ) )
    return render(request, 'fileup/index.html')

def upload_file(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        myFile.name='fore.png'
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("./fileup/static/image", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作,
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over! file in /static/image/"+myFile.name)
        #return HttpResponseRedirect('http://localhost/')
    if request.method == "GET":
        return render(request, 'fileup/upload.html')
    
def getImage( threadName, delay):
   while 1:
       try:
           time.sleep(delay)
           print("hellokitty")
           r = requests.get(IMAGE_URL)
           flagf = open('./fileup/static/image/row','wb')
           flagf.close()
           with open('./fileup/static/image/fore.png', 'wb') as f:
               f.write(r.content)
           filename='./fileup/static/image/gen'
           afterPng='./fileup/static/image/after.png'
           overPng='./fileup/static/image/'
           if (os.path.isfile(filename) and os.path.isfile(afterPng)):
               os.remove(filename)
               if os.path.isfile(overPng):
                   os.remove(overPng)
               old_f = open('./fileup/static/flag.txt','r') # 读模式 删除之前的图片
               old_name=old_f.readline()
               print("Old file is "+old_name )
               os.remove(overPng+str(old_name)+'.png')

               flag=random.randint(100000,300000)
               flag_txt=open('./fileup/static/flag.txt','w') #文件名字·写入
               flag_txt.write(str(flag))
               flag_txt.close()
               final_str=overPng+str(flag)+'.png'
               os.rename(afterPng,final_str)
               print("has file")
       except Exception as e:
           print(e)
      

