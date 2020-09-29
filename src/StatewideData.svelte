<script>
  import {intcomma} from 'journalize';
	import moment from 'moment-timezone';

  export let county_data_2020 = [];

  let last_updated;
  let total_ballots_requested = 0;
  let total_ballots_accepted = 0;
  let pct_ballots_accepted = 0;

  const round_pct = (input) => (100 * input).toFixed(1) + '%';

  $: {
    if (county_data_2020.length > 0) {
      last_updated = moment(county_data_2020[0].date_latest).tz('America/Chicago').format('MMM D, YYYY')
      total_ballots_requested = county_data_2020.reduce((total, county) => total + county.apps_submitted_latest, 0);
      total_ballots_accepted = county_data_2020.reduce((total, county) => total + county.ballots_accepted_latest, 0);
      pct_ballots_accepted = total_ballots_accepted / total_ballots_requested;
    }
  }

</script>

<h3>Total absentee ballots requested: {intcomma(total_ballots_requested)}</h3>
<h3>Total absentee ballots accepted so far: {intcomma(total_ballots_accepted)} ({round_pct(pct_ballots_accepted)} of all requested)</h3>
<div>Last update: {last_updated}</div>
