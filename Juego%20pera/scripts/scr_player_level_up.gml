/// Level up

level_factor = 5;

// --------------------------------------------------------------

if (obj_player_stats.exp_actual == obj_player_stats.exp_needed){
    obj_player_stats.player_level += 1;
    obj_player_stats.int_points += 1;
    obj_player_stats.exp_actual = 0;
    obj_player_stats.hp_actual = obj_player_stats.hp_max;
    obj_player_stats.dmg_actual = round((obj_player_stats.dmg_base + 2*(obj_player_stats.int_points))*0.4);
    obj_player_stats.hp_actual = obj_player_stats.hp_base + 20*(obj_player_stats.vit_points) + 10*(obj_player_stats.player_level);
    obj_player_stats.hp_max = obj_player_stats.hp_actual;
    obj_player_stats.exp_needed = 0;
    if (obj_player_stats.player_level <= 10) level_factor = 5;
    else if (obj_player_stats.player_level <= 20) level_factor = 8;
    else if (20 < obj_player_stats.player_level <= 30) level_factor = 10;
    else if (30 < obj_player_stats.player_level <= 40) level_factor = 12;
    else if (40 < obj_player_stats.player_level <= 50) level_factor = 15;
    else if (obj_player_stats.player_level > 50) level_factor = 20;
    obj_player_stats.exp_needed = 10 + level_factor*(obj_player_stats.player_level-1);
}

if (obj_player_stats.exp_actual > obj_player_stats.exp_needed){
    obj_player_stats.player_level += 1;
    obj_player_stats.int_points += 1;
    obj_player_stats.exp_actual = obj_player_stats.exp_actual - obj_player_stats.exp_needed;
    obj_player_stats.hp_actual = obj_player_stats.hp_max;
    obj_player_stats.dmg_actual = round((obj_player_stats.dmg_base + 2*(obj_player_stats.int_points))*0.4);
    obj_player_stats.hp_actual = obj_player_stats.hp_base + 20*(obj_player_stats.vit_points) + 10*(obj_player_stats.player_level);
    obj_player_stats.hp_max = obj_player_stats.hp_actual;
    obj_player_stats.exp_needed = 0;
    if (obj_player_stats.player_level <= 10) level_factor = 5;
    else if (obj_player_stats.player_level <= 20) level_factor = 8;
    else if (20 < obj_player_stats.player_level <= 30) level_factor = 10;
    else if (30 < obj_player_stats.player_level <= 40) level_factor = 12;
    else if (40 < obj_player_stats.player_level <= 50) level_factor = 15;
    else if (obj_player_stats.player_level > 50) level_factor = 20;
    obj_player_stats.exp_needed = 10 + level_factor*(obj_player_stats.player_level-1);
}


