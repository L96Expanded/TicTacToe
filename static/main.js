// Initializes the turn variable and grid size
turn = 0 
grid_side = 600
width = window.innerWidth/2;
height = window.innerHeight/2;

// Function to handle the change of turn when a player interacts with the grid
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
async function turn_change(event){
    turn = turn + 1  
    xCoor = parseInt((event.clientX - ((width) - (grid_side/2))) / (grid_side/3)) + 1;  
    yCoor = parseInt((event.clientY - ((height) - (grid_side/2))) / (grid_side/3)) + 1;  
    grid_pos = "grid " + yCoor + "-" + xCoor;  
    modifyJsonFile("gridKey", "grid " + yCoor + " " + xCoor);  
    data = await getJsonFile() 
    setTimeout(() => {
        make_grid(event)  
    }, 100);


    if(data["home_option"] == "2"){
        turn = turn + 1
        setTimeout(async () => {  
            make_grid(event)  
        }, 1500)
    }
    
    
    setTimeout(async () => {
        data = await getJsonFile()
        if(data["game_state"] != "wait"){
            turn = 0
            show_end_popup()  
        }
    }, 200);
}


// Function to render the game grid
/// Time Complexity:
/// - Best Case: O(9). 
/// - Average Case: O(9). 
/// - Worst Case: O(9).
async function make_grid(event){
    document.getElementById("grid").innerHTML = ' '  
    xCoor = parseInt((event.clientX - ((width) - (grid_side/2))) / (grid_side/3)) + 1;  
    yCoor = parseInt((event.clientY - ((height) - (grid_side/2))) / (grid_side/3)) + 1;  
    data = await getJsonFile() 

    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++){
            if(data["grid"][(i*3) + j] == '0'){
                document.getElementById("grid").innerHTML +=
                    '<div style="top: '+ (i*33) +'%; left: '+ (j*33) +'%;" id="grid '+ (i+1) +'-'+ (j+1) +'" class="grid_draw" ></div>'
            } else if(data["grid"][(i*3) + j] == '1'){
                document.getElementById("grid").innerHTML +=
                    '<div style="top: ' + (((i+1)*(100/3)) - (100/6)) + '%; left: ' + (((j+1)*(100/3)) - (100/6)) + '%; translate: -50% -50%" id="grid '+ (i+1) +'-'+ (j+1) +'" class="x" ></div>'
            } else {
                document.getElementById("grid").innerHTML +=
                    '<div style="top: ' + (((i+1)*(100/3)) - (100/6)) + '%; left: ' + (((j+1)*(100/3)) - (100/6)) + '%; translate: -50% -50%" id="grid '+ (i+1) +'-'+ (j+1) +'" class="o" ></div>'
            }
        }
    }
}


// Function to show hover effects on the grid based on the current turn
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function grid_hover_see(event){
    xCoor = parseInt((event.clientX - ((width) - (grid_side/2))) / (grid_side/3)) + 1;  
    yCoor = parseInt((event.clientY - ((height) - (grid_side/2))) / (grid_side/3)) + 1; 
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


// Function to remove hover effect when mouse leaves the grid
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function grid_hover_end(event){
    document.getElementById("grid_hover").innerHTML = "";  
}


// Function to dynamically adjust grid size based on the window size
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function set_params(event){
    grid_side = (window.innerHeight / 10) * 8; 
    width = window.innerWidth / 2;
    height = window.innerHeight / 2;

    if((window.innerHeight / 10) * 8 > (window.innerWidth / 10) * 8){
        grid_side = (window.innerWidth / 10) * 8;
    }
    if(grid_side > 450){
        grid_side = 450;  
    }

    var root = document.querySelector(':root');
    root.style.setProperty('--border-w', ((window.innerWidth / 2) - ((grid_side * 1.3) / 2)) + "px");
    root.style.setProperty('--LD-w', ((window.innerWidth / 2) - ((grid_side * 1.6) / 2)) + "px");
    root.style.setProperty('--square-side', grid_side + "px");
    
    make_grid(event);  
}


// Function to hide an element by its ID
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
async function hide(id) {
    document.getElementById(id).style.display = "none" 
}


// Function to show an element by its ID
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
async function show(id) {
    document.getElementById(id).style.display = "block"  
}


// Function to switch visibility between two elements
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
async function change(id1, id2) {
    hide(id1);  
    show(id2);  
}


// Json functions ------------------------------------------------------------------


// Function to modify data in the JSON file via a POST request
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function modifyJsonFile(key, value) {
    const newData = {
        key: document.getElementById(key).value,
        value: document.getElementById(value).value
    };

    fetch('/modify_json', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newData) 
    });
}

// Function to fetch the current data from the JSON file via a GET request
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
async function getJsonFile(){
    const response =  await fetch('/get_json_data', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }, 
    })
    const invoices = await response.json();
    return invoices
}


// Game functions -------------------------------------------------------------------------


// PVP function: Displays a Player vs Player popup and hides another popup. Also modifies a JSON file.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function PVP(){
    
    show("PVPpopup1");
    hide("popup");
    modifyJsonFile("key", "P1vP2");
}


// PVAI function: Displays a Player vs AI popup and hides another popup. Also modifies a JSON file.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function PVAI(){
    
    show("PVPpopupAI");
    hide("popup");
    modifyJsonFile("key", "P1vAI");
}


