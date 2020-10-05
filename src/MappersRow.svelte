<script>

import county_results_history from './scraper/json/county-results-history.json';
import IsoMap from './IsoMap.svelte'

export let county_data_2020;
export let current_week;

</script>


<div id="map-row">
  <div class="map-group">
    <h3>Absentee ballots accepted so far</h3>
    <div class="map-subrow">
      <div class="map-item">
        <h4>Trump 2016 counties</h4>
        <IsoMap {county_results_history} {county_data_2020} show_var='winner_2016' show_val='R' map_type='accepted_count'}/>
      </div>
      <div class="map-item">
        <h4>Clinton 2016 counties</h4>
        <IsoMap {county_results_history} {county_data_2020} show_var='winner_2016' show_val='D' map_type='accepted_count'}/>
      </div>
    </div>
  </div>
  <div class="map-group">
    <h3>Ballots accepted compared to {current_week} week{#if current_week != 1}s{/if} to go in 2018</h3>
    <div class="map-subrow">
      <div class="map-item">
        <h4>Trump 2016 counties</h4>
        <IsoMap {county_results_history} {county_data_2020} show_var='winner_2016' show_val='R' map_type='pct_change'}/>
      </div>
      <div class="map-item">
        <h4>Clinton 2016 counties</h4>
        <IsoMap {county_results_history} {county_data_2020} show_var='winner_2016' show_val='D' map_type='pct_change'}/>
      </div>
    </div>
  </div>
</div>
