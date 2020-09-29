<script>
	// export let name;
	import {intcomma} from 'journalize';
	// import moment from 'moment-timezone';

	import DaysLeft from './DaysLeft.svelte';
	import StatewideData from './StatewideData.svelte';
	import StatewideWeeklyChart from './StatewideWeeklyChart.svelte';
	import CountyList from './CountyList.svelte';
	import county_obj_2018 from './scraper/json/county-list-2018.json';

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

	let county_obj;
	let county_data_2020 = [];
	let statewide_timeseries = [];
	let county_list_2018 = reshape_county_list(county_obj_2018);
	// let statewide_timeseries_2018 = [];
	console.log(county_obj_2018);

	let getCountyData = async function() {
		const response = await fetch("https://static.startribune.com/staging/news/projects/all/20200923-vote-tracking/json/county-list-latest.json");
		county_obj = await response.json();
		if (response.ok) {
      return reshape_county_list(county_obj);  // This is a little weird because the dict gets reshaped into a list below
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
	<StatewideWeeklyChart data={statewide_timeseries} data_2018={county_obj_2018.ts_statewide} id='statewide-trend-chart'/>
	<CountyList {county_data_2020}/>
{:catch error}
	<p style="color: red">Something bad happened</p>
{/await}
