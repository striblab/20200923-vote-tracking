<script>
  import { geoPath } from "d3-geo";
  import { feature } from 'topojson';
  import * as d3 from 'd3';
  import mn from './scraper/json/mn.json';

  let aspect_ratio = 1.3;
  export let width = 400;
  export let height = width * aspect_ratio;
  export let window_width;

  export let show_var;  // Which var to check
  export let show_val;  // What that var should equal
  export let county_results_history;
  export let county_data_2020;

  let show_counties = county_results_history.filter(c => c[show_var] == show_val).map(c => c.county.toLowerCase());

  $: {
    resp_width = window_width;
  }

  let resp_width;

  let min_change = Math.min.apply(
    Math, county_data_2020.filter(o => o.pct_to_date != 'N/A').map(function(o) { return o.pct_to_date; })
  );

  let max_change = Math.max.apply(
    Math, county_data_2020.filter(o => o.pct_to_date != 'N/A').map(function(o) { return o.pct_to_date; })
  );

  var color = d3.scaleLinear()
    .domain([min_change, 0, max_change])
    .range(['#4A4061', "white", '#3C8259']);

  function getFillColor(county_name) {
    var bool_show_county = show_counties.indexOf(county_name.toLowerCase()) != -1;
    if (bool_show_county) {
      var pct_to_date = county_data_2020.find(c => c.county_name.toLowerCase() == county_name.toLowerCase()).pct_to_date;
      return color(pct_to_date);
    }
  }

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
