extends Area

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	pass




func _on_Interior_body_entered(body):
	if body is KinematicBody:
		get_node("Torch").light_energy = 0.1
		


func _on_Interior_body_exited(body):
	if body is KinematicBody:
		get_node("Torch").light_energy = 0
