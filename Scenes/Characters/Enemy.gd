extends KinematicBody

# class member variables go here, for example:
# var velocity = Vector3(1, 0, 0)
var speed = 20
var radius = 5
var time = 0.0
var centre = Vector3()
var offset = Vector3()
var pos = Vector3()
var T = 0.0

# var period = 2

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	# centre = Vector3(translation.x, 0, -translation.x)
	#centre = Vector3(radius/sqrt(2), 0, radius/sqrt(2))
	T = 2*PI*radius/speed
	#centre = Vector3(-translation.x, 0, -translation.x)
	centre = Vector3(0, 0, 0)
	pass

func _process(delta):
	# Called every frame. Delta is time since last frame.
	# Update game logic here
	# step += 1
	time += delta/T
	
	# offset = Vector3(sin(angle), 0, cos(angle))*radius
	offset = Vector3(cos(time), 0, sin(time))*radius
	pos = centre + offset
	move_and_slide(pos)
	
	
	#print('time = ', time, ', delta = ', delta, ', offset = ', offset, ', centre = ', centre, ',  pos = ', pos)
	#print('translation.x = ', translation.x, '; translation.y = ', translation.y,'; translation.z = ', translation.z)

#
#func _on_Player_body_entered():
#	self.queue_free()

	
	
	

func _on_Area_body_entered(body):
#	if body.name == "Player":
	if body.is_in_group("Weapon"):
		self.queue_free()
