var barChartCanvas = document.getElementById('temperature')

var barData = { labels: ['Data'], datasets: [{ data: [5], borderWidth: 2, borderAlign: 'inner', backgroundColor: ['rgba(7, 59, 76, 0.5)',], borderColor: ['rgba(7, 59, 76, 1)',],}],}


var barOptions = {}

var myBarChart = new Chart(barChartCanvas, { type: 'bar', data: barData, options: barOptions,})