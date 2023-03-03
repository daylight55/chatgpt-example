---
title: RTSP
---

# RTSP
## 正称
RTSPはReal Time Streaming Protocolの略である。
## 特徴
ストリーミングデータを再生するためのプロトコルである。音声・動画・3Dグラフィックなどのリアルタイム性のあるデータを転送する際に使用される。TCPやUDPを使用している。
## 応用例
配信動画サービス、ライブ放送、音声通話などで使用されている。
## 注意点
セキュリティ上の問題からSIP(Session Initiation Protocol)と合わせて使うことが多い。また、NAT(Network Address Translation)の設定が必要となる場合もある。
## 関連用語
- TCP: Transmission Control Protocol  通信範囲を特定し two way communication をするプロトコルであり、Internet などの通信網において最も重要な役割を果たしている。IP によってホスト間の通信経路が決まった後、TCP によってホスト間の通信手順が決まります。TCP は全てのアプリケーションに対応しています。HTTP(Webブラウザ) や SMTP(メールソフト) などは TCP/IP プロトコルを利用したアプリケーションです。 
- UDP: User Datagram Protocol  UDPはTransmission Control Protocol(TCP)とは異なり、コネクションレス型の通信プロトコルです。UDPはパケット単位でデータを送受信するため、速度が遅くなりがちです。UDPはTCPより軽量なため、エコー機能などの必要のないアプリケーションに適しています。 　　 　  　  　  　  　  　  　  　  　    - NAT（Network Address Translation）：NATは「ネットワークアドレス変換」の意味であり、一般的にインターネットを利用する企業内LAN内部からインターネットにアクセスさせる際に利用されます。NATは複数のLAN内部からインターネットにアクセスさせた場合に有効となります。NATの場合はパソコン1台1台に固定IPアドレスを割り当てる必要が無く、LAN内にあるパソコンからインターネット経由でデータの送受信が行えます。