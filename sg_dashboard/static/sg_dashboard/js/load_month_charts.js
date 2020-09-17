// All charts of the dashboard
var charts = {};
$(function () {
    var params = window.location.pathname.split("/");
    var year = params["3"];
    var month = params["4"];
    // DATA url
    var endpoint = `http://localhost:8000/dashboard/api/${year}/${month}/`;

    /**
     * Create charts on the dashboard (historical)
     */
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
            // Days labels
            var labels = new Array(data.Days.length)
                .fill(1)
                .map((_, i) => "Day ".concat(i + 1));
            var min_temp_data = [];
            var avg_temp_data = [];
            var max_temp_data = [];
            var pressure_data = [];
            var humid_data = [];
            var prec_data = [];

            // Run through the data and collect : min, avg, max temp, pressure
            data.Days.map(function (record) {
                min_temp_data.push(record.min_temp);
                avg_temp_data.push(record.avg_temp);
                max_temp_data.push(record.max_temp);
                pressure_data.push(record.pressure);
                humid_data.push(record.rel_humid);
                prec_data.push(record.prec);
            });


            //  Temperature chart
            var tempdata = {
                min_data: min_temp_data,
                avg_data: avg_temp_data,
                max_data: max_temp_data,
                labels: labels,
            };
            charts.tempChart = createTempChart(tempdata);
            // -------------------------------------------
            //                  Temp
            // -------------------------------------------
            // min
            min_temp = Number(data.Stats.min_temp.toFixed(2));
            $("#min_temp").html(min_temp + "<sup>°C</sup>");
            // avg 
            avg_temp = Number(data.Stats.avg_temp.toFixed(2));
            $("#avg_temp").html(avg_temp + "<sup>°C</sup>");
            // max 
            max_temp = Number(data.Stats.max_temp.toFixed(2));
            $("#max_temp").html(max_temp + "<sup>°C</sup>");

            // -------------------------------------------
            //                 precipitation 
            // -------------------------------------------
            // min
            min_prec = Number(data.Stats.min_prec.toFixed(2));
            $("#min_prec").html(min_prec + "<sup>%</sup>");
            // avg 
            avg_prec = Number(data.Stats.avg_prec.toFixed(2));
            $("#avg_prec").html(avg_prec + "<sup>%</sup>");
            // max 
            max_prec = Number(data.Stats.max_prec.toFixed(2));
            $("#max_prec").html(max_prec + "<sup>%</sup>");

            // -------------------------------------------
            //               Rel_humid
            // -------------------------------------------
            // min
            min_rel_humid = Number(data.Stats.min_rel_humid.toFixed(2));
            $("#min_rel_humid").html(min_rel_humid + "<sup>%</sup>");
            // avg 
            avg_rel_humid = Number(data.Stats.avg_rel_humid.toFixed(2));
            $("#avg_rel_humid").html(avg_rel_humid + "<sup>%</sup>");
            // max 
            max_rel_humid = Number(data.Stats.max_rel_humid.toFixed(2));
            $("#max_rel_humid").html(max_rel_humid + "<sup>%</sup>");

            // -------------------------------------------
            //               Pressure
            // -------------------------------------------
            // min
            min_pressure = Number(data.Stats.min_pressure.toFixed(2));
            $("#min_pressure").html(min_pressure + "<sup>%</sup>");
            // avg 
            avg_pressure = Number(data.Stats.avg_pressure.toFixed(2));
            $("#avg_pressure").html(avg_pressure + "<sup>%</sup>");
            // max 
            max_pressure = Number(data.Stats.max_pressure.toFixed(2));
            $("#max_pressure").html(max_pressure + "<sup>%</sup>");


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

            // Precipitation chart
            var precipitationdata = {
                data: prec_data,
                labels: labels,
            };
            charts.precipitationChart = createPrecipitationChart(precipitationdata);


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
            console.log("Error:", error);
        },
    });
});