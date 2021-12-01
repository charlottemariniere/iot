var barChartCanvas = document.getElementById('pressure')

var barData = { labels: ['Data'], datasets: [{ data: [123], borderWidth: 2, borderAlign: 'inner', backgroundColor: ['rgba(17, 138, 178, 0.5)',], borderColor: ['rgba(17, 138, 178, 1)',],}],}


var barOptions = {}

var myBarChart = new Chart(barChartCanvas, { type: 'bar', data: barData, options: barOptions,})