---
layout: page
title: 项目
permalink: /projects/
description: 正在构建与维护的项目。
nav: true
nav_order: 2
horizontal: false
---

{% assign sorted_projects = site.projects | sort: "importance" %}

<div class="projects">
  <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>

