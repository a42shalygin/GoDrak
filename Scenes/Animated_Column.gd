extends Spatial
var timer = 0
# class member variables go here, for example:
# var a = 2
# var b = "textvar"

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	pass
	

func _process(delta):
	var anim = $AnimationPlayer
	if(not anim.is_playing()):
    	anim.play("default")
		
	if Input.is_key_pressed(KEY_ALT):
		timer += delta
		
	if timer >= 0.05:
		if not $Skeleton/pCube1.visible:
			$Skeleton/pCube1.visible = true
		else:
			$Skeleton/pCube1.visible = false
		
		timer = 0
	
