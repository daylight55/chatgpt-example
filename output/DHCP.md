

# DHCP（Dynamic Host Configuration Protocol）
DHCPはIPアドレスなどのネットワーク接続に関する情報を動的に割り当てるプロトコルである。
DHCPサーバーからクライアントに対してアドレスなどの情報を割り当て、クライアントはその情報を使用してネットワーク接続を行う。

## 特徴
DHCPはIPv4やIPv6のアドレス割り当てに加え、DNSサーバーやデフォルトゲートウェイなどの経路情報の割り当ても行うことができる。また、DHCPクライアントはDHCPサーバーから割り当てられた情報を自動的に更新することができるため、DHCPサーバーの稼働状況に応じて動的にIPアドレスなどの情報を変更することができる。

## 応用例
DHCPはパソコンやスマートフォンなどのネットワークデバイスに対して動的にIPアドレスを割り当てることができるため、企業内LANなどで広く利用されている。また、Wi-Fiルーターなどの家庭用ネットワーク機器でもDHCPを利用している例が多い。

## 注意点
DHCPサーバーが稼働していないとネットワーク接続はできないため、注意が必要だ。また、DHCPサーバーからIPアドレスの割り当て規則（マスクやデフォルトゲートウェイ）を変更することもできるが、クライアントの設定と相違が生じると予期しない動作をする可能性があるため注意が必要だ。


## 関連用語
* ネットワークマスク（Subnet Mask）: ネットワーク上の通信方式を定義するビットマスクのこと。IPv4では32ビットから成り、主に8ビット単位で「0」「1」「255」の3パターンから成っている。