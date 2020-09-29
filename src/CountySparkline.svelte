<script>
	import * as d3 from 'd3';
  import { onMount } from 'svelte';

  import moment from 'moment-timezone';

	export let name;
	export let data_2020;
	export let data_2018;
	export let x_axis_labels;
	console.log(data_2018);

	let width = 150;
	let height = 50;
	let id = `county-sparkline-${name.replace(/ /g, '-').replace(/\./g, '')}`;
	let margin = ({top: 5, right: 0, bottom: 5, left: 5})

	let x = d3.scaleTime().range([margin.left, width - margin.right]);
  x.domain(d3.extent(x_axis_labels, function(d) { return d.date; }));

	// Use a separate y_max for each county to show trends, based on whichever is currently bigger -- 2020 or 2018 max
	const max_2020 = Math.max.apply(Math, data_2020.map(c => c.ballots_accepted));
	const max_2018 = Math.max.apply(Math, data_2018.map(c => c.ballots_accepted));
	const y_max = max_2020 > max_2018 ? max_2020 : max_2018;

  let y = d3.scaleLinear()
    .domain([0, y_max])
    .range([height - margin.bottom, margin.top])

	let line_2020 = d3.line()
    .defined(d => !isNaN(d.ballots_accepted))
    .x(d => x(new Date(moment(d.date).tz('America/Chicago'))))
    .y(d => y(d.ballots_accepted))

  let line_2018 = d3.line()
    .defined(d => !isNaN(d.ballots_accepted))
    .x(d => x(new Date(moment(d.date_2020).tz('America/Chicago'))))
    .y(d => y(d.ballots_accepted))

	const buildChart = function() {
    var svg = d3.select(`#${id}`)

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
        .attr('r', 2)

    // 2020
    svg.append("path")
      .datum(data_2020)
      .attr('class', 'accepted accepted-2020')
      .attr("d", line_2020)

    svg.append("g")
      .selectAll('circle')
      .data(data_2020)
      .join("circle")
        .attr('class', 'accepted circle-2020')
        .attr('cx', d => x(new Date(moment(d.date).tz('America/Chicago'))))
        .attr('cy', d => y(d.ballots_accepted))
        .attr('r', 2)
  }

	onMount(() => {
    buildChart()
  });
</script>

<svg class="sparkline" viewbox="0 0 {width} {height}" id={id} style="width: 100%;" ></svg>
