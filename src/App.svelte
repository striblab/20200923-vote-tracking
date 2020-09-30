<script>
	import {intcomma} from 'journalize';
	import moment from 'moment-timezone';

	import DaysLeft from './DaysLeft.svelte';
	import StatewideData from './StatewideData.svelte';
	import StatewideWeeklyChart from './StatewideWeeklyChart.svelte';
	import CountyList from './CountyList.svelte';
	import county_obj_2018 from './scraper/json/county-list-2018.json';

	// This is used by several of the modules to map 2020 dates to "weeks to go" from each other year.
	const date_label_lookup = [
    {'date': new Date(moment('2020-09-25').tz('America/Chicago')), 'weeks_away': 6, 'label': '6 weeks away'},
    {'date': new Date(moment('2020-10-02').tz('America/Chicago')), 'weeks_away': 5, 'label': '5 weeks away'},
    {'date': new Date(moment('2020-10-09').tz('America/Chicago')), 'weeks_away': 4, 'label': '4 weeks away'},
    {'date': new Date(moment('2020-10-16').tz('America/Chicago')), 'weeks_away': 3, 'label': '3 weeks away'},
    {'date': new Date(moment('2020-10-23').tz('America/Chicago')), 'weeks_away': 2, 'label': '2 weeks away'},
    {'date': new Date(moment('2020-10-30').tz('America/Chicago')), 'weeks_away': 1, 'label': '1 week away'},
    {'date': new Date(moment('2020-11-02').tz('America/Chicago')), 'weeks_away': 0, 'label': ''},
    {'date': new Date(moment('2020-11-03').tz('America/Chicago')), 'weeks_away': 'election_day', 'label': 'Election Day'},
    {'date': new Date(moment('2020-11-06').tz('America/Chicago')), 'weeks_away': '', 'label': ''}
  ]

	const set_2020_dates = function (year_data) {
    year_data.forEach(element => element.date_2020 = date_label_lookup.find(label => label.weeks_away == element.weeks_away).date);
  }

	// Turn the object-based county JSON into an array
	const reshape_county_list = function (obj) {
		var out_array = [];
		for (const [key, value] of Object.entries(obj)) {
			if (key != 'ts_statewide') {
				var item = value;
				item['county_name'] = key;
				out_array.push(item);
			}
		}
		return out_array;
	}

	// Tag weekly data from previous years with a 2020 date for chart placement/comparison
	set_2020_dates(county_obj_2018.ts_statewide);
	let county_list_2018 = reshape_county_list(county_obj_2018);
	// Tag dates for each county's time series
	county_list_2018.forEach(element => set_2020_dates(element.ts));

	let county_obj;
	let county_data_2020 = [];
	let statewide_timeseries = [];

	let getCountyData = async function() {
		const response = await fetch("https://static.startribune.com/staging/news/projects/all/20200923-vote-tracking/json/county-list-latest.json");
		county_obj = await response.json();
		if (response.ok) {
      return reshape_county_list(county_obj);
		}
	}

	$: {
		if (county_obj) {
			statewide_timeseries = county_obj['ts_statewide'];
		}
	}
</script>

<DaysLeft/>

<h2>Absentee votes accepted</h2>

{#await getCountyData()}
	<p>Loading data ...</p>
{:then county_data_2020}
	<StatewideData {county_data_2020}/>
	<StatewideWeeklyChart data={statewide_timeseries} data_2018={county_obj_2018.ts_statewide} id='statewide-trend-chart' x_axis_labels={date_label_lookup}/>
	<CountyList {county_data_2020} county_data_2018={county_list_2018} x_axis_labels={date_label_lookup}/>
{:catch error}
	<p style="color: red">Something bad happened</p>
{/await}
