function createPushNotificationsJobs(jobs, queue) {
    // Check if the jobs argument is an array
    if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
    }
  
    // Iterate over each job in the jobs array
    jobs.forEach((jobData) => {
      const job = queue.create('push_notification_code_3', jobData)
        .save((err) => {
          if (!err) {
            console.log(`Notification job created: ${job.id}`);
          }
        });
  
      // Job completion handler
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });
  
      // Job failure handler
      job.on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      });
  
      // Job progress handler
      job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    });
  }
  
  export default createPushNotificationsJobs;
  