<script>
  import moment from 'moment-timezone';

  // Received by Oct. 13
  let now = moment().tz('America/Chicago')
  let registration_deadline = moment('2020-10-13 23:59:59').tz('America/Chicago')
  let time_to_preregister = registration_deadline.diff(now, 'days')

  let election_day = moment('2020-11-03 12:00').tz('America/Chicago')
  let time_to_mail_ballot = election_day.diff(now, 'days')
</script>

<div class="days-left-header">In Minnesota ...</div>
<div class="days-left-group">
  <div class="days-left">
    <span class="preregister-days number">{time_to_preregister}</span>
    <span class="date-explainer">days left to<br />register early</span>
  	<span class="detail-date">({registration_deadline.format('MMM D, YYYY')})</span>
  	<span class="small">You can also register at the polls on Election Day</span>
  </div>
  <div class="days-left">
    <span class="mailing-days number">{time_to_mail_ballot}</span>
    <span class="date-explainer">days left to<br />mail your ballot</span>
    <span class="detail-date">({election_day.format('MMM D, YYYY')})</span>
  	<span class="small">You can also drop your ballot off by Election Day</span>
  </div>
</div>
<p>&nbsp;</p>

<div class="hero-override">
<p>Record numbers of mail ballots are expected to be counted for November’s general election, and in our September Minnesota Poll, <a href="https://www.startribune.com/poll-minnesota-voters-split-on-integrity-of-mail-in-voting/572533691/">more than a third of respondents</a> indicated they would plan to vote early rather than in person on Election Day. The tally from the Secretary of State’s office updates on Fridays leading up to Nov. 3, but in the meantime, read up on where Minnesota’s <a href="https://www.startribune.com/minnesota-voters-guide-2020-election-senate-house-candidates-who-is-running-gop-dfl-issues/572227401/">major candidates stand on key issues</a>, <a href="https://www.startribune.com/how-to-vote-2020-elections-minnesota-voting-absentee-president-senate-congress-covid-19-coronavirus/572227371/">how to register and vote</a>, and <a href="https://www.startribune.com/what-happens-to-your-minnesota-mail-in-absentee-ballot-after-you-mail-it-votes-counted/572029141/?refresh=true">what happens to an absentee ballot after it’s sent</a>, and keep up-to-date by subscribing to our <a href="http://newsletters.startribune.com/pages/1788361/4540">Politics newsletter</a>, penned by reporters daily.</p>
</div>

<p class="buffer">&nbsp;</p>
