import kue from 'kue';
import redis from 'redis';

const client = redis.createClient();
const jobs = kue.createQueue();

jobs.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, (error) => {
    if (error) done(error);
    else done();
  });
});

function sendNotification(phoneNumber, message, callback) {
  console.log(`Sending notification to ${phoneNumber}: ${message}`);
  callback();
}
