---
title: L2SW
---

# L2SWとは
L2SWはLayer2スイッチのことを指します。  
物理的な接続を仮想的なポートに変換し、通信を行うことができます。  
ポート数は8ポートから52ポート程度で、最近では100ポート以上のものもあります。  
OSPFなどのルーティングプロトコルは動作しませんが、VLANやSTP(スパニングツリープロトコル)などの基本的な機能はサポートされています。  
1台のスイッチに複数の物理LANカードを搭載して1つの仮想スイッチとして動作させることもできます。


## 特徴
- ネットワーク機器に物理的なLANポートを用意する必要がなく、コスト削減に貢献できる
- 複数の物理LANカードを1台のスイッチとして動作させることができるため、高い拡張性を誇る


## 応用例
- LAN内の通信路を分離したい場合やセキュリティ対策に用いられることが多い


## 注意点
- ルーティングプロトコルはサポートされていないため、異なるセグメント間の通信はできない


## 関連用語
- LAN：Local Area Networkの略。同一セグメント内の通信路のこと