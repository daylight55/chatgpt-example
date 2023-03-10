---
title: CIDR
---

#CIDR(Classless Inter-Domain Routing)
##特徴
CIDRはIPv4アドレスを効率的に使用するための方式である。  
CIDRでは、通常、IPv4アドレスの最初のバイトとそれに続くビット数を指定してアドレスブロックを割り当てられる。  
これは通常「アドレス/プレフィックス長」と呼ばれる。  
プレフィックス長は8ビット単位で指定され、0から31までの値を取る。  
例えば、192.0.2.0/24は192.0.2.0から192.0.2.255までの範囲を表す。  
このようなアドレスブロックの割り当て方法により、IPv4アドレス空間を効率的に使用することができる。  
また、CIDRによってルーティングテーブルサイズが大幅に削減され、ルーティングテーブルの検索も高速化される。  


##応用例
CIDRはRFC 1519「Classless Inter-Domain Routing in the Internet」によって提唱された。  
RFC 1519は1993年10月に制定された。  
CIDRの主な目的は、IPv4アドレスの空間を効率的に使用することだった。  
当時は、IPv4アドレスの空間が急速に枯渇していたため、CIDRが導入された。  


##注意点・関連用語
CIDRによって割り当てられたアドレスブロックの範囲を「プライベートネットワーク」と呼ぶこともある。