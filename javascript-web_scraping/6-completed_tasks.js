#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
// get data
request(url, (error, response, body) => {
  if (error) {
    console.error('Request error:', error);
    process.exit(1);
  }
  // parse data
  const tasks = JSON.parse(body);

  // setup an obj to store tasks count and ids
  const completedTasksCount = {};

  // iterate through tasks
  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTasksCount[task.userId]) {
        completedTasksCount[task.userId] = 0;
      }
      completedTasksCount[task.userId]++;
    }
  });

  // print task and user id
  console.log(completedTasksCount);
});
