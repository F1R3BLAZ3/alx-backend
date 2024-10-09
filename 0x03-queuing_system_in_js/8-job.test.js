import { expect } from 'chai';
import kue from 'kue';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    sinon.spy(queue, 'create'); // Mock the queue's create function
  });

  afterEach(() => {
    queue.create.restore(); // Restore the original method after each test
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.create.callCount).to.equal(2);  // Ensure two jobs were created
    expect(queue.create.firstCall.args[0]).to.equal('push_notification_code_3');
    expect(queue.create.firstCall.args[1]).to.deep.equal(jobs[0]);
    expect(queue.create.secondCall.args[0]).to.equal('push_notification_code_3');
    expect(queue.create.secondCall.args[1]).to.deep.equal(jobs[1]);
  });
});
