#!/usr/bin/node
/**
*prints users with completed tasks and number
*/
const url = 'https://jsonplaceholder.typicode.com/todos';
const request = require('request');
const dict = {};
request.get(url, (err, body, response) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(response);
  for (const task of data) {
    const userId = task.userId;
    if (task.completed === true) {
      if (userId in dict === false) { dict[userId.toString()] = 1; } else { dict[userId] += 1; }
    }
  }
  console.log(dict);
});
