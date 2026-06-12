#krishiv
import cv2

detector=cv2.QRCodeDetector()#qr code detector object

video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    if not ret: #if video is working or not
        break  
    
    if cv2.waitKey(25)==32:
        break 
    data,box,_ =detector.detectAndDecode(frame)#it will detect and decode qrcode
    if box is not None:
        n=len(box)
        for i in range(n):
            pt1 = tuple(map(int, box[i][0]))
            pt2 = tuple(map(int, box[(i + 1) % n][0]))
            cv2.line(frame, pt1, pt2, (0, 255, 0), 2)
            cv2.putText(frame,data,(100,75),cv2.FONT_HERSHEY_SIMPLEX,1,(200,90,0),3)

    cv2.imshow("web cam",frame)

     


video.release()
cv2.destroyAllWindows()