---
title: DHCP
---

# DHCP(Dynamic Host Configuration Protocol)
DHCPはIPアドレスを動的に割り当て、管理するためのプロトコルである。

## 特徴
DHCPサーバーはクライアントからの要求に応じて、クライアントに対して一時的なIPアドレスを割り当てる。クライアントはDHCPサーバーから受信した情報を使用してネットワークに接続する。DHCPクライアントは、サーバーからIPアドレスの割り当て要求を行うためにUDPポート67番を使用する。DHCPサーバーは、クライアントからの要求に応じてUDPポート68番を使用してIPアドレスを送信する。

## 応用例
DHCPサーバーはLAN内のすべてのデバイスに対して動的なIPアドレスの割り当てを行うことができる。これにより、LAN内のデバイスの構成が簡単になり、ネットワーク管理が容易になる。また、DHCPサーバーは複数のLANセグメントを持つこともできる。これにより、大規模なネットワークの管理が可能となる。

## 注意点
DHCPサーバーは常時起動し続ける必要があるため、高いセキュリティレベルが必要となる。また、DHCPサーバーはネットワーク上で正常に動作するために正確な設定が必要となる。誤った設定により、ネットワーク上の通信が不安定になったり、エラーが発生したりする可能性があるため注意が必要である。

## 関連用語
* IPアドレス：コンピュータやネットワークデバイスを特定するための番号
* UDP：User Datagram Protocolの略で、IPパケットの送受信方式の1つ