<script>
  import { geoAlbers, geoPath, geoMercator, geoCentroid } from "d3-geo";
  import { feature } from 'topojson';
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  import {intcomma} from 'journalize';
  import mn from './scraper/json/mn.json';

  // export let mn;IsoMap
  let aspect_ratio = 1.3;
  export let width = 400;
  export let height = width * aspect_ratio;
  // export let counties_latest = [];
  export let window_width;

  export let show_var;  // Which var to check
  export let show_val;  // What that var should equal
  export let county_results_history;

  let show_counties = county_results_history.filter(c => c[show_var] == show_val).map(c => c.county.toLowerCase());
  console.log(show_counties);

  $: {
    resp_width = window_width;
    // console.log(county_centroids)
  }

  let resp_width;
  // let max_cases = 0;
  // let max_cases_1k = 0;
  // let max_deaths = 0;
  // let max_deaths_1k = 0

  let tooltipResults;
  let tooltipHeight;
  let tooltipWidth;

  // if (counties_latest.length > 0) {
  //   max_cases = Math.max.apply(Math, counties_latest.map(function(o) { return o.total_positive_tests; }))
  //   max_cases_1k = Math.max.apply(Math, counties_latest.map(function(o) { return o.cases_per_1k; }))
  //   max_deaths = Math.max.apply(Math, counties_latest.map(function(o) { return o.total_deaths; }))
  //   max_deaths_1k = Math.max.apply(Math, counties_latest.map(function(o) { return o.deaths_per_1k; }))
  // }

  // console.log(counties_latest)

  let updateMap = function (which_var, which_max) {

    var svg = d3.select('svg.mnSVG')

    // let rScale = d3.scaleSqrt()
    //   .domain([0, which_max])
    //   .range([0, 30]);
    //
    // if (which_var == "cases") {
    //   svg.selectAll("circle.caseCircle.casesRaw")
    // 		.transition()
    // 		.duration(500)
    //     .attr('fill', '#528e9f')
    // 		.attr('r', d => rScale(d.positive_tests));
    // }
    // else if (which_var == "deaths") {
    //   svg.selectAll("circle.caseCircle.casesRaw")
    // 		.transition()
    // 		.duration(500)
    //     .attr('fill', '#969696')
    // 		.attr('r', d => rScale(d.deaths));
    // }
    // else if (which_var == "cases_per_1k") {
    //   svg.selectAll("circle.caseCircle.casesRaw")
    // 		.transition()
    // 		.duration(500)
    //     .attr('fill', '#528e9f')
    // 		.attr('r', d => rScale(d.cases_1k));
    // }
    // else if (which_var == "deaths_per_1k") {
    //   svg.selectAll("circle.caseCircle.casesRaw")
    // 		.transition()
    // 		.duration(500)
    //     .attr('fill', '#969696')
    // 		.attr('r', d => rScale(d.deaths_1k));
    // }

    // map_view = which_var;
	}

  let buildChart = function() {
    var svg = d3.select('svg.mnSVG')

    // svg.append("g")
    //   .selectAll('circle')
    //   .data(county_centroids)
    //   .join("circle")
    //     .attr('class', 'hoverCircle casesRaw')
    //     .attr('cx', (d, i) => d.centroid[0])
    //     .attr('cy', (d, i) => d.centroid[1])
    //     .attr('r', 5)
    //     .attr('fill', '#f0f0f0')
    //     .on('mouseover', buildTooltip)
    //     .on('mousemove', positionTooltip)
    //     .on('mouseout', hideTooltip);
    //
    // svg.append("g")
    //   .selectAll('circle')
    //   .data(county_centroids)
    //   .join("circle")
    //     .attr('class', 'caseCircle casesRaw')
    //     .attr('cx', (d, i) => d.centroid[0])
    //     .attr('cy', (d, i) => d.centroid[1])
    //     .attr('r', (d, i) => rScale(d.positive_tests))
    //     .attr('county_name', d => d.name.replace(/\s/g,'').replace(/\./g,' ').replace(/ /g,"_").toUpperCase())
    //     .attr('fill', '#528e9f')
    //     .on('mouseover', buildTooltip)
    //     .on('mousemove', positionTooltip)
    //     .on('mouseout', hideTooltip);
  }

  // function mapCases() { updateMap('cases', max_cases); }
  // function mapDeaths() { updateMap('deaths', max_cases); }
  // function mapCases1k() { updateMap('cases_per_1k', max_cases_1k); }
  // function mapDeaths1k() { updateMap('deaths_per_1k', max_cases_1k); }

  let county_centroids;

  const land = feature(mn, mn.objects.counties).features;

  const projection = d3.geoConicConformal()
    .parallels([45 + 37 / 60, 47 + 3 / 60])
    .rotate([94 + 15 / 60, 0])
    .fitSize([width, height], {type: "FeatureCollection", features: land});

  let path = d3.geoPath().projection(projection);

  // const rScale = d3.scaleSqrt()
  //         .domain([0, max_cases])
  //         .range([0, 25]);

  $: {
    // if (counties_latest.length > 0) {
    //   county_centroids = land.map(function (feature) {
    //     var record = counties_latest.find(element => element.county_fips == feature.properties.GEOID);
    //     return {
    //       'positive_tests': record.total_positive_tests,
    //       'deaths': record.total_deaths,
    //       'cases_1k': record.cases_per_1k,
    //       'deaths_1k': record.deaths_per_1k,
    //       'centroid': path.centroid(feature),
    //       'fips': feature.properties.GEOID,
    //       'name': record.county_name
    //     };
    //   });
    // } else {
    //   county_centroids = [];
    // }
  }

