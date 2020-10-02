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

<h2>Absentee voting is on track to dwarf past elections</h2>
<div class="updatedTime">Last update: {last_updated}</div>
<div class="stats">Total absentee ballots requested: <span class="bolded">{intcomma(total_ballots_requested)}</span></div>
<div class="stats">Total absentee ballots accepted so far: <span class="highlight highlight-under bolded">{intcomma(total_ballots_accepted)}</span> ({round_pct(pct_ballots_accepted)} of all requested)</div>

