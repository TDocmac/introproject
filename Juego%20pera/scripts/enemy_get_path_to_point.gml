///get_path_to_point(xx,yy,speed, mpgrid)
// for player position ((obj_player.x div cell_w)*cell_w+cell_w/2, (obj_player.y div cell_h)*cell_h+cell_h/2) 
if (instance_exists(obj_player)) {
    var xx = argument[0];
    var yy = argument[1];
    var spd = argument[2];
    var mpgrid = argument[3];
    if (mp_grid_path(mpgrid, path, x, y, xx, yy, true)) {      
        path_start(path, spd, path_action_stop, false);
    }
    
}
