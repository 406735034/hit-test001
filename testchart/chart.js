$(function () {    


// Create the chart

var options = {
    chart: {
       events: {
            drilldown: function (e) {
                if (!e.seriesOptions) {

                    var chart = this;

                        

                    // Show the loading label
                    chart.showLoading('Loading ...');

                    setTimeout(function () {
                        chart.hideLoading();
                        chart.addSeriesAsDrilldown(e.point, series);
                    }, 1000); 
                }

            }
        },
        plotBorderWidth: 0
    },

    title: {
        text: 'Chart Title',
    },
    //
    subtitle: {
            text: 'Subtitle'
    },
    //
    xAxis: {
            type: 'category',
    },
    //
    yAxis: {

            title: {
                margin: 10,
                text: 'Activity'
            },      
    },
    //
    legend: {
        enabled: true,
    },
    //
    plotOptions: {
        series: {
            pointPadding: 0.2,
            borderWidth: 0,
            dataLabels: {
                enabled: true
            }
        },
        pie: {
            plotBorderWidth: 0,
            allowPointSelect: true,
            cursor: 'pointer',
            size: '100%',
            dataLabels: {
                enabled: true,
                format: '{point.name}: <b>{point.y}</b>'
            }
        }
    },
    //
     series: [{
        name: 'Case',
        colorByPoint: true,
        data: [80, 96, 65, 35, 41,98,33]
    }],
    //
    drilldown: {
        series: []
    }
};

// Column chart
options.chart.renderTo = 'container';
options.chart.type = 'column';
var chart1 = new Highcharts.Chart(options);

chartfunc = function()
{
var column = document.getElementById('column');
var bar = document.getElementById('bar');
var pie = document.getElementById('pie');
var line = document.getElementById('line');

        
if(column.checked)
    {
        
        options.chart.renderTo = 'container';
        options.chart.type = 'column';
        var chart1 = new Highcharts.Chart(options);
    }
else if(bar.checked)
    {
        options.chart.renderTo = 'container';
        options.chart.type = 'bar';
        var chart1 = new Highcharts.Chart(options);
    }
else if(pie.checked)
    {
        options.chart.renderTo = 'container';
        options.chart.type = 'pie';
        var chart1 = new Highcharts.Chart(options);
    }
else
    {
        options.chart.renderTo = 'container';
        options.chart.type = 'line';
        var chart1 = new Highcharts.Chart(options);
    }

}

$('#change_chart_title').click(function(){
    var new_title = $('#chart_title').val();
    var chart = $('#container').highcharts();
    chart.setTitle({ text: new_title });
        
    alert('Chart title changed to '+new_title+' !');
    
});
});

