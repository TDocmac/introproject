/// Movimiento
if (instance_exists(level)) {
player_get_path_to_point(obj_pointer.x,obj_pointer.y,3,level.mpgrid);
}
else if (instance_exists(obj_level_s)) {
player_get_path_to_point(obj_pointer.x,obj_pointer.y,3,obj_level_s.mpgrid);
}
else{
player_get_path_to_point(obj_pointer.x,obj_pointer.y,3,obj_town.mpgrid);
}

