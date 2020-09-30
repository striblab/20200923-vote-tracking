<script>

import county_results_history from './scraper/json/county-results-history.json';
import IsoMap from './IsoMap.svelte'

</script>

<h3>Hey look maps</h3>

<div>
  <h4>Trump counties 2016</h4>
  <IsoMap {county_results_history} show_var='winner_2016' show_val='R'}/>
</div>
<div>
  <h4>Clinton counties 2016</h4>
  <IsoMap {county_results_history} show_var='winner_2016' show_val='D'}/>
</div>
