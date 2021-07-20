<template>
  <div id="main" style="width: 600px; height: 400px"></div>
</template>

<script>
import echarts from "echarts";

export default {
  name: "Plot",
  date() {
    return {
      time_axis: [],
      usage_data: [],
    };
  },
  methods: {
    myEcharts() {
      var myChart = echarts.init(document.getElementById("main"));
      var option = {
        xAxis: {
          type: "category",
          data: this.time_axis.map(function(d) {
            return (
              (d.getHours() < 10 ? "0" : "") +
              d.getHours() +
              ":" +
              (d.getMinutes() < 10 ? "0" : "") +
              d.getMinutes() +
              ":" +
              (d.getSeconds() < 10 ? "0" : "") +
              d.getSeconds()
            );
          }),
        },
        yAxis: {
          type: "value",
          min: "dataMin",
          scale: true,
        },
        series: [
          {
            data: this.usage_data.map(function(v) {
              return Math.round(v * 100) / 100;
            }),
            type: "line",
          },
        ],
        tooltip: {
          trigger: "axis",
          show: true,
          formatter: "{b}\t{c}",
        },
      };
      myChart.setOption(option);
    },
    refresh() {
      if (this.usage_data.length >= 10) {
        this.usage_data.shift();
        this.time_axis.shift();
      }
      let last = this.usage_data[this.usage_data.length - 1];
      this.usage_data.push(last + Math.random() * 0.1);
      this.time_axis.push(new Date());
      this.myEcharts();
    },
  },
  mounted() {
    this.time_axis = [new Date()];
    this.usage_data = [Math.random() * 0.1];
    this.myEcharts();
    window.setInterval(this.refresh, 2000);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
