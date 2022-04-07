import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    print("Snapshot Taken")
    # releases the camera
    videoCaptureObject.release()
    cv2.destroyAllWindeows()
def upload_file(img_name):
    access_token="sl.BFSE7GTPGZBh9Qb3GhlThF3Ygyg1-nbMWkIZSBB2d6dd-uNoOH8BYTdbCm2DB9jImToDESV6rq8tk6UiJYxD6gPYmrAnVsyxWQ9uJYIID9ll0zpHQCE9deNkqO67Ac2u--VtLhdXIy3q"
    file=img_name
    file_from=file
    file_to="/testFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()
    
