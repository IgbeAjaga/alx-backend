import kue from 'kue';
import redis from 'redis';

const client = redis.createClient();
const jobs = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'Job notification for you!'
};

const job = jobs.create('push_notification_code', jobData);

job.save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
});
