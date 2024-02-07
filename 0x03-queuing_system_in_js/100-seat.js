const express = require('express');
const redis = require('redis');
const kue = require('kue');
const { promisify } = require('util');

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

const reserveSeat = promisify(client.set).bind(client);
const getCurrentAvailableSeats = promisify(client.get).bind(client);

let numberOfAvailableSeats = 50;
let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      const currentSeats = await getCurrentAvailableSeats('available_seats');
      const newSeats = parseInt(currentSeats) - 1;

      if (newSeats < 0) {
        throw new Error('Not enough seats available');
      }

      numberOfAvailableSeats = newSeats;
      await reserveSeat('available_seats', numberOfAvailableSeats.toString());

      if (numberOfAvailableSeats === 0) {
        reservationEnabled = false;
      }

      console.log(`Seat reservation job ${job.id} completed`);
      done();
    } catch (error) {
      console.error(`Seat reservation job ${job.id} failed: ${error.message}`);
      done(error);
    }
  });
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
