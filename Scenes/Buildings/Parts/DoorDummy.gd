extends Spatial

var player
var door_open
var entered

func _ready():
	door_open = false
	player = AudioStreamPlayer.new()
	self.add_child(player)
	player.stream = load('res://Sounds/Door.wav')
#	player.get_volume_db()
#	player.play()

func _process(delta):
	print(player.is_playing())


func _on_Area_body_entered(body):
		
	if body.name == "Player":
#		print('entered')
#		print(door_open)
		if $AnimationPlayer.current_animation == "":
			player.play()
			if door_open==true:
#				print('closing')
				$AnimationPlayer.play('close')
				door_open = false
#				print(door_open)
			else:
#				print('opening')
				$AnimationPlayer.play('open')
				door_open = true
#				print(door_open)
