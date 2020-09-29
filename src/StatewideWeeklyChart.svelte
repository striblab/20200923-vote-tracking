<script>
  import * as d3 from 'd3';
  import { onMount } from 'svelte';
  // import { watchResize } from "svelte-watch-resize";
  import {intcomma} from 'journalize';
  import moment from 'moment-timezone';

  export let data;
  export let data_2018;
  export let id;
  export let window_width;

  $: {
    resp_width = window_width;
  }

  // console.log(data)
  let resp_width
  let width = 600
  let height = 400
  let margin = ({top: 30, right: 23, bottom: 30, left: 60})

  let svg_width

  let selector = '#' + id
  // let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  let x_values = []
  const x_axis_labels = [
    {'date': new Date(moment('2020-09-25').tz('America/Chicago')), 'weeks_away': 6, 'label': '6 weeks away'},
    {'date': new Date(moment('2020-10-02').tz('America/Chicago')), 'weeks_away': 5, 'label': '5 weeks away'},
    {'date': new Date(moment('2020-10-09').tz('America/Chicago')), 'weeks_away': 4, 'label': '4 weeks away'},
    {'date': new Date(moment('2020-10-16').tz('America/Chicago')), 'weeks_away': 3, 'label': '3 weeks away'},
    {'date': new Date(moment('2020-10-23').tz('America/Chicago')), 'weeks_away': 2, 'label': '2 weeks away'},
    {'date': new Date(moment('2020-10-30').tz('America/Chicago')), 'weeks_away': 1, 'label': '1 week away'},
    {'date': new Date(moment('2020-11-02').tz('America/Chicago')), 'weeks_away': 0, 'label': ''},
    {'date': new Date(moment('2020-11-03').tz('America/Chicago')), 'weeks_away': 'election_day', 'label': 'Election Day'},
    {'date': new Date(moment('2020-11-06').tz('America/Chicago')), 'weeks_away': '', 'label': ''}
  ]

  const set_2020_dates = function (year_data) {
    year_data.forEach(element => element.date_2020 = x_axis_labels.find(label => label.weeks_away == element.weeks_away).date);
  }

  set_2020_dates(data_2018);

  let chart_type = "new";

  let formatWeek = d3.timeFormat("%e");
  let formatMonth = d3.timeFormat("%b");
  let formatMillisecond = d3.timeFormat(".%L")
  let formatDay = d3.timeFormat("%A")

  let formatDate = d3.timeFormat("%b %e");

  let tooltipResults;
  let x0;
  let y0;
  let i;
  let line_view;
  let tooltipWidth;
  let tooltipHeight;
  // x_axis_labels.forEach(element => console.log(element.date, element.date.getTime()));

  function processWeeksAway(input) {
    // console.log(input, input.getTime())
    // // x_values.push(input.label);'
    var matching_date = x_axis_labels.filter(n => n.date.getTime() == input.getTime());
    if (matching_date.length > 0) {
      return matching_date[0].label
    } else {
      return ''
    }
  }



  let formatTooltipDate = d3.timeFormat("%b %e");

  let x = d3.scaleTime().range([margin.left, width - margin.right]);
  x.domain(d3.extent(x_axis_labels, function(d) { return d.date; }));


  let y = d3.scaleLinear()
    .domain([0, 800000])
    // .domain([0, d3.max(data, d => d.hosp_total_daily_change)])
    .range([height - margin.bottom, margin.top])


  let line_2020 = d3.line()
    .defined(d => !isNaN(d.ballots_accepted))
    .x(d => x(new Date(moment(d.date).tz('America/Chicago'))))
    .y(d => y(d.ballots_accepted))

  let line_2018 = d3.line()
    .defined(d => !isNaN(d.ballots_accepted))
    .x(d => x(new Date(moment(d.date_2020).tz('America/Chicago'))))
    .y(d => y(d.ballots_accepted))

  let format = d3.format(",")

  function formatTick(d) {
    let s = format(d)
    return this.parentNode.nextSibling ? `${s}` : `${s} ballots accepted`;
  }

  let xAxis = d3.axisBottom(x)
      .tickValues(x_axis_labels.map(d => d.date))
      .tickFormat(date => processWeeksAway(new Date(moment(date).tz('America/Chicago'))))
      .tickSizeOuter(0)
      .tickSizeInner(0)

  let yAxis = g => g
      // .attr("transform", `translate(0,0)`)
      .attr('class', 'yAxis')
      .call(
        d3.axisRight(y)
          .ticks(5)
          .tickFormat(formatTick)
          .tickSize(width - margin.right)
      )
      .call(g => g.selectAll(".tick text")
        .attr("x", 4)
        .attr("dy", -4))


  function buildChart() {
    var svg = d3.select(selector)

    let hospColor = "#5788b9"
    let icuColor = "#807dba"

    svg.append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .attr('class', 'xAxis')
      .call(xAxis)

    svg.selectAll(".xAxis .tick text").attr("y", 8);

    svg.append("g")
      .call(yAxis)
      .call(g => g.select(".domain").remove())
      .call(g => g.selectAll(".yAxis .tick:not(:first-of-type) line")
        .attr('stroke', '#a9a9a9')
        .attr("stroke-opacity", 0.5)
        .attr("stroke-width", 1))
      .call(g => g.selectAll(".tick text")
        .attr("x", 4)
        .attr("dy", -4))

    // 2018
    svg.append("path")
      .datum(data_2018)
      .attr('class', 'accepted accepted-2018')
      .attr("d", line_2018)

    svg.append("g")
      .selectAll('circle')
      .data(data_2018)
      .join("circle")
        .attr('class', 'accepted circle-2018')
        .attr('cx', d => x(new Date(moment(d.date_2020).tz('America/Chicago'))))
        .attr('cy', d => y(d.ballots_accepted))
        .attr('r', 3)

    // 2020
    svg.append("path")
      .datum(data)
      .attr('class', 'accepted accepted-2020')
      .attr("d", line_2020)

    svg.append("g")
      .selectAll('circle')
      .data(data)
      .join("circle")
        .attr('class', 'accepted circle-2020')
        .attr('cx', d => x(new Date(moment(d.date).tz('America/Chicago'))))
        .attr('cy', d => y(d.ballots_accepted))
        .attr('r', 3)

      add_year_total(svg, 'general_2016', 676722, '2016 total (general)');
      add_year_total(svg, 'general_2018', 638581, '2018 total (general)');
      add_year_total(svg, 'primary_2020', 543649, '2020 total (Aug. primary)');
  }

  function add_year_total(svg, selector, total_ballots_accepted, label) {

    svg.append("line")
      .attr('class', 'year-total ' + selector)
      .attr("x1", 0)
      .attr("y1", y(total_ballots_accepted))
      .attr("x2", width - margin.right)
      .attr("y2", y(total_ballots_accepted))

    svg.append('text')
      .attr('class', 'year-total-label ' + selector)
      .attr('x', (width / 2))
      .attr('y', y(total_ballots_accepted) - 5)
      .text(label)
  }

  onMount(() => {
    buildChart()
  });
</script>

<style>

</style>

<div>
  <h3>Absentee voting is on track to dwarf past elections</h3>
  <svg viewbox="0 0 {width} {height}" id={id} style="width: 100%; height: 100%;" ></svg>
</div>

<p class="footnote">This is a footnote</p>
