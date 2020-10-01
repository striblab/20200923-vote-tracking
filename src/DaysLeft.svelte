<script>
  import moment from 'moment-timezone';

  // Received by Oct. 13
  let now = moment().tz('America/Chicago')
  let registration_deadline = moment('2020-10-13 23:59:59').tz('America/Chicago')
  let time_to_preregister = registration_deadline.diff(now, 'days')

  let election_day = moment('2020-11-03 12:00').tz('America/Chicago')
  let time_to_mail_ballot = election_day.diff(now, 'days')
</script>

<div class="days-left-header">In Minnesota you have ...</div>
<div class="days-left-group">
  <div class="days-left">
    <span class="preregister-days number">{time_to_preregister}</span>
    <span class="date-explainer">days remain to<br />register early</span>
  	<span class="detail-date">({registration_deadline.format('MMM D, YYYY')})</span>
  	<span class="small">You can also register at the polls on Election Day</span>
  </div>
  <div class="days-left">
    <span class="mailing-days number">{time_to_mail_ballot}</span>
    <span class="date-explainer">days remain to<br />mail your ballot</span>
    <span class="detail-date">({election_day.format('MMM D, YYYY')})</span>
  	<span class="small">You can also drop your ballot off by Election Day</span>
  </div>
</div>
<p>&nbsp;</p>
