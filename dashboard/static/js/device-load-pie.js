var pieChartCanvas = document.getElementById('device-load')

var pieData = {
    labels: ['CPU Use', 'Idle'],
    datasets: [{ data: [36, 64], borderWidth: 2, borderAlign: 'inner', borderWidth: 2, borderAlign: 'inner', backgroundColor: ['rgba(239, 71, 111, 0.5)','rgba(255, 209, 102, 0.5)',], borderColor: ['rgba(239, 71, 111, 1)','rgba(255, 209, 102, 1)',],}],}


var pieOptions = {}

var myPieChart = new Chart(pieChartCanvas, { type: 'pie', data: pieData, options: pieOptions,})