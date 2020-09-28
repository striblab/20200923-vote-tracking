<script>
	// export let name;
	import {intcomma} from 'journalize';
	import moment from 'moment-timezone';

	import StatewideData from './StatewideData.svelte';
	import StatewideWeeklyChart from './StatewideWeeklyChart.svelte';
	import CountyList from './CountyList.svelte';
	import county_obj_2018 from './scraper/json/county-list-2018.json';


	// Received by Oct. 13
	let now = moment().tz('America/Chicago')
	let registration_deadline = moment('2020-10-13 23:59:59').tz('America/Chicago')
	let time_to_preregister = registration_deadline.diff(now, 'days')

	let election_day = moment('2020-11-03 12:00').tz('America/Chicago')
	let time_to_mail_ballot = election_day.diff(now, 'days')

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
	console.log(county_list_2018);

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

<div>In Minnesota you have {time_to_preregister} days ({registration_deadline.format('MMM D, YYYY [at] h:mm a')}) left to register early (you can also register at the polls on Election Day).</div>

<div>In Minnesota you have {time_to_mail_ballot} days ({election_day.format('MMM D, YYYY [at] h:mm a')}) left to mail your ballot (you can also drop your ballot off by Election Day).</div>

{#await getCountyData()}
	<p>Loading data ...</p>
{:then county_data_2020}
	<StatewideData {county_data_2020}/>
	<StatewideWeeklyChart data={statewide_timeseries} id='statewide-trend-chart'/>
	<CountyList {county_data_2020}/>
{:catch error}
	<p style="color: red">Something bad happened</p>
{/await}
