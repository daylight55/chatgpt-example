

# PPTP(Point-to-Point Tunneling Protocol)
## 正称
PPP(Point-to-Point Protocol)をトンネル化したプロトコルである。  
## 特徴
IPパケットのフラグメント化を回避するために、TCPヘッダーのオプションフィールドを省略している。  
また、PPPフレーム内にIPパケットを入れ込む際には、IPパケットのヘッダー情報を圧縮して送信できるようになっている。  
さらに、セキュリティ対策も施されており、認証方式としてMS-CHAPv2が採用されている。  
## 応用例
VPN(Virtual Private Network)の構築に利用されることが多い。  
また、企業内LANの通信をインターネット経由で安全かつ簡単に行うことができるため、企業間の通信手段としても利用されることがある。  
## 注意点
セキュリティ上の問題から使用すべきではないと考えられている。  
特にMS-CHAPv2の脆弱性からクラックすることが容易であり、セキュリティ上危険な問題が多く指摘されている。  
## 関連用語
VPN(Virtual Private Network): インターネット上を仮想的なプライベートネットワークとして利用することができるサービス