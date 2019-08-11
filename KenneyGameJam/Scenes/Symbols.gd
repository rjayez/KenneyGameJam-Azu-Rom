extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	var node = get_node("emote_alert")
	print(node.get_position())
	
	node.set_position(Vector2(500,500))
	
	
	print(node.get_position())
	node.set_scale(Vector2(10,10))
	#var symbols = get_node_in("Symbols")
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
