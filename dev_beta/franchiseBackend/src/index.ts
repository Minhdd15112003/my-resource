import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';
import { serveStatic } from 'hono/bun';
import { prettyJSON } from 'hono/pretty-json';
import { csrf } from 'hono/csrf';
import { languageDetector } from 'hono/language';
import adminRouter from './routes/admin/admin.route';
import { HTTPException } from 'hono/http-exception';
import { env } from 'hono/adapter';
import { ENV } from './configs/env.config';
import { io, Socket } from 'socket.io-client';

const app = new Hono().basePath('/api/v1');

// Middleware
app.use(prettyJSON());
app.use('/public/*', serveStatic({ root: './' }));
app.use(logger());
app.use('/api/*', cors()); // Cho phép CORS
app.use(csrf()); // CSRF protection

const ioClient = io('http://localhost:4444');

ioClient.on('connect', () => {
  console.log('Socket.IO client connected');
});

ioClient.on('disconnect', () => {
  console.log('Socket.IO client disconnected');
});

app.route('/admin', adminRouter);
app.get('/', (c) => {
  return c.json({ message: 'Welcome to the API' + env(c).PORT }, 200);
});

app.onError((err, c) => {
  console.error(err);
  if (err instanceof HTTPException) {
    return c.json({ message: err.message, status: err.status }, err.status);
  }
  return c.json({ message: 'Internal Server Error' }, 500);
});

app.notFound((c) => {
  return c.json({ message: 'Not Found' }, 404);
});

export default {
  port: ENV.PORT,
  fetch: app.fetch,
};
