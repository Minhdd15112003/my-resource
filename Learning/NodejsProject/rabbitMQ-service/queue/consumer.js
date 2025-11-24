const amqplib = require('amqplib');

const amqb_url_cloud = 'amqps://vpmvnyoa:IWC7G8XGHUNoeCdGb4BGhKkSd_AJNkED@fuji.lmq.cloudamqp.com/vpmvnyoa';
const amqb_url_docker = 'amqp://rabbitmq:L3GATmHKeWnbeD7S@0.0.0.0:5672';

const receiveSend = async () => {
    try {
        const conn = await amqplib.connect(amqb_url_docker);
        //tạo channel
        const channel = await conn.createChannel();
        //tạo queue
        const nameQueue = 'q2';

        //assertQueue để tạo queue
        await channel.assertQueue(nameQueue, {
            durable: true, //queue sẽ tồn tại sau khi rabbitmq restart
        });

        //receive message
        await channel.consume(
            nameQueue,
            (msg) => {
                console.log('Received message:', msg.content.toString());
            },
            {
                noAck: true,
                //nếu true thì sau khi nhận message sẽ tự động xóa message đó
                //false thì phải xác nhận đã nhận message
            },
        );

        // //đóng kết nối
        // await channel.close();
    } catch (error) {
        console.log('Error in producer.js:', error);
    }
};

receiveSend();
