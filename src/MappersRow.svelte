<script>

import county_results_history from './scraper/json/county-results-history.json';
import IsoMap from './IsoMap.svelte'

export let county_data_2020;

</script>


<p class="buffer">&nbsp;</p>

<div id="map-row">
  <div class="map-group">
    <div class="chartTitle">Absentee ballots accepted so far</div>
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
    <div class="center">
      <div class="legend"><div class="null"></div><div class="purple1"></div><div class="purple2"></div><div class="purple3"></div><div class="purple4"></div><div class="purple5"></div></div>
      <div class="legend"><div class="white">--</div><div class="white">more >></div><div class="white">&nbsp;</div><div class="white">&nbsp;</div><div class="white">&nbsp;</div><div class="white"></div></div>
    </div>
  </div>
  <div class="map-group">
    <div class="chartTitle">% ballots accepted compared to 2018</div>
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
    <div class="center">
      <div class="legend"><div class="orange5"></div><div class="orange3"></div><div class="orange1"></div><div class="green1"></div><div class="green3"></div><div class="green5"></div></div>
      <div class="legend"><div class="white"></div><div class="white"></div><div class="white">-</div><div class="white">+</div><div class="white"></div><div class="white"></div></div>
    </div>
  </div>
</div>
