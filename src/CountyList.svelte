<script>
	import {intcomma} from 'journalize';
  export let county_data = [];
</script>

<table id="county-totals">
  <tr>
    <th>County</th>
    <th>Ballots requested</th>
    <th>Ballots accepted</th>
  </tr>
  {#each county_data as county, i}
  <tr>
    <td>{county.county_name}</td>
    <td>{intcomma(county.apps_submitted_latest)}</td>
    <td>{intcomma(county.ballots_accepted_latest)}</td>
  </tr>
  {/each}
  </table>
