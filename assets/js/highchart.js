$(function () {
  // Create the chart

  var options = {
    chart: {
      events: {
        drilldown: function (e) {
          if (!e.seriesOptions) {
            var chart = this;

            // Show the loading label
            chart.showLoading("Loading ...");

            setTimeout(function () {
              chart.hideLoading();
              chart.addSeriesAsDrilldown(e.point, series);
            }, 1000);
          }
        },
      },
      plotBorderWidth: 0,
    },

    title: {
      text: "卡路里",
    },
    //
    subtitle: {
      text: " ",
    },
    //
    xAxis: {
      categories: [
        "星期一",
        "星期二",
        "星期三",
        "星期四",
        "星期五",
        "星期六",
        "星期日",
      ],
    },
    //
    yAxis: {
      title: {
        margin: 10,
        text: "Activity",
      },
    },
    //
    legend: {
      enabled: true,
    },
    //
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: "pointer",
        dataLabels: {
          enabled: false,
        },
        showInLegend: true,
      },
    },
    series: [
      {
        name: "自己",
        colorByPoint: true,
        data: [
          { name: "星期一", y: 50 },
          { name: "星期二", y: 20 },
          { name: "星期三", y: 35 },
          { name: "星期四", y: 95 },
          { name: "星期五", y: 85 },
          { name: "星期六", y: 95 },
          { name: "星期日", y: 15 },
        ],
      },
      {
        name: "同學",
        colorByPoint: true,
        data: [
          { name: "星期一", y: 80 },
          { name: "星期二", y: 90 },
          { name: "星期三", y: 95 },
          { name: "星期四", y: 65 },
          { name: "星期五", y: 45 },
          { name: "星期六", y: 95 },
          { name: "星期日", y: 65 },
        ],
      },
    ],
    //
    drilldown: {
      series: [],
    },
  };

  // Column chart
  options.chart.renderTo = "container";
  options.chart.type = "column";
  var chart1 = new Highcharts.Chart(options);
  document.getElementById("column").addEventListener("click", chartfunc);
  document.getElementById("bar").addEventListener("click", chartfunc);
  document.getElementById("pie").addEventListener("click", chartfunc);
  document.getElementById("line").addEventListener("click", chartfunc);

  function chartfunc() {
    options.chart.renderTo = "container";
    options.chart.type = this.value;
    var chart1 = new Highcharts.Chart(options);
  }
  //   $("#change_chart_title").click(function () {
  //     var new_title = $("#chart_title").val();
  //     var chart = $("#container").highcharts();
  //     chart.setTitle({ text: new_title });

  //     alert("Chart title changed to " + new_title + " !");
  //   });
});
