

# DHCP（Dynamic Host Configuration Protocol）
DHCPはIPアドレスやサブネットマスクなど、コンピューターのネットワーク接続に必要な設定情報を動的に割り当てるプロトコルである。
DHCPサーバからクライアントへ情報を割り当てる際に使用する。

## 特徴
DHCPはIPv4とIPv6両方に対応している。また、OSにも依存しないため様々なOSで利用可能である。

## 応用例
DHCPはインターネット接続を行う際に使用されることが多い。ISPから固定IPアドレスを取得する場合でもDHCPを利用することがある。また、Wi-FiルーターなどのLAN内部でもDHCPサーバを立てられるため、LAN内の機器の自動的なIPアドレスの割り当てに利用できる。

## 注意点
DHCPサーバがダウンしていた場合、DHCPクライアントは正常に動作しなくなってしまうため注意が必要である。また、セキュリティ上の理由からLAN内部のDHCPサーバは非推奨とされていることもある。

## 関連用語
* DHCPクライアント：DHCPサーバから情報を受信するコンピューターのこと。通常はパソコンやスマートフォンなどの端末機器がDHCPクライアントとなっている。 
* DHCPサーバ：DHCPクライアントへ情報を割り当てるコンピューターのこと。ISPのルーターや企業内LANの場合、専用機器を設置したりソフトウェアを導入すればDHCPサーバとして動作させられる。