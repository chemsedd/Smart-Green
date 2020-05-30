/**
 * Create Temperature chart
 */
function createTempChart(data) {

    var tempCanvas = document.getElementById('tempCanvas').getContext('2d');

    return new Chart(tempCanvas, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: data.datalabel,
                data: data.data[1],
                backgroundColor: 'rgba(255, 215, 70, 0.7)',
                borderWidth: 3,
            }]
        },
        options: {
            scales: {
                yAxes: {
                    ticks: {
                        min: 0,
                        max: 70,
                    },
                }
            }
        }
    });
}


/**
 * Update Temperature chart
 */
function updateTemperature(value) {
    charts.tempChart.data.labels.push("Test");
    console.log(charts.tempChart.data.datasets[0].data.push(value));
    charts.tempChart.update();
}