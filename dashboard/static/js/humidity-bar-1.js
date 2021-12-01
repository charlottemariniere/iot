var chartCanvas = document.getElementById('Humidity-Bar')
var barData = {
    labels: ['Humidity'],
    datasets: [{
        label:'Humidity',
        data: [],
        borderWidth:1,
        backgroundColor: ['rgba(6, 214, 160, 0.5)'],
        borderColor: ['rgba(6, 214, 160, 1)'],
    }],
}

var barOptions = {scales:{},}

var myChart = new Chart(chartCanvas,{
    type: 'bar',
    data: barData,
    options: barOptions,
})

let h_xhr = new XMLHttpRequest()
h_xhr.open("GET", "http://127.0.0.1:5555/api/humidity")
h_xhr.responseType = "json"
h_xhr.send()
h_xhr.onload = function(){
    let responseObj = h_xhr.response
    for (let responseNumber in responseObj){
        let response = responseObj[responseNumber]
        console.log(barData)
        console.log(response)
        barData.datasets[0].data.push(response);
        myChart.update();}};