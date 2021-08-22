#EC2 Instance and Attaching a 5gb EBS Volume..
#################################################################################################
import boto3
import subprocess as sb
ec2 = boto3.resource('ec2')
# Connecting to AWS..We have to configure our AWS CLI first!!!

def EC2_launch():
    try:
        #LAunching an Ec2 Instance..
        instance = ec2.create_instances(
            ImageId='ami-0ad704c126371a549',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            SecurityGroupIds=['sg-026dd3773ee684723'],
            SubnetId='subnet-c8c5cca0',)
        return (instance[0].id) 
    except:
        print("Configure your AWS CLI first!!\n")

###############################################################################################################################
# Creating a New EBS Volume..
def EBS_create():
    try:
        ec2 = boto3.resource('ec2')
        ebs = ec2.create_volume(AvailabilityZone='ap-south-1a', Size=5, VolumeType='gp2')
        return (ebs.id)
    except:
        print("Please check your internet Connectivity!!\n")
###############################################################################################################################
# Attaching NEW-EBS with the EC2 insatnce        
def Attach_EBS_to_EC2(ins_id,vol_id):
    volume = ec2.Volume(vol_id)
    attach_ebs= volume.attach_to_instance(
        Device='/dev/sdh',
        InstanceId=ins_id,
        VolumeId=vol_id,)
    return 0

#################################################################################################################################
import time
## Using Facial Recognition..For Sending Mail!!     
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def face_detector(img, size=0.5):
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi

# Open Webcam
cap = cv2.VideoCapture(0)
f=0
trigger=0
while True:
    ret, frame = cap.read()
    image, face = face_detector(frame)
    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        results = vimal_model.predict(face)
        if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User'
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)      
        if confidence >=85:
            cv2.imshow("face",face)
            f=f+1
        else:
            print("Come infront of the camera.....")
        if f==25:
            trigger=1
            print("One face detected...Launching EC2 instance")
            break
    except:
        pass
        
    if cv2.waitKey(10) == 13: #13 is the Enter Key
        break
               
cap.release()
cv2.destroyAllWindows()

if trigger==1:
    ec2_launch = EC2_launch()
    ebs=EBS_create()
    time.sleep(30)
    att=Attach_EBS_to_EC2(ec2_launch,ebs)
####################################################################################################################################