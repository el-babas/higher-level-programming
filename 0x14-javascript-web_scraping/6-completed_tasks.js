#!/usr/bin/node
const axios = require('axios').default;

const api = process.argv[2];
/**
 * Request status code.
 */
axios.get(api)
  .then(function (response) {
    // handle success
    const task = response.data;
    const taskCompleted = {};
    task.forEach(function (element) {
      if (element.completed === true) {
        const userId = element.userId;
        if (taskCompleted[userId] === undefined) {
          taskCompleted[userId] = 1;
        } else {
          taskCompleted[userId] += 1;
        }
      }
    });
    console.log(taskCompleted);
  })
  .catch(function (error) {
    // handle error
    console.log(error.message);
  })
  .then(function () {
    // always executed
  });
