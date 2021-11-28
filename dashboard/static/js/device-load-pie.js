var pieChartCanvas = document.getElementById('device-load')

var pieData = {
    labels: ['CPU Use', 'Idle'],
    datasets: [{ data: [36, 64], borderWidth: 2, borderAlign: 'inner', borderWidth: 2, borderAlign: 'inner', backgroundColor: ['rgba(192, 0, 0, 0.4)','rgba(64, 64, 192, 0.4)',], borderColor: ['rgba(192, 0, 0, 1)', 'rgba(64, 64, 192, 1)',],}],}


var pieOptions = {}

var myPieChart = new Chart(pieChartCanvas, { type: 'pie', data: pieData, options: pieOptions,})