/**
 * Created by neoha on 17-04-2017.
 */
let jqery = require('jquery');
let util = require('util');

const {dialog} = require('electron').remote;

let bootloaderLable, partitionLable,applicationLable;

let outputPanel;

let currentflashSize, currentbaudRate, currentport, currentchip = 'ESP32';


let memoryESP8266 = ['detect','512KB','256KB','1MB','2MB','4MB','2MB-c1','4MB-c1','4MB-c2'];
let memoryESP32 = ['detect','1MB','2MB','4MB','8MB','16MB'];
let baudRate = ['921600','512000','256000','230400','115200'];
let theWindow;

let SerialPort= require('serial-node'), serial = new SerialPort();




jqery(document).ready(function () {

    bootloaderLable = document.getElementById("bootloaderLable");
    partitionLable = document.getElementById("partitionLable");
    applicationLable = document.getElementById("applicationLable");
    outputPanel = document.getElementById("outputPanel");
  let  flashSizeButton = document.getElementById("flashSizeButton");
  let  baudButton = document.getElementById("baudButton");
  let  portButton = document.getElementById("portButton");
    const {BrowserWindow} = require('electron').remote;
    theWindow = BrowserWindow.getFocusedWindow();

    for (let baud of baudRate)
    {
        jqery('.baudSelectList').append("<li><a class=\"baudSelect\" href=\"#\">"+baud+"</a></li>");
    }
    for (let memory of memoryESP32)
    {
        jqery('.flashSelectList').append("<li><a class=\"flashSelect\" href=\"#\">"+memory+"</a></li>");
    }


    jqery('.chipSelect').click(function (event) {
        event.preventDefault();
        let id = jqery(this).html();
        currentchip = id;
        if (currentchip==="ESP32")
        {
            jqery('.current-chip-div').html("");
            jqery('.current-chip-div').html("ESP32")
            jqery('.flashSelectList').html("");
            jqery('.flashSelectList').html("");
            jqery('#partitionButton').css("visibility", "visible");
            jqery('#applicationButton').css("visibility", "visible");
            jqery('#partitionLable').css("visibility", "visible");
            jqery('#applicationLable').css("visibility", "visible");
            jqery('#bootloaderLable').html("Bootloader");
            jqery('#bootloaderButton').html('Bootloader');
            for (let memory of memoryESP32)
            {
                jqery('.flashSelectList').append("<li><a class=\"flashSelect\" href=\"#\">"+memory+"</a></li>")
            }
        }
        else
        {
            jqery('.current-chip-div').html("");
            jqery('.current-chip-div').html("ESP8266")
            jqery('.flashSelectList').html("");
            jqery('#partitionButton').css("visibility", "hidden");
            jqery('#applicationButton').css("visibility", "hidden");
            jqery('#partitionLable').css("visibility", "hidden");
            jqery('#applicationLable').css("visibility", "hidden");
            jqery('#bootloaderLable').html("Application");
            jqery('#bootloaderButton').html('Application');
            for (let memory of memoryESP8266)
            {
                jqery('.flashSelectList').append("<li><a class=\"flashSelect\" href=\"#\">"+memory+"</a></li>")
            }
        }
        let d = document.querySelector('.mdl-layout');
        d.MaterialLayout.toggleDrawer();
        console.log(id)
    });

    jqery('.flashSelectList').on('click','.flashSelect',function () {
        currentflashSize= jqery(this).html();
        flashSizeButton.innerHTML = currentflashSize;
    });

    jqery('.baudSelectList').on('click','.baudSelect',function () {
        currentbaudRate= jqery(this).html();
        baudButton.innerHTML = currentbaudRate;
    });


    jqery('.portSelectList').on('click','.portSelect',function(){
        currentport = jqery(this).html();
        portButton.innerHTML = currentport;
    });



});

function eraseButtonClicked() {

    const spawn = require('child_process').exec;
    let cmd;
    if (currentchip==='ESP32')
    {
         cmd = util.format('%s\\esptool.exe --chip esp32 --port %s --baud %s erase_flash', process.cwd(),currentport,currentbaudRate );
            console.log(cmd)
    }
    else
    {
        cmd = util.format('%s\\esptool.exe --chip esp8266 --port %s --baud %s erase_flash', process.cwd(),currentport,currentbaudRate );
        console.log(cmd);

    }

    const ls = spawn(cmd);
    ls.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
        jqery('#outputPanel').append(data +"<br>")
    });

    ls.stderr.on('data', (data) => {
        console.log(`stderr: ${data}`);
        jqery('#outputPanel').append(data +"<br>")
    });

    ls.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        jqery('#outputPanel').append(data +"<br>")
    });
}
function flashButtonClicked() {
    const spawn = require('child_process').exec;
    let cmd;
    if (currentchip==='ESP32')
    {
        cmd = util.format('%s\\resources\\app\\esptool.exe --chip esp32 --port %s --baud %s --before default_reset --after hard_reset write_flash -z --flash_freq 80m --flash_mod dio --flash_size %s 0x1000 %s 0x8000 %s 0x10000 %s', process.cwd(), currentport,currentbaudRate,currentflashSize,bootloaderLable.innerHTML,partitionLable.innerHTML,applicationLable.innerHTML);
        console.log(cmd)
    }
    else
    {
        cmd = util.format('%s\\resources\\app\\esptool.exe --chip esp8266 --port %s --baud %s --before default_reset --after hard_reset write_flash --flash_size %s 0 %s', process.cwd(), currentport,currentbaudRate,currentflashSize,bootloaderLable.innerHTML);
        console.log(cmd);

    }

    const ls = spawn(cmd);
    ls.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
        jqery('#outputPanel').append(data +"<br>")
        var $cont = jqery('.mui-panel');
        $cont[0].scrollTop = $cont[0].scrollHeight;
    });

    ls.stderr.on('data', (data) => {
        console.log(`stderr: ${data}`);
        jqery('#outputPanel').append(data +"<br>")
    });

    ls.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        jqery('#outputPanel').append(data +"<br>")
    });
}

function bootloaderButtonClicked() {
    bootloaderLable.innerHTML = dialog.showOpenDialog({title:"Select Bootloader", properties: ['openFile'], filters:[{name: 'bootloader', extensions: ['bin']}] })[0]
}

function partitionButtonClicked() {
    partitionLable.innerHTML = dialog.showOpenDialog({title:"Select Partition", properties: ['openFile'],filters:[{name: 'partition', extensions: ['bin']}]})[0]
}

function applicationButtonClicked() {
    applicationLable.innerHTML = dialog.showOpenDialog({properties: ['openFile'],filters:[{name: 'application', extensions: ['bin']}],title:"Select Application"})[0]
}
function closeWindow() {
    theWindow.close()
}


function portButtonClicked() {
    try {
        listc = serial.list();
        jqery('.portSelectList').html("");
        for (i = 0; i < listc.length; i++) {
            console.log(listc[i]);
                console.log("<li><a class=\"portSelect\" href=\"#\">"+listc[i]+"</a></li>")
                jqery('.portSelectList').append("<li><a class=\"portSelect\" href=\"#\">"+listc[i]+"</a></li>")

        }
    }
    catch (err)
    {

    }

}