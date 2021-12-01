var chartCanvas = document.getElementById('Pressure-Bar')
var barData = {
    labels: ['Pressure'],
    datasets: [{
        label:'Pressure',
        data:[10],
        borderWidth:1,
        backgroundColor: 'rgba(17, 138, 178, 0.5)',
        borderColor: 'rgba(17, 138, 178, 1)',
    }],
}

var barOptions = {scales:{},}

var myChart = new Chart(chartCanvas,{
    type: 'bar',
    data: barData,
    options: barOptions,
})

let p_xhr = new XMLHttpRequest()
p_xhr.open("GET", "http://127.0.0.1:5555/api/pressure")
p_xhr.responseType = "json"
p_xhr.send()
p_xhr.onload = function(){
    let responseObj = p_xhr.response
    for (let responseNumber in responseObj){
        let response = responseObj[responseNumber]
        console.log(barData)
        console.log(response)
        barData.datasets[0].data.push(response);
        myChart.update();}};