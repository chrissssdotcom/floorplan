import config from '../config.mjs';
import defaults from 'lodash-es/defaults.js';
import cors from 'cors';
import { connect as connectDatabase } from './database.mjs';
import express from 'express';
import http from 'http';
import path from 'path';
import slash from 'express-slash';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

defaults(config, {
    wwwPort: 3000,
    dbHost: '127.0.0.1',
    dbPort: 27017,
    dbName: 'floorplan',
    mountPoint: '/'
});

config.mountPoint = config.mountPoint.replace(/\/+$/, '');

// Define __dirname for ES module scope
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

await connectDatabase();

const server = express();
export default server;
const publicDir = path.join(__dirname, '../public');

server.set('env', 'production');
server.set('port', config.wwwPort);
server.set('views', path.join(__dirname, '../views'));
server.set('view engine', 'hbs');
server.enable('strict routing');
server.use(express.compress());
server.use(config.mountPoint, express.favicon('public/favicon.ico'));
server.use(express.logger());
server.use(express.bodyParser());
server.use(cors());
server.use(config.mountPoint, server.router);
server.use(config.mountPoint, slash());
server.use((err, req, res, next) => {
    console.error(err.stack || err.message);
    res.type('text');
    res.send(500, err.message);
});

const lessMiddlewareModule = await import('less-middleware');
const lessMiddleware = lessMiddlewareModule.default || lessMiddlewareModule;
server.use(config.mountPoint, lessMiddleware({ src: publicDir }));

server.use(config.mountPoint, express.static(publicDir, { maxAge: 4 * 60 * 60 * 1000 }));
server.use(config.mountPoint, (req, res, next) => {
    if (/^\/photos\/[0-9a-f]+\.jpg$/.test(req.path)) {
        res.redirect('/images/missing_photo.jpg');
    } else {
        console.log(404, req.path);
        next();
    }
});

// Add a basic route for testing
server.get('/test', (req, res) => {
    res.send('Hello, world!');
});

http.createServer(server).listen(server.get('port'), () => {
    console.log('Listening on http://*:%d%s', server.get('port'), config.mountPoint);
});
