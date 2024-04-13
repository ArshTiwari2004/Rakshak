import express from 'express';
import dotenv from 'dotenv';
import router from './src/routes/index.routes.js';

const app = express()
dotenv.config();

const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.use('/api', router);

app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}! 🚀 -> http://localhost:4000/`);
});
