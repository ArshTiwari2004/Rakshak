import express from 'express';
import { outgoingScan, incomingScan, getDetails } from '../../controllers/inventory.controllers.js';

const router = express.Router();

router.route('/outgoing/').post(outgoingScan);
router.route('/incoming/').post(incomingScan);
router.route('/getDetails/').post(getDetails);

export default router;
