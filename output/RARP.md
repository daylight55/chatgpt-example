

# RARP(Reverse Address Resolution Protocol)
## 正称
Reverse Address Resolution Protocol（リバースアドレス解決プロトコル）は、OSI参照モデルでいうところのトランスポート層にあたるものである。
## 特徴
IPアドレスをMACアドレスに変換するプロトコルである。通常のARPはMACアドレスからIPアドレスを調べるが、RARPはIPアドレスからMACアドレスを調べる。RARPはIPv4専用であり、IPv6専用のプロトコルとしてNDPが存在する。
## 応用例
RARPを使うことで、IPv4アドレスを割り当てられたマシンの電源を入れたときに自動的にインターネットに接続することができる。
## 注意点
RARPはセキュリティ上の問題が多く存在しているため、最近では使われなくなっている。代わりにBOOTPやDHCPを使うことが多い。
## 関連用語
- ARP：Address Resolution Protocol（アドレス解決プロトコル）の略称。MACアドレスからIPアドレスを調べるプロトコル。OSI参照モデルでいうところのネットワーク層にあたるものである。
- DHCP：Dynamic Host Configuration Protocolの略称。動的にIPアドレス・サブネットマスク・デフォルトゲートウェイ・DNSサーバーなどを割り当てられたマシンの電源を入れたときに自動的にインターネットに接続することができるプロトコル。OSI参照モデルでいうところのアプリケーション層にあたるものであり、TCP/UDP上で動作する。