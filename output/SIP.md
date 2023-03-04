---
title: SIP
---


# SIP（Session Initiation Protocol）
SIPはコンピュータネットワーク上で通信セッションを初期化するためのアプリケーション層プロトコルである。
SIPはRFC3261によって定義されている。
## 特徴
SIPは以下の特徴を持つ。
- クライアントサーバモデルを採用している。クライアントからサーバへリクエストメッセージを送信し、サーバからレスポンスメッセージを返す。
- プロキシサーバ機能を持つ。プロキシサーバは、クライアントからの通信要求を受信し、目的のユーザに転送する役割を果たす。また、応答メッセージも同様に処理する。
- リダイレクトサーバ機能を持つ。リダイレクトサーバは、要求メッセージの受信者が存在しない場合に、別の場所に転送する役割を果たす。
- ルータ機能を持つ。ルータは、要求メッセージの送り先が自分のネットワーク内に存在しない場合に、別のネットワーク経由で転送する役割を果たす。
## 応用例
SIPは以下の応用例がある。
- VoIP（Voice over IP）
- ビデオ会議システムなどのマルチメディア通信システム
- プロキシ呼び出し（Proxy Call）などの電話応答システム
## 注意点
SIPは以下の注意点がある。
- UDPやTCPなどのTransport Layerで動作するため、NAT（Network Address Translation）やファイヤウォールの設定が必要となる場合がある。また、NATやファイヤウォールでブロックされてしまうとSIPの通信ができなくなってしまうこともあるため注意が必要である。