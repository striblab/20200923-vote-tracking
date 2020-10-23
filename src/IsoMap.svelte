<script>
  import { geoPath } from "d3-geo";
  import { feature } from 'topojson';
  import {ckmeans} from 'simple-statistics'
  import * as d3 from 'd3';
  import mn from './scraper/json/mn.json';

  let aspect_ratio = 1.3;
  export let width = 400;
  export let height = width * aspect_ratio;
  export let window_width;

  export let show_var;  // Which var to check
  export let show_val;  // What that var should equal
  export let map_type = 'pct_change';
  export let county_results_history;
  export let county_data_2020;

  let show_counties = county_results_history.filter(c => c[show_var] == show_val).map(c => c.county.toLowerCase());

  $: {
    resp_width = window_width;
  }

  let resp_width;

  let pct_extent = d3.extent(county_data_2020.filter(o => o.pct_to_date != 'N/A'), d => d.pct_to_date);
  let accepted_extent = d3.extent(county_data_2020, d => d.ballots_accepted_latest);
  console.log(accepted_extent);

  var pct_change_color = d3.scaleLinear()
    .domain([50, 100, 200, 300, 400, 500])
     .range(['#c7e5b5', '#9ee384', '#5bbf48', '#299e3d', '#118241', '#004C21']);

  // var raw_count_color = d3.scaleSequential()
  //   // .domain([-300, 0, 300])
  //   .domain([accepted_extent[0], accepted_extent[1]])
  //   .interpolator(d3.interpolateGreens);

  let means = ckmeans(county_data_2020.map(d => d.ballots_accepted_latest), 5);
  let ckmeans_stops = means.map(group => Math.max(...group));
  ckmeans_stops.unshift(1);
  console.log(ckmeans_stops);
  var raw_count_color = d3.scaleThreshold()
    .domain(ckmeans_stops)
    .range(['#D9D3EB', '#B6AED4', '#7D739C', '#62597D', '#4A4061']);

  function getFillColor(county_name) {
    var bool_show_county = show_counties.indexOf(county_name.toLowerCase()) != -1;
    if (bool_show_county) {
      if (map_type == 'pct_change') {
        var pct_to_date = county_data_2020.find(c => c.county_name.toLowerCase() == county_name.toLowerCase()).pct_to_date;
        console.log(pct_to_date);
        return pct_change_color(pct_to_date);
      } else {
        var ballots_accepted = county_data_2020.find(c => c.county_name.toLowerCase() == county_name.toLowerCase()).ballots_accepted_latest;
        return raw_count_color(ballots_accepted);
      }
    }
  }

  let county_centroids;

  const land = feature(mn, mn.objects.counties).features;

  const projection = d3.geoConicConformal()
    .parallels([45 + 37 / 60, 47 + 3 / 60])
    .rotate([94 + 15 / 60, 0])
    .fitSize([width, height], {type: "FeatureCollection", features: land});

  let path = d3.geoPath().projection(projection);

</script>

<div class="iso-map">
  <svg viewbox="0 0 {width} {height}" style="width: 100%; height: 100%;" class="mnSVG">
    <g class="counties">
      {#each land as feature}
        {feature.properties.NAME}
        <path d={path(feature)} class="area-feature" class:highlight-feature="{show_counties.indexOf(feature.properties.NAME.toLowerCase()) != -1}" style="fill: {getFillColor(feature.properties.NAME)}"/>
      {/each}
    </g>
  </svg>
</div>
