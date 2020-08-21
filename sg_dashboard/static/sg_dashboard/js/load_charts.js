// All charts of the dashboard
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
            //open_socket();
        },
        error: function (error) {
            console.log(error);
        }
    });

    /**
     * Open Websocket with the Server
     * to recieve updates
     * and update dashboard accordingly 
     
    function open_socket() {

        // Server address
        var SERVER = 'localhost';

        // Server port
        var PORT = '8750';

        // Websocket connected to the server
        var ws = new WebSocket("ws://" + SERVER + ":" + PORT);

        // On message, perform updates on charts
        ws.onmessage = function (message) {
            // Parse recieved message to object
            var data = JSON.parse(message.data);
            console.log(data)
            // Update charts
            updateTemperature(data.temperature);
            updateHumidity(data.humidity);
            updateMoisture(data.moisture);
        };

        ws.onerror = function (error) {
            // on error message...
        }
    }
    */
})