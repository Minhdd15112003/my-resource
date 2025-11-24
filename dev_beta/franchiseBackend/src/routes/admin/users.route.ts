import { Hono } from 'hono';

const userRouter = new Hono();
userRouter
  .get('/', (c) => {
    return c.json({ message: 'List of users' });
  })
  .post('/', (c) => {
    return c.json({ message: 'User created' });
  })
  .get('/:id', (c) => {
    const id = c.req.param('id');
    return c.json({ message: `User details for ID: ${id}` });
  })
  .put('/:id', (c) => {
    const id = c.req.param('id');
    return c.json({ message: `User updated for ID: ${id}` });
  })
  .delete('/:id', (c) => {
    const id = c.req.param('id');
    return c.json({ message: `User deleted for ID: ${id}` });
  });

export default userRouter;
