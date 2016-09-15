/// Daño al enemigo - Experiencia

enemy_hp -= obj_player_stats.dmg_actual;

if (enemy_hp <= 0) instance_destroy();
