---
title: L2TP
---

# L2TP（Layer 2 Tunneling Protocol）
## 特徴
L2TPは、IPv4で導入されたプロトコルである。IPv6にも対応している。
L2TPは、IPネットワーク上でユーザー・コンピュータ間の通信を行う際に、二つのネットワーク層（データリンク層とネットワーク層）をトunnelingすることでセキュリティを高めるものである。
また、L2TPはセキュリティ機能を強化するためにIPSecプロトコルと組み合わせて使用することができる。
## 応用例
L2TPは、VPN（Virtual Private Network）接続などに使用されることが多い。
VPNとは、企業内部の通信システムをインターネット経由で拠点間で共有するシステムのことだ。
企業内部の通信システムをインターネットを通して拠点間で共有することで、遠隔地にある拠点の間の通信コストを削減し、効率的なコミュニケーションを実現する。
VPNの接続方式には「リモートアクセス VPN」「サイト間 VPN」の2種類があり、L2TPはサイト間 VPNの接続方式の1つとして広く使用されている。
## 注意点
- L2TP/IPSecパッケージが必要  
- ポート1701 UDPが解放されていないと接続できない  
  - ファイヤウォール設定が必要  
- NAT設定が必要  
  - NAT Traversal（NATトラバーサル）機能が必要  
- 認証方式  
  - PAP(Password Authentication Protocol)  
  - CHAP(Challenge Handshake Authentication Protocol)  

















  ## 関連用語