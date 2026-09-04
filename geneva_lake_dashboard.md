<style>
:root {
  --ink: #17324d;
  --muted: #61788d;
  --line: #d8e2e8;
  --lake: #176b87;
  --coral: #d1495b;
  --paper: #f5f8f9;
  --white: #ffffff;
}

* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background: var(--paper);
  font-family: Georgia, "Times New Roman", serif;
}
.dashboard {
  max-width: 1400px;
  margin: 0 auto;
}
.page {
  min-height: 100vh;
  padding: 48px 56px;
  background: var(--white);
  border-bottom: 1px solid var(--line);
  page-break-after: always;
}
.page:last-child { page-break-after: auto; }
.kicker {
  margin: 0 0 12px;
  color: var(--coral);
  font-family: Arial, sans-serif;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
h1, h2 { margin-top: 0; }
h1 { max-width: 850px; font-size: clamp(2.4rem, 6vw, 5.8rem); line-height: 0.98; }
h2 { font-size: clamp(1.8rem, 4vw, 3.4rem); line-height: 1.05; }
.lede { max-width: 700px; color: var(--muted); font-size: 1.15rem; line-height: 1.5; }
.hero-grid, .two-col, .four-grid {
  display: grid;
  gap: 28px;
  align-items: start;
}
.hero-grid { grid-template-columns: 0.85fr 1.15fr; }
.two-col { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.four-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.media {
  width: 100%;
  display: block;
  border: 1px solid var(--line);
  background: #eef4f6;
}
.hero-image { max-height: 78vh; object-fit: contain; }
.graph { max-height: 58vh; object-fit: contain; }
.satellite-feature { max-width: 92%; margin: 34px auto 0; }
.weather-figure { max-width: 78%; }
.video-feature { max-width: 88%; margin: 30px auto 0; }
.video-feature video.media { max-height: 75vh; }
.temperature-illustration { max-width: 58%; margin: 28px auto 0; }
.temperature-pair { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 28px; margin-top: 28px; }
video.media { max-height: 62vh; }
figure { margin: 0; }
figcaption {
  margin-top: 9px;
  color: var(--muted);
  font-family: Arial, sans-serif;
  font-size: 0.82rem;
  line-height: 1.35;
}
.section-rule {
  width: 100%;
  height: 5px;
  margin: 24px 0 32px;
  background: var(--lake);
}
.commentary {
  min-height: 110px;
  margin-top: 34px;
  padding: 18px 20px;
  border: 1px dashed #9db1bd;
  background: #fbfcfc;
  color: var(--muted);
  font-family: Arial, sans-serif;
  font-size: 0.9rem;
}
.commentary strong { color: var(--ink); }
.small-note { color: var(--muted); font-size: 0.9rem; }
@media (max-width: 800px) {
  .page { padding: 30px 22px; }
  .hero-grid, .two-col, .four-grid { grid-template-columns: 1fr; }
  .satellite-feature { max-width: 100%; }
  .weather-figure { max-width: 100%; }
  .video-feature, .temperature-illustration { max-width: 100%; }
  .temperature-pair { grid-template-columns: 1fr; }
  h1 { font-size: 3.25rem; }
}
@media print {
  body { background: white; }
  .page { min-height: 0; height: 100vh; overflow: hidden; }
}
</style>

<div class="dashboard">

<section class="page">
  <p class="kicker">Lake Geneva / Field note</p>
  <div class="section-rule"></div>
  <div>
    <h1>Why has Lake Geneva suddendly turned green? </h1>
    <p class="lede">You may have noticed that the lake's water turned turbid and green in a matter of days. Sattelite images confirmed that while low in August 25th, the amount of algae has doubled as of today.</p>
    <p class="small-note"> What happenend and is this unusual? </p>
  </div>
  <figure class="satellite-feature">
    <img class="media hero-image" src="Illustrations/CHL.png" alt="Chlorophyll-a illustration for Lake Geneva">
    <figcaption>Satellite chlorophyll-a observations, August–September 2026 Source asset: AlpLakes</figcaption>
  </figure>
  <figure class="weather-figure" style="margin-top: 34px;">
    <img class="media graph" src="graphs/weather_since_2026_08_20.png" alt="Weather observations since 20 August 2026 with air temperature, irradiance, wind speed, and dominant wind direction arrows">
    <figcaption>Weather since 20 August 2026. Air temperature, irradiance, and wind speed are shown at the native 10-minute resolution; arrows indicate dominant daily wind direction. Source: DataLakes</figcaption>
  </figure>
  <div class="commentary"><strong>Commentary</strong><br><br> Over the week end and throughout monday, the North-East wind blew consistently. The weather has been quiet and sunny from Tuesday</div>
</section>

<section class="page">
  <p class="kicker">Page 02 / Water column</p>
  <h2>Heat, mixing, and the water column</h2>
  <p class="lede">The temperature 3D model and CTD profiles provide the vertical context behind the surface signal.</p>
  <figure class="video-feature">
    <video class="media" controls preload="metadata">
      <source src="Illustrations/TEMP_AUG28_SEP3.mp4" type="video/mp4">
      Your browser does not support embedded video. Open TEMP_AUG28_SEP3.mp4 directly.
    </video>
    <figcaption>Surface water temperatures from 28 August to 3 September 2026. Source asset: AlpLakes</figcaption>
  </figure>
  <div class="temperature-pair">
    <figure class="temperature-illustration">
      <img class="media graph" src="Illustrations/TEMP_AUG31.png" alt="Water temperature illustration from 31 August 2026">
      <figcaption>Screenshot from 31 August 2026 showing the upwelling from bottom, cold water on the northern shore of Lake geneva. Source asset: Alplakes</figcaption>
    </figure>
    <figure class="temperature-illustration">
      <img class="media graph" src="Illustrations/tilting_thermocline.png" alt="Illustration of a tilting thermocline in Lake Geneva">
      <figcaption>Screenshot of a North-South transect of Lake Geneva, showing the warm surface waters being pushed by the synoptic wind southward. Source: Alplakes </figcaption>
    </figure>
  </div>
  <div class="commentary"><strong>Commentary</strong><br><br> As the wind blew contitnuously from the NE, it pushed warm surface waters to the South-Western shore of the lake, leading to a downwelling downwind and an upwelling upwind. The 31 August temperature snapshot shows the upwelling of coldwaters along the northern shore. </div>
</section>

<section class="page">
  <p class="kicker">Page 03 / CTD profiles</p>
  <h2>What the water column reveals</h2>
  <p class="lede">The CTD profiles show how temperature, chlorophyll-a, and conductivity vary with depth during the event.</p>
  <figure style="margin-top: 30px;">
    <img class="media graph" src="graphs/ctd_temperature_chlorophyll_profiles_from_2026_08_20.png" alt="CTD water temperature, chlorophyll-a, and conductivity profiles after 20 August 2026">
    <figcaption>CTD depth profiles after 20 August 2026: water temperature, chlorophyll-a, and conductivity normalized to 25 °C. Profiles are colored by date.</figcaption>
  </figure>
  <div class="commentary"><strong>Commentary</strong><br><br> The wind event led to tilting and deepening of the thermocline and brought up to the surface colder waters. Deep cold waters are rich in nutrients, such as phosphorous...  While the surface waters were limited in nutrients, a fresh supply in phosphorous and sunny conditions makes the surface waters ground for algal growth</div>
</section>

<section class="page">
  <p class="kicker">Page 04 / Context</p>
  <h2>Is this unusual?</h2>
  <p class="lede">The bloom is sudden but the climatology of remote-sensed chlorophyll for the lake over the latst 11 years shows that this regain in algal growth is rather typical for late summer. The satellite record places the 2026 chlorophyll-a observations within the seasonal distribution and the year-to-year spread.</p>
  <div class="four-grid">
    <figure>
      <img class="media graph" src="graphs/geneva_chlorophyll_a_climatology.png" alt="Geneva chlorophyll-a climatology with 2026 overlay">
      <figcaption>Geneva chlorophyll-a day-of-year climatology with 2026 observations overlaid. The analysis uses the satellite mean chlorophyll-a field.</figcaption>
    </figure>
    <figure>
      <img class="media graph" src="graphs/geneva_air_temperature_climatology_netcdf.png" alt="Geneva air temperature climatology with 2026 overlay">
      <figcaption>Mean air-temperature climatology with 2026 overlaid (2019-2026 from LéXPLORE Source DataLakes).</figcaption>
    </figure>
    <figure>
      <img class="media graph" src="graphs/geneva_wind_climatology_netcdf.png" alt="Geneva wind-speed climatology with 2026 overlay">
      <figcaption>>Mean windspeed climatology with 2026 overlaid (2019-2026 from LéXPLORE Source DataLakes).</figcaption>
    </figure>
    <figure>
      <img class="media graph" src="graphs/geneva_daily_mean_chlorophyll_a_violin_by_year_doy150_240.png" alt="Annual violin plot of daily mean chlorophyll-a between day of year 150 and 240">
      <figcaption>Annual distributions of daily mean chlorophyll-a for DOY 150–240 (from satellites, source: AlpLakes).</figcaption>
    </figure>
  </div>
  <div class="commentary"><strong>Commentary</strong><br><br> The wind regime for the year 2026 has been within typucally observd values since 2019. The summer of 2026 has been 4-5°C warmer than any summers obszrved from LéXPLORE since 2019. In spite of this canicular summer, the amount of algae in the lake has been very consistent with values observed in the previous year, not more, not less. Wind-driven upwellings and seiches are transient but important and recurrent mechanisms to restore some nutrients to the surface waters in Lake Geneva in summer. </div>
</section>

</div>
