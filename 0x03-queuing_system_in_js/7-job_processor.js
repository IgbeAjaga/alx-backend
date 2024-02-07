import kue from 'kue';
import redis from 'redis';

const client = redis.createClient();
const jobs = kue.createQueue();

jobs.process('push_notification_code', (job, done) => {
  const blacklisted = ['123', '456'];
  if (blacklisted.includes(job.data.phoneNumber)) {
    return done(Error('This phone number is blacklisted'));
  }
  sendNotification(job.data.phoneNumber, job.data.message, (error) => {
    if (error) done(error);
    else done();
  });
});

function sendNotification(phoneNumber, message, callback) {
  console.log(`Sending notification to ${phoneNumber}: ${message}`);
  callback();
}
