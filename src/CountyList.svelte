<script>
	import CountySparkline from './CountySparkline.svelte';

	import {intcomma} from 'journalize';
  export let county_data_2020 = [];
	export let county_data_2018 = [];
	export let x_axis_labels;
</script>

<h2>Absentee voting by county</h2>
<table id="county-totals">
  <tr>
    <th>County</th>
    <th>Ballots requested</th>
    <th>Ballots accepted</th>
		<th></th>
  </tr>
  {#each county_data_2020 as county, i}
  <tr>
    <td>{county.county_name}</td>
    <td>{intcomma(county.apps_submitted_latest)}</td>
    <td>{intcomma(county.ballots_accepted_latest)}</td>
		<td class="spark-td"><CountySparkline name={county.county_name} data_2020={county.ts} data_2018={county_data_2018.find(elem => elem.county_name.toLowerCase() == county.county_name.toLowerCase())} {x_axis_labels}/></td>
  </tr>
  {/each}
  </table>
