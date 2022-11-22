# Vehicle Detection
Hello, My name is Jonah Figdor. I decided to create a project, surronding my interest in cars, originally I had planned for my Project to be of use to aspiring and new mechanics, the inaccuracy and small class sizes limited this to more of a project I was just creating for fun.
## The Algorithm
I collected the data for my assignment by using the built in data camera capture tool in the nano, taking and annotating many printed out photos, consisting of my four classes, Body, Wheels, Supsension, Engine. Once I had collected my Data, I trained through the DetectNet netwok, allowing me to locate objects on a live camera feed and classify them.
## Instructions to run the project
1)First you would have to create a directory on your Jetson nano in your jetson-inference/python/training/detection/ssd folder

2)Then you would add my git repository to that directory by cding into that directory than entering `git remote add origin https://github.com/Jonah-F19/VehicleClass` than do  `git pull origin master`

2)Next you would open the terminal in your nano, headed, headless ssh, and headless serial all work, but to see the display window you will need to be in headed

3)Once you have done that you will cd into your jetson-inference, and run the docker container which is `./docker/run.sh`

4)Than you should cd into python/training/detection/ssd folder

5)Than you will run the code: `detectnet.py --model=”new_directory_name”/ssd-mobilenet.onnx --labels=”new_directory_name”labels.txt --input-blob=input_0 --output-cvg=scores --output-bbox=boxes /dev/video0 
`

a)Your camera input may not be /dev/video0, but that is the default, if not just enter your camera input

7)Once you run that you should see the display window (If it is in headed)pop up, and it should recognize images of cars, wheels, suspension, and a engine. If you are in headless you should see a line saying how many classes it is detection when you put one of the earlier mentioned objects in front of the camera.
## Demo Videos
Part 1: https://drive.google.com/file/d/1FOcYRen-rdd1EY1dTBccer4Kz07O16Tc/view?usp=share_link

Part 2: https://drive.google.com/file/d/1NZ2smxqPblTxALSzlig4K3npTVrfOsaK/view?usp=share_link
