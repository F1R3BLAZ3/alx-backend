import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Start tracking progress at 0%

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`)); // Fail the job
  }

  job.progress(50, 100); // Progress to 50%
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done(); // Job completed
}

// Create a queue
const queue = kue.createQueue();

// Process the jobs in the queue 'push_notification_code_2', with two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
