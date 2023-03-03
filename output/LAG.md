

# LAG（Link Aggregation）
## 正称
LAG、Link Aggregation、リンクアグリゲーション
## 特徴
通常、LANを構成する際には単一の物理リンクで通信を行います。しかし、LAGを用いることで複数の物理リンクを1つの仮想リンクのように扱うことができます。これにより、物理リンクの帯域幅の合計分の通信を行うことができます。また、通信中に物理リンクが切断された場合でも、接続されている他の物理リンクを使用して通信を継続することができます。

## 応用例
- イーサネットフレームの転送方式として最も一般的なIEEE 802.3adによって実現される
- ネットワークスイッチ間の通信路として使用される場合がある
- ネットワークアダプタ間の通信路として使用される場合がある
- ゲートウェイ間の通信路として使用される場合がある
- ロードバランサー間の通信路として使用される場合がある


## 注意点
- LAGは必ず連携機能を備えたデバイス同士で構成する必要があります。連携機能のないデバイス間ではLAGは構成できません。
- LAGの構成にはテクノロジーによって異なります。IEEE 802.3adなどの規格に従ったLAGは互換性があります。一方でベンダー固有のLAGも存在します。この場合はベンダー間の互換性はなく、接続するデバイスもベンダー固有のものに限られます。

 
## 関連用語
- スループット：単位時間あたりの送受信できたデータ量