const amqplib = require('amqplib');

const amqb_url_docker = 'amqp://rabbitmq:L3GATmHKeWnbeD7S@0.0.0.0:5672';

const post = async () => {
    try {
        const conn = await amqplib.connect(amqb_url_docker);
        //tạo channel để gửi message
        const channel = await conn.createChannel();

        //tao exchange
        const nameExchange = `exchangeTopic`;
        await channel.assertExchange(nameExchange, 'topic', {
            durable: false,
        });
        //fanout: gửi message đến tất cả các queue đã bind với exchange
        //direct: gửi message đến queue có routingKey giống với routingKey của message
        //topic: gửi message đến queue có routingKey match với routingKey của message
        //headers: gửi message đến queue có header giống với header của message

        // publish message
        const args = process.argv.slice(2);
        const msg = args[1] || 'Fixed message';
        const topic = args[0] || 'anonymous.info';
        console.log('topic:', topic, 'msg:', msg);

        await channel.publish(nameExchange, topic, Buffer.from(msg));
        console.log('Sent message:', msg);

        setTimeout(() => {
            conn.close();
            process.exit(0);
        }, 5000);
    } catch (error) {
        console.log('Error in producer.js:', error);
    }
};

post();
