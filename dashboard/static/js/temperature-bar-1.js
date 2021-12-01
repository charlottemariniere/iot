var chartCanvas = document.getElementById('Temperature-Bar')
var barData = {
    labels: ['Temperature'],
    datasets: [{
        label:'Temperature',
        data:[33],
        borderWidth:1,
        backgroundColor: ['rgba(7, 59, 76, 0.5)'],
        borderColor: ['rgba(7, 59, 76, 1)'],
    }],
}

var barOptions = {scales:{},}

var myChart = new Chart(chartCanvas,{
    type: 'bar',
    data: barData,
    options: barOptions,
})

let t_xhr = new XMLHttpRequest()
t_xhr.open("GET", "http://127.0.0.1:5555/api/temperature")
t_xhr.responseType = "json"
t_xhr.send()
t_xhr.onload = function(){
    let responseObj = t_xhr.response
    for (let responseNumber in responseObj){
        let response = responseObj[responseNumber]
        console.log(barData)
        console.log(response)
        barData.datasets[0].data.push(response);
        myChart.update();}};