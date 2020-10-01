<script>
	import CountySparkline from './CountySparkline.svelte';
	import county_results_history from './scraper/json/county-results-history.json';

	import {intcomma} from 'journalize';
  import moment from 'moment-timezone';

  export let county_data_2020 = [];
	export let county_data_2018 = [];
	export let x_axis_labels;
	export let current_week;

	const get_county_prev_year = function (data, county_name) {
		// console.log(county_name)
		return data.find(elem => elem.county_name.toLowerCase() == county_name.toLowerCase())
	}

	const display_pct = function (pct_change) {
		var change_sign = pct_change >= 0 ? '+' : '';
		return change_sign + pct_change + '%'
	}

	const winner_2012 = function(county_name) {
		var county_obj = county_results_history.find(c => c.county.toLowerCase() == county_name.toLowerCase());
		return county_obj.winner_2012 == 'D' ? '<span class="winner-d">Obama</span>' : '<span class="winner-r">Romney</span>';
	}

	const winner_2016 = function(county_name) {
		var county_obj = county_results_history.find(c => c.county.toLowerCase() == county_name.toLowerCase());
		return county_obj.winner_2016 == 'D' ? '<span class="winner-d">Clinton</span>' : '<span class="winner-r">Trump</span>';
	}

</script>

<h2>Absentee voting by county</h2>
<table id="county-totals">
  <tr>
    <th>County</th>
		<th>Winner 2012</th>
		<th>Winner 2016</th>
		<th>Ballots requested</th>
    <th>Ballots accepted</th>
		<th>% of 2018<br/>({current_week} weeks to go)</th>
		<th></th>
  </tr>
  {#each county_data_2020 as county, i}
  <tr>
    <td>{county.county_name}</td>
		<td>{@html winner_2012(county.county_name)}</td>
		<td>{@html winner_2016(county.county_name)}</td>
    <td>{intcomma(county.apps_submitted_latest)}</td>
    <td>{intcomma(county.ballots_accepted_latest)}</td>
		<td>{display_pct(county.pct_to_date)}</td>
		<td class="spark-td">
				<CountySparkline
					name={county.county_name}
					data_2020={county.ts}
					data_2018={get_county_prev_year(county_data_2018, county.county_name).ts}
					{x_axis_labels}
				/>
		</td>
  </tr>
  {/each}
  </table>