//   function buildTooltip() {
//     tooltipResults = d3.select(this).data()
//
//     let tooltip =  d3.select('#mnTooltip')
//
//     let string_selector = '[county_name=' + tooltipResults[0].name.replace(/\s/g,'').replace(/\./g,' ').replace(/ /g,"_").toUpperCase() + ']'
//
//     if (tooltip.classed('tooltip-active')) {
//       tooltip.classed('tooltip-active', false);
//     }
//     else {
//       tooltip.classed('tooltip-active', true);
//     }
//
//     if (map_view == "cases" || map_view == "cases_per_1k") {
//       d3.select(string_selector)
//         .attr('stroke', '#004a6d')
//         .attr('stroke-width', '1.5')
//     }
//     else {
//       d3.select(string_selector)
//         .attr('stroke', '	#808080')
//         .attr('stroke-width', '1.5')
//     }
//
//
//   }
//
//   function hideTooltip() {
//
//     if (counties_latest) {
//       let tooltip = document.querySelector('#mnTooltip')
//       if (tooltip.classList.contains('tooltip-active')) {
//         tooltip.classList.remove('tooltip-active');
//       }
//
//       let string_selector = '[county_name=' + tooltipResults[0].name.replace(/\s/g,'').replace(/\./g,' ').replace(/ /g,"_").toUpperCase() + ']'
//
//       d3.select(string_selector)
//         .attr('stroke', 'none')
//         .attr('stroke-width', 'none')
//     }
//   }
//
//   function positionTooltip() {
//   if (counties_latest) {
//     // console.log("position")
//     let tooltip = d3.select('#mnTooltip')
//     let svg = document.querySelector('.mnSVG')
//     let bounding = svg.getBoundingClientRect()
//
//
//     var x = event.layerX ==  event.offsetX ? event.offsetX : event.layerX;
//     var y = event.layerY ==  event.offsetY ? event.offsetY : event.layerY;
//
//     // calculates where cursor is on x axis relative to the size of the canvas
//     let cursorX = event.clientX - bounding.left;
//
//     tooltipHeight = tooltip.node().clientHeight;
//     tooltipWidth = tooltip.node().clientWidth;
//
//     let tooltipOffset = 25;
//     let cursorOffPage = event.clientY + (tooltipHeight + tooltipOffset) >= window.innerHeight;
//
//     if (!cursorOffPage) {
//       if (cursorX > bounding.width / 2) {
//         tooltip
//           .style('left', x - (tooltipWidth) + 'px')
//           .style('top', y + tooltipOffset + 'px');
//       }
//       else if (cursorX < bounding.width / 2) {
//         tooltip
//           .style('left', x + 0 + 'px')
//           .style('top', y + tooltipOffset + 'px');
//       }
//     }
//     else {
//       if (cursorX > bounding.width / 2) {
//         tooltip
//           .style('left', x - (tooltipWidth) + 'px')
//           .style('top', y - (tooltipHeight + tooltipOffset) + 'px');
//       }
//       else if (cursorX < bounding.width / 2) {
//         tooltip
//           .style('left', x + 0 + 'px')
//           .style('top', y - (tooltipHeight + tooltipOffset) + 'px');
//       }
//     }
//   }
// }


onMount(() => {
  buildChart();
});

</script>

<div class="iso-map">
  <svg viewbox="0 0 {width} {height}" style="width: 100%; height: 100%;" class="mnSVG">
    <g class="counties">
      {#each land as feature}
        {feature.properties.NAME}
        <path d={path(feature)} class="area-feature" class:highlight-feature="{show_counties.indexOf(feature.properties.NAME.toLowerCase()) != -1}"/>
      {/each}
    </g>
  </svg>
</div>
