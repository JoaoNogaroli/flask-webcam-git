from distutils.log import debug
from flask import Flask, render_template, Response, request
import cv2


app =Flask(__name__)



def generate_frames():
    global camera
    camera = cv2.VideoCapture(-1,2)
    while True:
        ## read the camera frame
        success, frame=camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            print('-------funcionou-------')
        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')    
def video():
    print('----funcaovideooo----')
    print(f"MEU IP ---{request.remote_addr}")
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run()