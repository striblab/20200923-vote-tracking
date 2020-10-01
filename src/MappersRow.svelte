<script>

import county_results_history from './scraper/json/county-results-history.json';
import IsoMap from './IsoMap.svelte'

export let county_data_2020;

</script>

<h3>Absentee ballot returns compared to 2018 general election</h3>
<div id="map-row">
  <div class="map-item">
    <h4>Trump 2016 counties</h4>
    <IsoMap {county_results_history} {county_data_2020} show_var='winner_2016' show_val='R'}/>
  </div>
  <div class="map-item">
    <h4>Clinton 2016 counties</h4>
    <IsoMap {county_results_history} {county_data_2020} show_var='winner_2016' show_val='D'}/>
  </div>
</div>
