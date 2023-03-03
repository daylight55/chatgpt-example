---
title: IPsec
---

# IPsec（Internet Protocol Security）
IPsecはインターネットプロトコルをセキュリティ対策するための暗号化技術である。

## 特徴
IPsecはIPパケットのセキュリティ対策を行うための様々な機能を備えている。  
また、IPv4とIPv6両方に対応している。  
通信内容の暗号化にはAES（Advanced Encryption Standard）やDES（Data Encryption Standard）などが使用される。  
また、認証にはRSA（Rivest–Shamir–Adleman）やDH（Diffie-Hellman key exchange）など様々な方式が使用される。  
これらの機能により、中間者攻撃・DoS攻撃・情報漏えいなどの脆弱性を大きく軽減することができる。

## 応用例 
VPN(Virtual Private Network)を利用する際に使用されることが多い。  
また、セキュリティ対策ソフトウェアの一部としても使用されている。  
例えば、トラフィックの通信内容を監視し、不正アクセスの場合はブロックする機能を備えているセキュリティソフトウェアであったり、特定の端末からの通信のみを許可するファイアウォールソフトウェアであったりする。 
 
## 注意点 
セキュリティ対策として効果的でありながらも、複雑な設定が必要となってしまうことが多いため注意が必要である。  

 
## 関連用語 
VPN(Virtual Private Network):仮想プライベートネットワーク  
AES(Advanced Encryption Standard):高度暗号化スタンダード   
DES(Data Encryption Standard):データ暗号化スタンダード    
RSA(Rivest–Shamir–Adleman):公開鍵暗号方式    
DH(Diffie-Hellman key exchange):差異ホラマン鍵交換