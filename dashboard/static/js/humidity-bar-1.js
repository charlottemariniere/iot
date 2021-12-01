var barChartCanvas = document.getElementById('humidity')

var barData = { labels: ['Data'], datasets: [{ data: [64], borderWidth: 2, borderAlign: 'inner', backgroundColor: ['rgba(6, 214, 160, 0.5)',], borderColor: ['rgba(6, 214, 160, 1)',],}],}


var barOptions = {}

var myBarChart = new Chart(barChartCanvas, { type: 'bar', data: barData, options: barOptions,})