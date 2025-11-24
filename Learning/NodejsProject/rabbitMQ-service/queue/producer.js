const amqplib = require('amqplib');

const amqb_url_cloud = 'amqps://vpmvnyoa:IWC7G8XGHUNoeCdGb4BGhKkSd_AJNkED@fuji.lmq.cloudamqp.com/vpmvnyoa';
const amqb_url_docker = 'amqp://rabbitmq:L3GATmHKeWnbeD7S@0.0.0.0:5672';

const send = async ({ msq }) => {
    try {
        const conn = await amqplib.connect(amqb_url_docker);
        //tạo channel
        const channel = await conn.createChannel();
        //tạo queue
        const nameQueue = 'q2';

        await channel.assertQueue(nameQueue, {
            durable: true,
        });
        //gửi message qua queue
        await channel.sendToQueue(
            nameQueue,
            Buffer.from(msq),
            {
                expiration: '10000', //TTL time to live (miliseconds)
            },
            {
                persistent: true, //message sẽ không bị mất khi rabbitmq restart
            },
        );
    } catch (error) {
        console.log('Error in producer.js:', error);
    }
};
const msg = process.argv.slice(2).join(' '); //lấy message từ command line

send({ msq: msg });
