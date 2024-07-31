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
 * Create a hash with multiple fields.
 */
function createHash() {
    const hashKey = 'HolbertonSchools';
    const schools = {
        Portland: '50',
        Seattle: '80',
        NewYork: '20',
        Bogota: '20',
        Cali: '40',
        Paris: '2'
    };

    for (const [field, value] of Object.entries(schools)) {
        client.hset(hashKey, field, value, redis.print);
    }
}

/**
 * Display the entire hash.
 */
function displayHash() {
    client.hgetall('HolbertonSchools', (err, reply) => {
        if (err) {
            console.error('Error:', err);
        } else {
            console.log(reply);
        }
    });
}

// Create the hash and then display it
createHash();
displayHash();
