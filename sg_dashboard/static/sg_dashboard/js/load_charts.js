// All charts of the dashboard
var charts = {};

$(function () {

    //  Temperature chart
    charts.tempChart = createTempChart();

    // Humidity chart
    charts.humdChart = createHumdChart();

    // Soil moisture chart
    charts.moistureChart = createMoistureChart();


    var ws = null;
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
        ws = new WebSocket("ws://" + SERVER + ":" + PORT);

        ws.onopen = function (event) {
            console.log('----------------------------------\n');
            console.log(' Connection with server initiated \n');
            console.log('----------------------------------\n');
        }

        ws.onmessage = function (event) {
            if (event.data != "start!") {
                var data = JSON.parse(event.data)
                console.log(data);
                updateTemperature(data.temperature);
                updateHumidity(data.humidity);
                updateMoisture(data.moisture);
            }
            ws.send('next');
        }

        ws.onclose = function (event) {
            console.log('----------------------------------\n');
            console.log('Connection with server closed...!\n');
            console.log('----------------------------------\n');
        }
    }
    $('#start_streaming').click(open_socket);

    /**
     * 
     */
    function close_socket() {
        if (ws != null)
            ws.close();
    }
    $('#stop_streaming').click(close_socket);
});