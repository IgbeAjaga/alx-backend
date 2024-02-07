import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', () => {
  console.log('Redis subscriber connected to the server');
});

subscriber.on('message', (channel, message) => {
  console.log(`Message received: ${message}`);
});

subscriber.subscribe('holberton school channel');
