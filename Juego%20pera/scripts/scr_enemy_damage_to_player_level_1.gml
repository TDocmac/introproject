/// Daño al player POR CONTACTO
var dano = argument[0];

obj_player_stats.hp_actual -= dano;

if (obj_player_stats.hp_actual <= 0) {
    obj_player_stats.hp_actual = 0;
    with (obj_player) {
        instance_destroy();
    }
}
