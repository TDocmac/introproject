///grid_place_meeting(x,y)
var xx = argument[0];
var yy = argument[1];

//original position
var xp = x;
var yp = y;

//check level
if (instance_exists(level)) { var cuadricula = level.grid}
else if (instance_exists(obj_level_s)) {var cuadricula = obj_level_s.grid}
else if (instance_exists(obj_town)) var cuadricula = obj_town.grid;

//update position for collision detection
x=xx;
y=yy;

//x meeting check
var x_meeting = (cuadricula[# bbox_right div cell_w, bbox_top div cell_h] != tfloor) or
                (cuadricula[# bbox_left div cell_w, bbox_top div cell_h] != tfloor);
                
//y meeting check
var y_meeting = (cuadricula[# bbox_right div cell_w, bbox_bottom div cell_h] != tfloor) or 
                (cuadricula[# bbox_left div cell_w, bbox_bottom div cell_h] != tfloor);

var center_meeting = cuadricula[# xx div cell_w, yy div cell_h] != tfloor;              
                
//return original position
x = xp;
y = yp;

//return value
return x_meeting or y_meeting or center_meeting;
