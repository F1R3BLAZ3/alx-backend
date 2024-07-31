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

// Subscribe to the channel
client.subscribe('holberton school channel');

// Event handler for receiving messages
client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
});
