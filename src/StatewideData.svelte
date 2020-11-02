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

<div class="chartTitle">Absentee voting is on track to dwarf past elections</div>
<div class="updatedTime">Last update: {last_updated}</div>
<p class="footnote">Note: weekly numbers reflect accepted absentee votes by mail and in-person</p>
<div class="stats">Total absentee ballots requested: <span class="bolded">{intcomma(total_ballots_requested)}</span></div>
<div class="stats">Total absentee ballots accepted so far: <span class="highlight highlight-under bolded">{intcomma(total_ballots_accepted)}</span> ({round_pct(pct_ballots_accepted)} of all requested)</div>
<div class="stats">So far absentee ballots accepted this year are up about 150% from <span class="highlight-2016">2016</span> and 170% from <span class="highlight-2018">2018</span>.</div>