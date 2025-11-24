const express = require('express');
const crypto = require('crypto');
const app = express();
const port = 4000;

// KHÓA BÍ MẬT CHIA SẺ VỚI COTURN SERVER (PHẢI GIỐNG HỆT NHƯ TRONG turnserver.conf)
const SHARED_SECRET_KEY = '32KYEjVARXwbdd5JkwBYCydRLjcKX3R4vUwvAGB7d9Uu0VbNfm'; // Thay thế bằng khóa thật của bạn

app.use(express.json()); // Để đọc body JSON nếu cần

app.get('/get-turn-credentials', (req, res) => {
  // Thời gian hết hạn của credential (ví dụ: 10 phút = 600 giây)
  const TTL = 600; // Time To Live in seconds
  const unixTimestamp = Math.floor(Date.now() / 1000) + TTL; // Thời gian hết hạn tính bằng giây UTC

  // `username` phải có định dạng `timestamp:some_unique_string`
  // `some_unique_string` có thể là ID người dùng, ID phiên, hoặc một chuỗi ngẫu nhiên.
  // Dùng ID người dùng/ID phiên để bạn có thể theo dõi.
  const userId = req.query.userId || 'guest' + Math.random().toString(36).substring(2, 8);
  const turnUsername = `${unixTimestamp}:${userId}`;

  // Tính toán credential (mật khẩu) bằng HMAC-SHA1
  const hmac = crypto.createHmac('sha1', SHARED_SECRET_KEY);
  hmac.update(turnUsername);
  const turnPassword = hmac.digest('base64');

  // Cấu hình ICE servers mà client sẽ sử dụng
  const iceServers = [
    {
      urls: 'stun:stun.l.google.com:19302', // STUN server của Google
    },
    {
      urls: `turn:34.126.102.198:3478`, // Hoặc turn:YOUR_PUBLIC_IP:3478
      username: turnUsername,
      credential: turnPassword,
    },
    {
      urls: `turns:34.126.102.198:5349?transport=tcp`, // Hoặc turns:YOUR_PUBLIC_IP:5349?transport=tcp
      username: turnUsername,
      credential: turnPassword,
    },
    // Thêm các TURN server khác nếu có (ví dụ: TURN server 2)
  ];

  res.json({ iceServers });
});

app.listen(port, () => {
  console.log(`Backend API listening at http://localhost:${port}`);
});
