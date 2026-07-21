---
layout: page
permalink: /publications/
title: Publications
description:
years: [2026, 2025, 2024, 2023]
nav: true
nav_order: 2
importance: 2
---

<p class="section-note">
  * indicates equal contribution. Also on
  <a href="https://scholar.google.com/citations?user={{ site.scholar_userid }}" target="_blank"
    rel="noopener">Google Scholar</a>.
</p>

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
<h2 class="year">{{y}}</h2>
{% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>