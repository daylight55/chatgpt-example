

# SYN
## 正称
SYNはTCP(Transmission Control Protocol)で使用されるフラグの一つで、コネクションの確立時に使用される。
## 特徴
SYNフラグは通信を開始する際に利用される。コネクションを確立するためには、通信相手先との通信経路が必要となり、このフラグは通信相手先を決定するために使用される。また、同時に通信相手先との通信経路が確認できていない場合、SYNフラグは利用できず、コネクションの確立もできない。
## 応用例
コネクションを確立したあとの通信ではSYNフラグは使用されない。コネクションの確立に成功した場合、SYNフラグはサーバーからクライアントへ返ってくる。このフラグをもつパケットを受信したクライアントは、サーバーとの通信経路が確認できていることを意味する。
## 注意点
- SYNフラグはコネクションの確立時にのみ使用されるため、通常の通信では利用されない。
- コネクションの確立に失敗した場合、SYNフラグは返ってこない。
- サーバーからクライアントへ返ってくるパケットにSYNフラグが付与されていない場合、コネクションの確立に失敗したことを意味する。
## 関連用語
- TCP(Transmission Control Protocol): データ転送を行う際に使用されるプロトコルの一つ。