<script>
  import {intcomma} from 'journalize';
	import moment from 'moment-timezone';

  export let county_data = [];

  let last_updated;
  let total_ballots_requested = 0;
  let total_ballots_accepted = 0;
  let pct_ballots_accepted = 0;

  const round_pct = (input) => (100 * input).toFixed(1) + '%';

  $: {
    if (county_data.length > 0) {
      last_updated = moment(county_data[0].date_latest).tz('America/Chicago').format('MMM D, YYYY')
      total_ballots_requested = county_data.reduce((total, county) => total + county.apps_submitted_latest, 0);
      total_ballots_accepted = county_data.reduce((total, county) => total + county.ballots_accepted_latest, 0);
      pct_ballots_accepted = total_ballots_accepted / total_ballots_requested;
    }
  }

</script>

<div>Last update: {last_updated}</div>
<div>Total absentee ballots requested: {intcomma(total_ballots_requested)}</div>
<div>Total absentee ballots accepted: {intcomma(total_ballots_accepted)} ({round_pct(pct_ballots_accepted)})</div>
