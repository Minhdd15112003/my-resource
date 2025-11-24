const amqplib = require('amqplib');

const amqb_url_docker = 'amqp://rabbitmq:L3GATmHKeWnbeD7S@0.0.0.0:5672';

const post = async ({ msg }) => {
    try {
        const conn = await amqplib.connect(amqb_url_docker);
        //tạo channel để gửi message
        const channel = await conn.createChannel();

        //tao exchange
        const nameExchange = `exchange1`;
        await channel.assertExchange(nameExchange, 'fanout', {
            durable: false,
        });
        //fanout: gửi message đến tất cả các queue đã bind với exchange
        //direct: gửi message đến queue có routingKey giống với routingKey của message
        //topic: gửi message đến queue có routingKey match với routingKey của message
        //headers: gửi message đến queue có header giống với header của message

        // publish message
        await channel.publish(nameExchange, '', Buffer.from(msg));
        console.log('Sent message:', msg);

        setTimeout(() => {
            conn.close();
            process.exit(0);
        }, 2000);
    } catch (error) {
        console.log('Error in producer.js:', error);
    }
};
const msg = process.argv[2] || 'Hello World';
post({ msg });
