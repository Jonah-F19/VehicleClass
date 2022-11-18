import jetson.inference
import jetson.utils

net = jetson.inference.detectNew("ssd-mobilenet-v2", threshhold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput()

while True:
    img = camera.Capture()
    detections = net.Detect(img)
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNewtworkFPS())) 