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
            open_socket();
        },
        error: function (error) {
            console.log(error);
        }
    });

    /*
     * Open Websocket with the Server
     * to recieve updates
     * and update dashboard accordingly 
     * */
    function open_socket() {

        // Server address
        var SERVER = 'localhost';

        // Server port
        var PORT = '5000';

        // Websocket connected to the server
        var ws = new WebSocket("ws://" + SERVER + ":" + PORT);

        ws.onopen = function (event) {
            console.log('----------------------------------\n');
            console.log(' Connection with server initiated \n');
            console.log('----------------------------------\n');
        }


        ws.onmessage = function (event) {
            var data = JSON.parse(event.data)
            console.log(data);
            updateTemperature(data.temperature);
            updateHumidity(data.humidity);
            updateMoisture(data.moisture);
        }

        ws.onclose = function (event) {
            console.log('----------------------------------\n');
            console.log('Connection with server closed...!\n');
            console.log('----------------------------------\n');
        }
    }
})