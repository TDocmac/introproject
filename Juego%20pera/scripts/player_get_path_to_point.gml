///get_path_to_point(xx,yy,speed, mpgrid)
// for player position ((obj_player.x div cell_w)*cell_w+cell_w/2, (obj_player.y div cell_h)*cell_h+cell_h/2) 
if (instance_exists(obj_player)) {
    var xx = argument[0];
    var yy = argument[1];
    var spd = argument[2];
    var mpgrid = argument[3];
    sprite_direction = round(point_direction(x,y,obj_pointer.x,obj_pointer.y));
    if (mp_grid_path(mpgrid, path, x, y, xx, yy, true)) {      
        path_start(path, spd, path_action_stop, false);
        if (point_distance(x,y,obj_pointer.x,obj_pointer.y) > 2){
            if (0 <= sprite_direction and sprite_direction <= 10){
                sprite_index = spr_player_right; 
                image_speed = .5;
            } 
            else if (10 < sprite_direction and sprite_direction < 80){
                sprite_index = spr_player_upright;
                image_speed = .5;
            }
            else if (80 <= sprite_direction and sprite_direction <= 100){
                sprite_index = spr_player_up;
                image_speed = .5;
            }
            else if (100 < sprite_direction and sprite_direction < 170){
                sprite_index = spr_player_upleft;
                image_speed = .5;
            }
            else if (170 <= sprite_direction and sprite_direction <= 190){
                sprite_index = spr_player_left;
                image_speed = .5;
            }
            else if (190 < sprite_direction and sprite_direction < 260){
                sprite_index = spr_player_downleft;
                image_speed = .5;
            }
            else if (260 <= sprite_direction and sprite_direction <= 280){
                sprite_index = spr_player_down;
                image_speed = .5;
            }
            else if (280 < sprite_direction and sprite_direction < 349){
                sprite_index = spr_player_downright;
                image_speed = .5;
            }
            else if (350 <= sprite_direction and sprite_direction < 360){
                sprite_index = spr_player_right; 
                image_speed = .5;
            }
            sprite_i = sprite_index;
            }
            if (point_distance(x,y,obj_pointer.x,obj_pointer.y) < 1.5){ 
                image_speed = 0;
                sprite_index = sprite_i;
                image_index = 3;
            }
    }

}

