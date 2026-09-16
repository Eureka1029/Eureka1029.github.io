---
layout: page
title: Projects
permalink: /projects/
description: Projects and experiments.
nav: true
nav_order: 2
horizontal: false
---

{% assign sorted_projects = site.projects | sort: "importance" %}

<div class="projects">
  {% if sorted_projects.size > 0 %}
    <div class="row row-cols-1 row-cols-md-2">
      {% for project in sorted_projects %}
        {% include projects.liquid %}
      {% endfor %}
    </div>
  {% else %}
    <p>No projects yet.</p>
  {% endif %}
</div>
