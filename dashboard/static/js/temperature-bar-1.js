var lineChartCanvas = document.getElementById('temperature')

var lineData = { labels: ['Data'], datasets: [{ data: [36, 64], borderWidth: 2, borderAlign: 'inner', borderWidth: 2, borderAlign: 'inner', backgroundColor: ['rgba(192, 0, 0, 0.4)','rgba(64, 64, 192, 0.4)',], borderColor: ['rgba(192, 0, 0, 1)', 'rgba(64, 64, 192, 1)',],}],}


var lineOptions = {}

var myLineChart = new Chart(lineChartCanvas, { type: 'line', data: lineData, options: lineOptions,})