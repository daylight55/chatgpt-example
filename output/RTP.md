

# RTP
RTP(Real-time Transport Protocol)は、インターネット上でリアルタイム性のあるデータ（音声や動画など）の送受信を行うためのプロトコルである。
## 特徴
RTPは、通常のIPパケットに加えて、シーケンス番号やタイムスタンプなどの情報を付加して送信する。これらの情報を使用して、受信側でデータが破損していないかチェックしたり、データの順序を整理したりすることができる。また、RTPはユーザーエージェントに対してメディアの種類やフォーマットを指定するSDP(Session Description Protocol)と組み合わせて使用することもできる。
## 応用例
RTPは主に音声や動画の通話アプリケーションに使用される。SkypeなどのツールはRTPを使って通話を行っている。
## 注意点
RTP単体ではセキュリティ機能がなく、盗聴や改竄の危険がある。そのため、SRTP(Secure Real-time Transport Protocol)などの暗号化方式を併用することが一般的である。
## 関連用語
* SRTP:Secure Real-time Transport Protocol