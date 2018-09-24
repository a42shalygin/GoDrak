extends Skeleton

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var timer = 0
# Called when the node enters the scene tree for the first time.
func _ready():
    physical_bones_start_simulation()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	
	if Input.is_key_pressed(KEY_ALT):
		timer += delta
		
	if timer >= 0.1:
		if not $pCube1.visible:
			$pCube1.visible = true
		else:
			$pCube1.visible = false
		
		timer = 0
