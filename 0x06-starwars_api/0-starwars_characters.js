#!/usr/bin/node

const request = require('request');

const getFilm = (callback) => {
  const args = process.argv.slice(2);

  if (args.length < 1) {
    process.exit(1);
  }
  const filmid = args[0];

  // Send a request to the endpoint
  const url = `https://swapi-api.alx-tools.com/api/films/${filmid}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error in getting the endpoint', error);
      callback(error, null);
      return;
    }
    if (response.statusCode === 200) {
      callback(null, body);
    } else {
      callback(new Error(`Error: ${response.statusCode}`), null);
    }
  });
};

const getName = () => {
  getFilm((error, body) => {
    if (error) {
      console.error('Error in getting the film', error);
      return;
    }
    const characters = JSON.parse(body).characters;

    const charaNames = characters.map(
      url => new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          }
          if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject(new Error(`Error: ${response.statusCode}`));
          }
        });
      })
    );

    Promise.all(charaNames)
      .then((names) => {
        console.log(names.join('\n'));
      })
      .catch((error) => {
        console.error('Error in getting the characters', error);
      });
  });
};

getName();
