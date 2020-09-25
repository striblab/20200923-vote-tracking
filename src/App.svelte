<script>
	// export let name;
	import {intcomma} from 'journalize';
	import moment from 'moment-timezone';

	import StatewideData from './StatewideData.svelte';
	import CountyList from './CountyList.svelte';

	// Received by Oct. 13
	let now = moment().tz('America/Chicago')
	let registration_deadline = moment('2020-10-13 23:59:59').tz('America/Chicago')
	let time_to_preregister = registration_deadline.diff(now, 'days')

	let election_day = moment('2020-11-03 12:00').tz('America/Chicago')
	let time_to_mail_ballot = election_day.diff(now, 'days')

	let county_obj;
	let county_data = [];

	let getCountyData = async function() {
		const response = await fetch("https://static.startribune.com/staging/news/projects/all/20200923-vote-tracking/json/county-list-latest.json");
		county_obj = await response.json();
		if (response.ok) {
      return county_data;  // This is a little weird because the dict gets reshaped into a list below
		}
	}

	$: {
		if (county_obj) {
			for (const [key, value] of Object.entries(county_obj)) {
				console.log(key, value);
				var item = value;
				item['county_name'] = key;
				county_data.push(item);
			}
		}
	}
</script>

<div>In Minnesota you have {time_to_preregister} days ({registration_deadline.format('MMM D, YYYY [at] h:mm a')}) left to register early (you can also register at the polls on Election Day).</div>

<div>In Minnesota you have {time_to_mail_ballot} days ({election_day.format('MMM D, YYYY [at] h:mm a')}) left to mail your ballot (you can also drop your ballot off by Election Day).</div>

{#await getCountyData()}
	<p>Loading data ...</p>
{:then county_data}
	<StatewideData {county_data}/>
	<CountyList {county_data}/>
{:catch error}
	<p style="color: red">Something bad happened</p>
{/await}
