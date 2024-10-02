import rospy
from project.srv import multiplier, multiplierResponse

def callback(request):
    return multiplierResponse(request.a * request.b)

def multiply():
    rospy.init_node("multiplier_service")
    service = rospy.Service("multiplier", multiplier, callback)
    rospy.spin()

if __name__ == '__main__':
    multiply()