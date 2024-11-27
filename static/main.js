turn = 0
grid_side = 600
width = window.innerWidth/2;
height = window.innerHeight/2;

hide("PVPpopup1");
hide("PVPpopup2");
hide("PVPpopupAI");
hide("ScoreboardPopup");
hide("HistoryPopup");
hide("EndPopup");



async function turn_change(event){
    turn = turn + 1
    xCoor = parseInt((event.clientX - ((width) - (grid_side/2))) / (grid_side/3)) +1;
    yCoor = parseInt((event.clientY - ((height) - (grid_side/2))) / (grid_side/3)) +1;
    grid_pos = "grid " + yCoor + "-" + xCoor
    console.log(grid_pos)
    modifyJsonFile("gridKey", "grid " + yCoor + " " + xCoor );
    data = await getJsonFile()
    setTimeout(() => {
        make_grid(event)
    }, 100);
    if(data["home_option"] == "2"){
        turn = turn + 1
            setTimeout(() => {  
            make_grid(event)
        }, 900)
    }
    data = await getJsonFile()
    console.log("AAAAAAAAAAAAAAAAAAAAAA")
    setTimeout(() => {
        if(data["game_state"] != "wait"){
            turn = 0
            show_end_popup()
        }
    }, 900);
}

async function make_grid(event){
    document.getElementById("grid").innerHTML = ' '
    xCoor = parseInt((event.clientX - ((width) - (grid_side/2))) / (grid_side/3)) +1;
    yCoor = parseInt((event.clientY - ((height) - (grid_side/2))) / (grid_side/3)) +1;
    data = await getJsonFile()
    for(i = 0;i < 3;i++){
        for(j = 0;j < 3;j++){
            console.log(data["grid"][(i*3)+j])
            if(data["grid"][(i*3)+j] == '0'){
                document.getElementById("grid").innerHTML+=
                    '<div style="top: '+ (i*33) +'%; left: '+ (j*33) +'%;" id="grid '+ (i+1) +'-'+ (j+1) +'" class="grid_draw" ></div>'
            } else if(data["grid"][(i*3)+j] == '1'){
                document.getElementById("grid").innerHTML+=
                '<div style="top: ' + (((i+1)*(100/3)) - (100/6)) + '%; left: ' + (((j+1)*(100/3)) - (100/6)) + '%; translate: -50% -50%" id="grid '+ (i+1) +'-'+ (j+1) +'" class="x" ></div>'

            } else{
                document.getElementById("grid").innerHTML+=
                '<div style="top: ' + (((i+1)*(100/3)) - (100/6)) + '%; left: ' + (((j+1)*(100/3)) - (100/6)) + '%; translate: -50% -50%" id="grid '+ (i+1) +'-'+ (j+1) +'" class="o" ></div>'

            }
        }
    }
}

function grid_hover_see(event){
    
    xCoor = parseInt((event.clientX - ((width) - (grid_side/2))) / (grid_side/3)) +1;
    yCoor = parseInt((event.clientY - ((height) - (grid_side/2))) / (grid_side/3)) +1;
    if(document.getElementById("grid " + yCoor + "-" + xCoor).classList.contains('grid_draw')){
        if(turn % 2 == 0){
            document.getElementById("grid_hover").innerHTML = 
            '<div style="top: ' + ((yCoor*(100/3)) - (100/6)) + '%; left: ' + ((xCoor*(100/3)) - (100/6)) + '%; translate: -50% -50%" class="xHover"></div>';
        } else {
            document.getElementById("grid_hover").innerHTML = 
            '<div style="top: ' + ((yCoor*(100/3)) - (100/6)) + '%; left: ' + ((xCoor*(100/3)) - (100/6)) + '%; translate:-50% -50%;" class="oHover"></div>';
        }
    }
}

function grid_hover_end(event){
    document.getElementById("grid_hover").innerHTML = "";
}

function set_params(event){
    grid_side = (window.innerHeight/10)*8;
    width = window.innerWidth/2;
    height = window.innerHeight/2;
    if((window.innerHeight/10)*8 > (window.innerWidth/10)*8){
        grid_side = (window.innerWidth/10)*8 ;
    }
    if(grid_side > 450){
        grid_side = 450;
    }
    var root = document.querySelector(':root');
    root.style.setProperty('--border-w', ((window.innerWidth/2) - ((grid_side*1.3)/2)) + "px");
    root.style.setProperty('--LD-w', ((window.innerWidth/2) - ((grid_side*1.6)/2)) + "px");

    root.style.setProperty('--square-side', grid_side + "px");
    
    make_grid(event);

}

async function hide(id) {
    document.getElementById(id).style.display = "none"
}

async function show(id) {
    document.getElementById(id).style.display = "block"
}

async function change(id1,id2) {
    hide(id1)
    show(id2)
}

// json -----------------------------------------------------------------------

        // Function to send data to Flask via Fetch API
function modifyJsonFile(key, value) {
    const newData = {
        key:  document.getElementById(key).value,
        value: document.getElementById(value).value
    };
    console.log(newData)
    console.log(key+" "+value)

            // Using fetch to send POST request to modify_json endpoint
    fetch('/modify_json', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newData) // Convert JS object to JSON string
    })
}

