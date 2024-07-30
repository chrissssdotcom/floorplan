import path from 'path';
import fs from 'fs/promises';
import zipObject from 'lodash-es/zipObject.js';
import server from '../lib/server.mjs';
import config from '../config.mjs';

let OFFICE_IDS = [];

const initializeRoutes = async () => {
    const MAPS_PATH = path.join(server.get('views'), 'maps');

    try {
        const files = await fs.readdir(MAPS_PATH);
        OFFICE_IDS = files.map(filename => path.basename(filename, '.svg'));
    } catch (err) {
        console.error('Error reading maps directory:', err);
        process.exit(1);
    }

    const renderAdmin = function (req, res, next) {
        const svgReadPromises = OFFICE_IDS.map(officeId => {
            const svgPath = path.join(MAPS_PATH, `${officeId}.svg`);
            return fs.readFile(svgPath, 'utf8');
        });

        Promise.all(svgReadPromises)
            .then(svgs => {
                const svgMap = zipObject(OFFICE_IDS, svgs);

                const context = {
                    svgs: svgMap,
                    config: JSON.stringify({
                        mountPoint: config.mountPoint
                    })
                };
                res.render('admin', context);
            }).catch(next);
    };

    server.get('/admin/', renderAdmin);
    server.get('/admin/:id', renderAdmin);
};

export default initializeRoutes;
