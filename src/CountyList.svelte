<script>
	import CountySparkline from './CountySparkline.svelte';
	import county_results_history from './scraper/json/county-results-history.json';

	import {intcomma} from 'journalize';
  import moment from 'moment-timezone';

  export let county_data_2020 = [];
	export let county_data_2018 = [];
	export let x_axis_labels;

	let current_week = x_axis_labels.find(x => x.date.getTime() == new Date(moment(county_data_2020[0].date_latest).tz('America/Chicago')).getTime()).weeks_away

	const get_county_prev_year = function (data, county_name) {
		// console.log(county_name)
		return data.find(elem => elem.county_name.toLowerCase() == county_name.toLowerCase())
	}

	const get_accepted_by_week = function (data, week) {
		return data.find(elem => elem.weeks_away == week).ballots_accepted
	}

	const pct_to_date = function (accepted_2020, accepted_prev_year_to_date) {
		// console.log(accepted_2020, accepted_prev_year_to_date);
		if (accepted_prev_year_to_date == 0 || accepted_2020 == 0) {
			return '--'
		} else {
			var pct_change = (accepted_2020 - accepted_prev_year_to_date) / accepted_prev_year_to_date
		}
		var change_sign = pct_change >= 0 ? '+' : '';
		return change_sign + (100 * pct_change).toFixed(1) + '%'
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

<p class="buffer">&nbsp;</p>
<div class="chartTitle">Absentee voting by county</div>
<table id="county-totals">
  <tr>
    <th>County</th>
		<th class="winners">Winner 2012</th>
		<th class="winners">Winner 2016</th>
		<th>Ballots requested</th>
    <th>Ballots accepted</th>
		<th class="current">% of 2018<br />({current_week} weeks away)</th>
		<th></th>
  </tr>
  {#each county_data_2020 as county, i}
  <tr>
    <td>{county.county_name}</td>
		<td class="winners">{@html winner_2012(county.county_name)}</td>
		<td class="winners">{@html winner_2016(county.county_name)}</td>
    <td>{intcomma(county.apps_submitted_latest)}</td>
    <td>{intcomma(county.ballots_accepted_latest)}</td>
		<td class="current">{pct_to_date(
				county.ballots_accepted_latest,
				get_accepted_by_week(get_county_prev_year(county_data_2018, county.county_name).ts, current_week)
			)}</td>
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
	<p class="footnote">Note: counties without a percent change listed lacked accepted absentee votes in the first week of 2018's data.</p>
