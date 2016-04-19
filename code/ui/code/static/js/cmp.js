/**
 * Created by taohao on 2016/4/17.
 */

var HOST = '/proxy/api/machines/';

$(document).ready(function() {

    //var ip_list = get_ip_list();


    var ip_list = ['172.17.0.2', '172.17.0.3', '172.17.0.4'];
    for(var i=0; i<ip_list.length; i++){
        $("#ip-select").append("<option value=" + ip_list[i] +">" + ip_list[i] + "</option>")
    }

    $(".chosen-select").chosen();
    $('#cpu-search').click(function(){
        var _start = timestr_to_timestamp($("#cpu-from").val());
        var _end = timestr_to_timestamp($("#cpu-to").val());
        if(_start >= _end){
            alert("结束时间要大于开始时间")
        }else {
            var category_name = $("#cpu-category-select").val();
            get_info('cpus', _start, _end, category_name, '#cpu-container');
        }
    });
    $('#load-search').click(function(){
        var _start = timestr_to_timestamp($('#load-from').val());
        var _end = timestr_to_timestamp($("#load-to").val());
        if(_start >= _end){
            alert("结束时间要大于开始时间")
        }else {
            var category_name = $("#load-category-select").val();
            get_info('loads', _start, _end, category_name, '#load-container');
        }
    });
    $('#memory-search').click(function(){
        var _start = timestr_to_timestamp($('#mem-from').val());
        var _end = timestr_to_timestamp($("#mem-to").val());
        if(_start >= _end){
            alert("结束时间要大于开始时间")
        }else {
            var category_name = $('#memory-category-select').val();
            get_info('mems', _start, _end, category_name, '#memory-container');
        }
    });
    $(".btn-time").click(function(){
        var data_type = $(this).attr("btn-type");
        var _time = $(this).attr("timerange");
        var _now = parseInt(new Date().getTime() / 1000);
        var _start = get_start_timestamp(_time, _now);
        if (data_type == "cpus"){
            var cpu_category_name = $("#cpu-category-select").val();
            get_info(data_type, _start, _now, cpu_category_name, '#cpu-container');
        }else if(data_type == "loads"){
            var load_category_name = $("#load-category-select").val();
            get_info(data_type, _start, _now, load_category_name, '#load-container');

        }else if(data_type == "mems"){
            var mem_category_name = $("#memory-category-select").val();
            get_info(data_type, _start, _now, mem_category_name, '#memory-container');
        }

    });

    $('.form_datetime').datetimepicker({
        clearBtn: true,
        autoclose: true,
        todayHighlight: true,
        toggleActive: true,
        format: 'yyyy-mm-dd hh:ii:ss'
    });

});


function get_info(data_category, _start, _end, category_name, container_id){
    var ips = $("#ip-select").val();
    if(!ips){
        alert("选择ip")
    }
    else {
        var url = HOST + data_category;
        var params = {
            endpoints: ips,
            _start: _start,
            _end: _end,
            category: category_name
        };
        $.ajax({
            type: "GET",
            url: url,
            dataType: "json",
            data: params,
            success: function (data) {
                //console.log(data.categories);
                show_line_chart(container_id, data);
            },
            error: function () {
                alert('error')
            }
        })
    }
}


