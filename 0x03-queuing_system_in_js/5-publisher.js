import redis from 'redis';

const publisher = redis.createClient();

publisher.on('connect', () => {
  console.log('Redis publisher connected to the server');
});

publisher.publish('holberton school channel', 'Redis is great');
