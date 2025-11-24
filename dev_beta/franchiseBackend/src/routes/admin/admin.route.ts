import { Hono } from 'hono';
const adminRouter = new Hono();
import userRouter from './users.route';

// Admin routes
adminRouter.route('/users', userRouter);

export default adminRouter;
