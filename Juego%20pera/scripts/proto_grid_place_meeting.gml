///proto_grid_place_meeting(x,y)
var xx = argument[0];
var yy = argument[1];

//original position
var xp = x;
var yp = y;

//update position for collision detection
x=xx;
y=yy;

//x meeting check
var x_meeting = (level_proto.grid[# bbox_right div pcell_w, bbox_top div pcell_h] != tfloor) or
                (level_proto.grid[# bbox_left div pcell_w, bbox_top div pcell_h] != tfloor);
                
//y meeting check
var y_meeting = (level_proto.grid[# bbox_right div pcell_w, bbox_bottom div pcell_h] != tfloor) or 
                (level_proto.grid[# bbox_left div pcell_w, bbox_bottom div pcell_h] != tfloor);

var center_meeting = level_proto.grid[# xx div pcell_w, yy div pcell_h] != tfloor;              
                
//return original position
x = xp;
y = yp;

//return value
return x_meeting or y_meeting or center_meeting;
