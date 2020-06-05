// All charts of the dashboard
var charts = {};

$(function () {
    var params = window.location.pathname.split("/");
    var year = params["3"];
    var month = params["4"];
    // DATA url
    var endpoint = `http://localhost:8000/dashboard/api/${year}/${month}/`;
    console.log(endpoint);
    /**
     * Create charts on the dashboard
     */
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
            // Days labels
            var labels = new Array(data.Days.length)
                .fill(1)
                .map((_, i) => "Day ".concat(i + 1));
            min_temp_data = [];
            avg_temp_data = [];
            max_temp_data = [];
            pressure_data = [];
            humid_data = [];
            // Run through the data and collect : min, avg, max temp, pressure
            data.Days.map(function (record) {
                min_temp_data.push(record.min_temp);
                avg_temp_data.push(record.avg_temp);
                max_temp_data.push(record.max_temp);
                pressure_data.push(record.pressure);
                humid_data.push(record.rel_humid);
            });
            //  Temperature chart
            var tempdata = {
                min_data: min_temp_data,
                avg_data: avg_temp_data,
                max_data: max_temp_data,
                labels: labels,
            };
            charts.tempChart = createTempChart(tempdata);
            // Set min temp
            min_temp = data.Month[0].min_temp;
            $("#min_temp").html(min_temp + "<sup>°C</sup>");
            // Set avg temp
            avg_temp = data.Month[0].avg_temp;
            $("#avg_temp").html(avg_temp + "<sup>°C</sup>");
            // Set max temp
            max_temp = data.Month[0].max_temp;
            $("#max_temp").html(max_temp + "<sup>°C</sup>");

            // Humidity chart
            var humdata = {
                data: humid_data,
                labels: labels,
            };
            charts.humdChart = createHumdChart(humdata);

            // Pressure chart
            var pressuredata = {
                data: pressure_data,
                labels: labels,
            };
            charts.pressureChart = createPressureChart(pressuredata);

            /*// Crop yieds chart
            cropsdata = data.crops;
            charts.cropsChart = createCropsChart(cropsdata);

            // Soil moisture chart
            moisturedata = data.moisture;
            charts.moistureChart = createMoistureChart(moisturedata);

            // Start websocket (Dashboard <-> Server)
            open_socket();
            */
        },
        error: function (error) {
            console.log(error);
        },
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
});
