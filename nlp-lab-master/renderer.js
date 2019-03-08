const zerorpc = require("zerorpc")
let client = new zerorpc.Client({heartbeatInterval:100000})
client.connect("tcp://127.0.0.1:4242")

let holder = document.getElementById('holder')
let kwrds = document.getElementById('kwrds')
let drag = document.getElementById('drag')
let key = document.getElementById('key')
let score = document.getElementById('score')

var filepath
var avg_risk
var kwrds_list

document.addEventListener('drop', function (e) {
    e.preventDefault();
    e.stopPropagation();
    
    for (let f of e.dataTransfer.files) {
        filepath = f.path
	console.log('File(s) you dragged here: ', filepath)
        drag.textContent = 'Dropped file: ' + filepath
        drag.style.verticalAlign = "top"
        drag.style.lineHeight = "initial"
        
        client.invoke("ews", filepath, (error, res) => {
            if(error) {
                console.error(error)
            } else {
                avg_risk = res[0]
                kwrds_list = res[3]

                kwrds.style.textAlign = "left"
                kwrds.style.paddingLeft = "10px"
                kwrds.style.fontSize = "12px"
                kwrds.style.border = "1px solid #0d0d0d"
                kwrds.style.float = "left"
                kwrds.style.columnCount = "3"
                kwrds.style.columnGap = "10px"
                kwrds.style.display = "inline-block"
                kwrds.style.overflow = "hidden"

                score.innerText = "Score: " + avg_risk
                key.innerText = "List of key words:"

                kwrds.innerHTML = ""
                kwrds_list.forEach(function(entry) {
                    kwrds.innerHTML += "<li>" + entry + "</li>"
                })
            }
        })
    }
})

document.addEventListener('dragover', function (e) {
    e.preventDefault();
    e.stopPropagation();
})
