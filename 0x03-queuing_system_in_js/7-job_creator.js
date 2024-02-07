import kue from 'kue';
import redis from 'redis';

const client = redis.createClient();
const jobs = kue.createQueue();

const jobData = [
  { phoneNumber: '123', message: 'Message 1' },
  { phoneNumber: '456', message: 'Message 2' },
  { phoneNumber: '789', message: 'Message 3' }
];

jobData.forEach(data => {
  const job = jobs.create('push_notification_code', data);

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', () => {
    console.log(`Notification job ${job.id} failed`);
  });

  job.save();
});
