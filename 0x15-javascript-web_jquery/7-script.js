#!/usr/bin/env node
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(response) {
  const name = response.name;
  $('DIV#character').text(name);
});
