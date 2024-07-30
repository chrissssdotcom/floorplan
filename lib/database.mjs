import config from '../config.mjs';
import pkg from 'mongodb';
const { MongoClient, ObjectId } = pkg;
const logger = console;

let client;
let db;

export const OID = function (objectIdOrHexString) {
    if (!objectIdOrHexString) {
        return null;
    } else if (objectIdOrHexString instanceof ObjectId) {
        return objectIdOrHexString;
    } else {
        return new ObjectId(objectIdOrHexString);
    }
};

export const connect = async () => {
    try {
        const uri = `mongodb://${config.dbHost}:${config.dbPort}`;
        client = new MongoClient(uri);
        await client.connect();
        db = client.db(config.dbName);
        logger.info('Connected to mongodb://%s:%d/%s.', config.dbHost, config.dbPort, config.dbName);
        return db;
    } catch (err) {
        logger.error('Failed to connect to database:', err);
        throw err;
    }
};

export const shutdown = async () => {
    if (client) {
        await client.close();
        logger.log('Shut down.');
    }
};

export const getDb = () => db;
