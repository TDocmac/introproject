///proto_move(hspd, vspd)
var hspd = argument[0];
var vspd = argument[1];

//horizontal collision
if (proto_grid_place_meeting(x+hspd,y)) {
    while (!proto_grid_place_meeting(x+sign(hspd),y)){
        x+=sign(hspd);
    }
    hspd=0;
}

//move horizontally
x+=hspd

//vertical collision
if (proto_grid_place_meeting(x,y+vspd)) {
    while (!proto_grid_place_meeting(x,y+sign(vspd))){
        y+=sign(vspd);
    }
    vspd=0;
}


//move vertically
y+=vspd


