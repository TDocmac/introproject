obj_pointer.x = x;
obj_pointer.y = y;
sprite_direction = round(point_direction(x,y,mouse_x,mouse_y));
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

sprite_index = sprite_i;
bullet = instance_create(x,y,obj_bullet);
bullet.direction = point_direction(x,y,mouse_x,mouse_y);
bullet.speed = 10;

state = scr_player_movement_state;
