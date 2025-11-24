const amqplib = require('amqplib');

const amqb_url_docker = 'amqp://rabbitmq:L3GATmHKeWnbeD7S@0.0.0.0:5672';

const receive = async () => {
  try {
    const conn = await amqplib.connect(amqb_url_docker);
    //tạo channel để gửi message
    const channel = await conn.createChannel();

    //tao exchange
    const nameExchange = `exchange1`;
    await channel.assertExchange(nameExchange, 'fanout', {
      durable: false,
    });
    // create queue
    const { queue } = await channel.assertQueue('', {
      durable: false, // queue sẽ không tồn tại sau khi rabbitmq restart
      exclusive: true, // queue sẽ tự động xóa sau khi consumer disconnect
    });
    console.log('queue:', queue);

    //bind queue là để kết nối queue với exchange
    await channel.bindQueue(queue, nameExchange, '');

    await channel.consume(
      queue,
      (msg) => {
        console.log('Received message:', msg.content.toString());
      },
      {
        noAck: true,
      },
    );
  } catch (error) {
    console.log('Error in producer.js:', error);
  }
};
const msg = process.argv[2] || 'Hello World';
receive();