// Leaderboard function: Fetches leaderboard data asynchronously, displays it, and modifies JSON.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(n). 
/// - Worst Case: O(n).
async function Leaderboard(){

    document.getElementById("LBGames").innerHTML = ""
    setTimeout(async () => {
        data = await getJsonFile();  
        for(i = 0; i < data["LBGames"].length; i++){ 
            document.getElementById("LBGames").innerHTML += 
            "<h3> " + (i+1) + ". " + data["LBGames"][i]["name"] 
            + " - Wins: " + data["LBGames"][i]["wins"] 
            + ", Losses: " + data["LBGames"][i]["losses"] 
            + ", Draws: " + data["LBGames"][i]["draws"] 
            + "</h3>";
        }
        show("LeaderboardPopup");
        hide("popup");
    }, 400);
    modifyJsonFile("key", "Leaderboard");
}


// History function: Fetches historical game data asynchronously and displays it. Modifies JSON.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(n). 
/// - Worst Case: O(n).
async function History(){

    document.getElementById("HGames").innerHTML = ""
    setTimeout(async () => {
        data = await getJsonFile(); 
        for(i = 0; i < data["HGames"].length; i++){ 
            if(data["HGames"][i]["draw"] == false){
                document.getElementById("HGames").innerHTML += 
                    "<h3> " + data["HGames"][i]["date"] 
                    + " - " + data["HGames"][i]["player1"] 
                    + " vs " + data["HGames"][i]["player2"] 
                    + ": " + data["HGames"][i]["winner"] 
                    + " won</h3>";
            } else {
                document.getElementById("HGames").innerHTML += 
                "<h3> " + data["HGames"][i]["date"] 
                + " - " + data["HGames"][i]["player1"] 
                + " vs " + data["HGames"][i]["player2"] 
                + ": Draw</h3>";
            }
        }
        show("HistoryPopup");
        hide("popup");
    }, 500);
    modifyJsonFile("key", "History");
}


// show_end_popup function: Fetches the current game state asynchronously and displays it in a popup.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
async function show_end_popup(){

    data = await getJsonFile();  
    document.getElementById("EndPopup").innerHTML = "<h2>"+ data["game_state"]+"</h2><button onclick='go_back_end()'>Go Back</button>";
    show("EndPopup");
}


// go_back_end function: Hides the "EndPopup" and shows the main popup.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function go_back_end(){
    hide("EndPopup");
    show("popup");
}


// search_history function: Searches for a player's history and displays relevant results.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(n). 
/// - Worst Case: O(n).
function search_history(){
    document.getElementById("HGames").innerHTML = "";
    setTimeout(async () => {
        modifyJsonFile("keyH", "valueHsearch");
    }, 200);
    setTimeout(async () => {
        
        data = await getJsonFile();  
            for(i = 0; i < data["SortedHGames"].length; i++){
                if(data["SortedHGames"][i]["draw"] == false){
                    document.getElementById("HGames").innerHTML += 
                        "<h3> " + data["SortedHGames"][i]["date"] 
                        + " - " + data["SortedHGames"][i]["player1"] 
                        + " vs " + data["SortedHGames"][i]["player2"] 
                        + ": " + data["SortedHGames"][i]["winner"] 
                        + " won</h3>";
                } else {
                    document.getElementById("HGames").innerHTML += 
                    "<h3> " + data["SortedHGames"][i]["date"] 
                    + " - " + data["SortedHGames"][i]["player1"] 
                    + " vs " + data["SortedHGames"][i]["player2"] 
                    + ": Draw</h3>";
                }
            }
        show("HistoryPopup");
        hide("popup");
    }, 600);
    modifyJsonFile("key", "History");
} 


// search_leaderboard function: Searches for a player's leaderboard and displays relevant results.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(n). 
/// - Worst Case: O(n).
function search_leaderboard(){
    document.getElementById("LBGames").innerHTML = "";
    setTimeout(async () => {
        modifyJsonFile("keyLB", "valueLBsearch");
    }, 200);
    setTimeout(async () => {
        
        data = await getJsonFile();  
            document.getElementById("LBGames").innerHTML = 
            "<h3> " + data["SortedLBGames"] + "</h3>";
        show("LeaderboardPopup");
        hide("popup");
    }, 400);
    modifyJsonFile("key", "Leaderboard");
}


// go_back_leaderboard function: Hides the "LeaderboardPopup" and shows the main popup.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function go_back_leaderboard(){
    hide("LeaderboardPopup");
    show("popup");
    modifyJsonFile("keyLB", "valueLB");
}


// go_back_history function: Hides the "HistoryPopup" and shows the main popup.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function go_back_history(){
    hide("HistoryPopup");
    show("popup");
    modifyJsonFile("keyH", "valueH");
}


// set_playerAI function: Sets the player's AI name and hides the AI popup.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function set_playerAI(){

    if(document.getElementById("valuePAI").value != ""){
        hide("PVPpopupAI");
        modifyJsonFile("keyPAI", "valuePAI");
    } else {
        alert("Please input a valid name.");
    }
}


// set_player1 function: Sets the player 1 name and shows the second player popup.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function set_player1(){
    if(document.getElementById("valueP1").value != ""){
        show("PVPpopup2");
        hide("PVPpopup1");
        modifyJsonFile("keyP1", "valueP1");
    } else {
        alert("Please input a valid name.");
    }
}


// set_player2 function: Sets the player 2 name and hides the second player popup.
/// Time Complexity:
/// - Best Case: O(1). 
/// - Average Case: O(1). 
/// - Worst Case: O(1).
function set_player2(){
    if(document.getElementById("valueP2").value != ""){
        hide("PVPpopup2");
        modifyJsonFile("keyP2", "valueP2");
    } else {
        alert("Please input a valid name.");
    }
}
