---
title: CPPM
---

#CPPM(Carrier-sense Time-division Multiple Access with Collision Prevention)
##特徴
CPPMは、キャリアセンスタイム分割マルチプレクサ(CSMA/CD)を拡張したネットワークです。パケットのやり取りに際して、送信機は相手の受信機が空いているかどうかを確認する必要があります。これによって、衝突を防止します。

##応用例
CPPMは、IEEE 802.3 Ethernetの一部として使用されています。

##注意点
CPPMは、通信路上に他の通信がなくても動作します。他の通信と競合しないため、帯域幅を効率的に使用できます。ただし、1つの受信機に対して複数の送信機から同時にパケットを送信できるため、帯域幅の利用率はあまり上がりません。

##関連用語
- キャリアセンスタイム分割マルチプレクサ(CSMA/CD): CPPMの拡張であるEthernetのネットワークで使われているプロトコル