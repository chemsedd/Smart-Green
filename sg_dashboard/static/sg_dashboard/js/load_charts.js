// All charts of the dashboard
var charts = {};

$(function () {

    //  Temperature chart
    charts.tempChart = createTempChart();

    // Humidity chart
    charts.humdChart = createHumdChart();

    // Soil moisture chart
    charts.moistureChart = createMoistureChart();

    // Start websocket (Dashboard <-> Server)
    open_socket();



    /**
     * 
     * @param {*} ms 
     */
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }


    /*
     * Open Websocket with the Server
     * to recieve updates
     * and update dashboard accordingly 
     * */
    function open_socket() {

        // Server address
        var SERVER = 'localhost';

        // Server port
        var PORT = '8000';

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
});