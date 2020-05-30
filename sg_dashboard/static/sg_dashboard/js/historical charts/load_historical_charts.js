var charts = {};

$(function () {
    // DATA url
    var endpoint = 'data';

    /**
     * Create charts on the dashboard
     */
    $.ajax({
        method: 'GET',
        url: endpoint,
        success: function (data) {
            //  Temperature chart
            tempdata = data.temperature;
            charts.tempChart = createTempChart(tempdata);

            // Humidity chart
            humdata = data.humidity;
            charts.humdChart = createHumdChart(humdata);

            // Crop yieds chart
            cropsdata = data.crops;
            charts.cropsChart = createCropsChart(cropsdata);

            // Soil moisture chart
            moisturedata = data.moisture;
            charts.moistureChart = createMoistureChart(moisturedata);

            // Start websocket (Dashboard <-> Server)
            open_socket();
        },
        error: function (error) {
            console.log(error);
        }
    });
})