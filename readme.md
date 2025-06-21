# VeriPass System Flow
1. Admin registers user with roles (students,teachers).
2. Each student is issued a permanent QR code (one-time generation).
3. Admin or teacher will create a session.
4. During session student will scan the qr code .
5. Server dont process it immediately . Instead, pushes scan record to RabbitMQ queue .
6. After session ends celery consumes RabbitMQ . Decrypts qr_token , validates it and marks attendance .Sends mail to student .
