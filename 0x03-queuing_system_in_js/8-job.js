import kue from 'kue';
import redis from 'redis';

const client = redis.createClient();
const jobs = kue.createQueue();

function createPushNotificationsJobs(jobs, jobData) {
  const job = jobs.create('push_notification_code', jobData);

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', () => {
    console.log(`Notification job ${job.id} failed`);
  });

  job.save();
}

export default createPushNotificationsJobs;
