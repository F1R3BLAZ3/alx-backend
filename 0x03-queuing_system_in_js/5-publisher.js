#!/usr/bin/node

import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event handler for successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Event handler for connection error
client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.message);
});

/**
 * Publish a message to a channel after a specified time.
 * @param {string} message - The message to publish.
 * @param {number} time - The time in milliseconds to wait before publishing the message.
 */
function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish('holberton school channel', message);
    }, time);
}

// Call the function with the specified messages and times
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
