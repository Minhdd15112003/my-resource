const amqplib = require('amqplib');

const amqb_url_docker = 'amqp://rabbitmq:L3GATmHKeWnbeD7S@0.0.0.0:5672';

const receive = async () => {
    try {
        const conn = await amqplib.connect(amqb_url_docker);
        //tạo channel để gửi message
        const channel = await conn.createChannel();

        //create queue
        const nameExchange = `exchangeTopic`;
        await channel.assertExchange(nameExchange, 'topic', {
            durable: false,
        });

        const { queue } = await channel.assertQueue('', {
            durable: false,
            exclusive: true,
        });
        /* 
        * có nghĩa là phù hợp với bất kỳ routingKey nào
        # phù hợp với một từ hoặc không từ nào trong routingKey
        */
        const topics = process.argv.slice(2);

        topics.forEach(async (key) => {
            await channel.bindQueue(queue, nameExchange, key);
        });

        console.log(`Waiting for messages in queue: ${queue}`);
        console.log('Listening to topics:', topics);

        await channel.consume(
            queue,
            (msg) => {
                console.log(`Received message: ${msg.content.toString()} with topic: ${msg.fields.routingKey}`);
            },
            {
                noAck: true,
            },
        );
    } catch (error) {
        console.log('Error in producer.js:', error);
    }
};

receive();
