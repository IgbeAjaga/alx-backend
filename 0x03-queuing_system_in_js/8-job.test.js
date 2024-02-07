import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import redis from 'redis';

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    const client = redis.createClient();
    const jobs = kue.createQueue();
    jobs.testMode.enter();
  });

  afterEach(() => {
    const jobs = kue.createQueue();
    jobs.testMode.exit();
  });

  it('creates a new job and enqueues it', () => {
    const jobData = {
      phoneNumber: '123',
      message: 'Test message'
    };
    createPushNotificationsJobs(jobData);
    const jobs = kue.createQueue();
    jobs.createJob('push_notification_code', jobData).save();
    expect(jobs.testMode.jobs.length).to.equal(1);
  });
});