async function getJsonFile() {
            // Using fetch to send POST request to modify_json endpoint
    const response =  await fetch('/get_json_data', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }, 
    })
    console.log(response)
    const invoices = await response.json();
    console.log(invoices)
    return invoices
}


// Game functions -------------------------------------------------------------------------

function PVP(){
    show("PVPpopup1");
    hide("popup");
    modifyJsonFile("key", "P1vP2");
}
function PVAI(){
    show("PVPpopupAI");
    hide("popup");
    modifyJsonFile("key", "P1vAI");
}

async function Scoreboard(){
    document.getElementById("LBGames").innerHTML = ""
    setTimeout(async () => {
        data = await getJsonFile()
        for(i = 0; i < data["LBGames"].length;i++){
            document.getElementById("LBGames").innerHTML += 
            "<h3> " + (i+1) + ". " + data["LBGames"][i]["name"] 
            + " - Wins: " + data["LBGames"][i]["wins"] 
            + ", Losses: " + data["LBGames"][i]["losses"] 
            + ", Draws: " + data["LBGames"][i]["draws"] 
            + "</h3>"
        }
        show("ScoreboardPopup");
        hide("popup");
    }, 500);

    modifyJsonFile("key", "Scoreboard")
}

async function History(){
    document.getElementById("HGames").innerHTML = ""
    setTimeout(async () => {
        data = await getJsonFile()
        for(i = 0; i < data["HGames"].length;i++){
            if(data["HGames"][i]["draw"] == false){
                document.getElementById("HGames").innerHTML += 
                    "<h3> " + data["HGames"][i]["date"] 
                    + " - " + data["HGames"][i]["player1"] 
                    + " vs " + data["HGames"][i]["player2"] 
                    + ": " + data["HGames"][i]["winner"] 
                    + " won</h3>"
            } else{
                document.getElementById("HGames").innerHTML += 
                "<h3> " + data["HGames"][i]["date"] 
                + " - " + data["HGames"][i]["player1"] 
                + " vs " + data["HGames"][i]["player2"] 
                + ": Draw</h3>"
            }
        }
        show("HistoryPopup");
        hide("popup");
    }, 500);

    modifyJsonFile("key", "History")
}

async function show_end_popup(){
    data = await getJsonFile();
    document.getElementById("EndPopup").innerHTML = "<h2>"+ data["game_state"]+"</h2><button onclick='go_back_end()'>Go Back</button>"
    show("EndPopup");
}

function go_back_end(){
    hide("EndPopup");
    show("popup");
}

function search_history(){
    modifyJsonFile("keyH", "valueHsearch");
    player_name = document.getElementById("valueHsearch").value
    document.getElementById("HGames").innerHTML = ""
    setTimeout(async () => {
        data = await getJsonFile()
        for(i = 0; i < data["HGames"].length;i++){
            if(data["HGames"][i]["player1"] == player_name || data["HGames"][i]["player2"] == player_name){
                if(data["HGames"][i]["draw"] == false){
                    document.getElementById("HGames").innerHTML += 
                        "<h3> " + data["HGames"][i]["date"] 
                        + " - " + data["HGames"][i]["player1"] 
                        + " vs " + data["HGames"][i]["player2"] 
                        + ": " + data["HGames"][i]["winner"] 
                        + " won</h3>"
                } else{
                    document.getElementById("HGames").innerHTML += 
                        "<h3> " + data["HGames"][i]["date"] 
                        + " - " + data["HGames"][i]["player1"] 
                        + " vs " + data["HGames"][i]["player2"] 
                        + ": Draw</h3>"
                }
            }
        }
        show("HistoryPopup");
        hide("popup");
    }, 500);

}

function search_scoreboard(){
    modifyJsonFile("keySB", "valueSBsearch");
    player_name = document.getElementById("valueSBsearch").value
    document.getElementById("LBGames").innerHTML = ""

    setTimeout(async () => {
        data = await getJsonFile()
        for(i = 0; i < data["LBGames"].length;i++){
            if(data["LBGames"][i]["name"] == player_name){
            document.getElementById("LBGames").innerHTML += 
            "<h3> " + (i+1) + ". " + data["LBGames"][i]["name"] 
            + " - Wins: " + data["LBGames"][i]["wins"] 
            + ", Losses: " + data["LBGames"][i]["losses"] 
            + ", Draws: " + data["LBGames"][i]["draws"] 
            + "</h3>"
            }
        }
        show("ScoreboardPopup");
        hide("popup");
    }, 500);
}

function go_back_scoreboard(){
    hide("ScoreboardPopup");
    show("popup");
    modifyJsonFile("keySB", "valueSB");
}
function go_back_history(){
    hide("HistoryPopup");
    show("popup");
    modifyJsonFile("keyH", "valueH");
}

function set_playerAI(){
    hide("PVPpopupAI");
    modifyJsonFile("keyPAI", "valuePAI");
}

function set_player1(){
    show("PVPpopup2");
    hide("PVPpopup1");
    modifyJsonFile("keyP1", "valueP1");
}
function set_player2(){
    hide("PVPpopup2");
    modifyJsonFile("keyP2", "valueP2");
}

