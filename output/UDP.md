

# UDP
UDP（User Datagram Protocol）は、IPネットワーク上でアプリケーション間でメッセージをやりとりするためのプロトコルである。TCPとは異なり、コネクションレス型であるため、通信開始から終了までの手続きが不要で、速度が速い。

## 特徴
- コネクションレス型プロトコル
- 通信開始から終了までの手続きが不要
- 速度が速い
- データグラム方式（パケット方式）であるため、データの順序は保証されない。また、パケットの到達も保証されない。
- そのため、必ず順序や到達を確認しなければいけないアプリケーションには向かない。例えばファイル転送ソフトウェアはTCPを使う。一方、音声伝送ソフトウェアはUDPを使うことが多い。音声伝送においてはパケットの順番は重要ではなく、一部のパケットが欠落しても問題にならないためだ。


## 応用例
UDPを使ってアプリケーション間メッセージをやり取りする際に使用される応用例として以下のものが挙げられる。
- DNS（Domain Name System）サーバーとクライアント間の通信
- NTP（Network Time Protocol）サーバーとクライアント間の通信

 
## 注意点・エラー処理方法
UDPには以下の注意点・エラー処理方法が挙げられる。 　  

 - データグラム方式（パケット方式）であるため、データの順序は保証されない。また、パケットの到達も保証されない。 　  

 - そのため、必ず順序や到達を確認しなければいけないアプリケーションには向かない。例えばファイル転送ソフトウェアはTCPを使う。一方、音声伝送ソフトウェアはUDPを使うことが多い。音声伝送においてはパケットの順番は重要ではなく、一部のパケットが欠落しても問題にならないためだ。 　  

 - UDPチェックサム機能によってエラーパケットを検出し削除することが可能だが、この機能 is はOSによって有効無効が異なってきており 、またチェックサム機能自体もコードレベルで実装する必要があるため 　  

 - 実装者にとって扱うことが難しくエラーハンドリングも困難だ。 　  

 - またUDPヘッダのチェックサム機能の無効化オプションも存在するため 　   

 - セキュリティ上の懸念もある。 　  

 - TCP/IPスタックの実装者の多くはUDPチェックサム機能の無効化オプションを有効化してしまっている傾向にあるため注意する必要がある 　  

   
## 関連用語
TCP,IP,NTP,DNS