extends KinematicBody

# class member variables go here, for example:
# var a = 2
# var b = "textvar"
var speed = 50
var gravity = 10
var cameraDirection

var initMouse = Vector2(500,200)
var lastMouse = initMouse
var mousespeed = 0.001
var minScale = Vector3(0.5, 0.5, 0.5)
var maxScale = Vector3(2, 2, 2)
var maxRoll = 0.3
var mouseCapture = false
var freelook = false
var yawNode
var pitchNode
var rollNode
var cameraNode
var velocity = Vector3()
var run = 1

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	yawNode = get_node("yaw")
	pitchNode = get_node("yaw/pitch")
	rollNode = get_node("yaw/pitch/roll")
	cameraNode = get_node("yaw/pitch/roll/Camera")
	
	
	
func _process(delta):
	var direction = Vector3(0,0,0)
	
	
	if not Input.is_key_pressed(KEY_Z):
		mouseCapture = true
		Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)
	else:
		mouseCapture = false
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
	
	freelook = Input.is_key_pressed(KEY_ALT)

	# vector from camera to player
	
	var cameraOrigin = cameraNode.get_global_transform().origin
	var playerOrigin = get_global_transform().origin
	cameraDirection =  playerOrigin - cameraOrigin

	# ===================== movement =====================
	if Input.is_key_pressed(KEY_W):
		direction += Vector3(cameraDirection.x, cameraDirection.y, cameraDirection.z)
	if Input.is_key_pressed(KEY_S):
		direction -= Vector3(cameraDirection.x, cameraDirection.y, cameraDirection.z)
	if Input.is_key_pressed(KEY_A):
		direction += Vector3(cameraDirection.z, 0, -cameraDirection.x)
	if Input.is_key_pressed(KEY_D):
		direction += Vector3(-cameraDirection.z, 0, cameraDirection.x)
		
	if Input.is_key_pressed(KEY_SHIFT):
		run = 2
	else:
		run = 1
	
	direction = direction.normalized() * delta * speed * run
	
	
	# Kinda gravity	
	velocity.y -= gravity * delta
	velocity.x = direction.x
	velocity.z = direction.z
	
		
	# Move
	velocity = move_and_slide(velocity, Vector3(0,1,0))
	
	
	# Jump 
	if Input.is_key_pressed(KEY_SPACE) and is_on_floor():
		print("JUMP MOTHERFUCKER!!!")
		velocity.y = 5
		
	# ========================= CAMERA ==========================
	
	if mouseCapture:
		get_viewport().warp_mouse(initMouse)
		lastMouse = get_viewport().get_mouse_position()
		
		if abs(lastMouse.x - initMouse.x) > 2:
			if freelook:
				yawNode.rotate_y(-(lastMouse.x - initMouse.x) * mousespeed)	
			else:
				# TODO: SET YAW BACK TO CameraDirection
				rotate_y(-(lastMouse.x - initMouse.x) * mousespeed)		
		if abs(lastMouse.y - initMouse.y) > 2:
			pitchNode.rotate_x(-(lastMouse.y - initMouse.y) * mousespeed)

		
		
		# DEBUG
#		if Input.is_key_pressed(KEY_RIGHT):
#			yawNode.rotate_y(0.1)
#		if Input.is_key_pressed(KEY_LEFT):
#			yawNode.rotate_y(-0.1)
#		if Input.is_key_pressed(KEY_UP):
#			pitchNode.rotate_x(0.1)
#		if Input.is_key_pressed(KEY_DOWN):
#			pitchNode.rotate_x(-0.1)
#
		
		
		
		
		# Camera translation
		if Input.is_mouse_button_pressed(BUTTON_RIGHT) and yawNode.scale > minScale:
			# zoom in
			yawNode.scale = yawNode.scale * Vector3(0.95, 0.95, 0.95)
			print(yawNode.scale)
	    # Wheel Down Event
		elif Input.is_mouse_button_pressed(BUTTON_LEFT) and yawNode.scale < maxScale:
			# zoom out
			yawNode.scale = yawNode.scale * Vector3(1.05, 1.05, 1.05)
			print(yawNode.scale)
	
	# ========================= ROLL ==============================
	# Roll up to maxRoll in both cameraDirectionections
	var current = rollNode.get_transform().basis.x.angle_to(Vector3(1,0,0))
#	print(current)
	if Input.is_key_pressed(KEY_Q) and current < maxRoll:
		rollNode.rotate_z(0.01)
	if Input.is_key_pressed(KEY_E) and current < maxRoll:
		rollNode.rotate_z(-0.01)
	
	# Duplicating  node to rotate it right and check the cutrrent cameraDirectionection
	var dup = rollNode.duplicate()
	dup.rotate_z(0.0001)
	var dupRoll = dup.get_transform().basis.x.angle_to(Vector3(1,0,0))
	var isRolledRight
	
#	print('current = ' + str(current))
#	print('dupRoll = ' + str(dupRoll))
#	print(current - dupRoll)
	if current > dupRoll:
		isRolledRight = true
	else:
		isRolledRight = false
	dup.rotate_z(-0.0001)
	dup.free()
	
	if abs(current - 0) > 0.001:
		if isRolledRight == true and not Input.is_key_pressed(KEY_E):
			rollNode.rotate_z(0.005)
		elif isRolledRight == false and not Input.is_key_pressed(KEY_Q):
			rollNode.rotate_z(-0.005)
			
