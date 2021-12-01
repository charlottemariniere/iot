var pieChartCanvas = document.getElementById('Device-Load-Pie')

var pieData = {
    labels: ['CPU Use', 'Idle'],
    datasets: [{
        data: [],
        borderWidth: 2,
        borderAlign: 'inner',
        backgroundColor: [
            'rgba(239, 71, 111, 0.5)','rgba(255, 209, 102, 0.5)',],
        borderColor: [
            'rgba(239, 71, 111, 1)','rgba(255, 209, 102, 1)',],}],};

var pieOptions = {}
var myPieChart = new Chart(pieChartCanvas, {
    type: 'pie',
    data: pieData,
    options: pieOptions,})

var updatePieData = function(){

}

let url = "http://127.0.0.1:5555/api/device-load"
let method = "GET"
let typeOfResponse = "json"
let xhr = new XMLHttpRequest()
xhr.open(method, url)
xhr.responseType = typeOfResponse
xhr.send()
xhr.onload = function(){
    let responseObj = xhr.response
    for (let responseNumber in responseObj){
        let response = responseObj[responseNumber]
        let load = response.load
        let idle = 100 - response.load
        pieData.datasets[0].data.push(load,idle);
        myPieChart.update();}};