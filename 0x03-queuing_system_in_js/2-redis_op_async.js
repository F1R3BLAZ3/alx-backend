#!/usr/bin/node

import redis from 'redis';
import { promisify } from 'util';

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
 * Set the value for a given key in Redis.
 * @param {string} schoolName - The key name.
 * @param {string} value - The value to set.
 */
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

/**
 * Display the value for a given key in Redis.
 * @param {string} schoolName - The key name.
 */
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.error('Error:', err);
    }
}

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
