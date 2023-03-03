---
title: RDATA
---

# RDATAとは
RDATAはDNSのメッセージの一部である。
DNSのメッセージは、クエリ(Q)とレスポンス(R)の2種類があり、RDATAはレスポンスのメッセージに含まれる。
RDATAは応答に対する追加情報を提供する。
RDATAフィールドの形式は、レコードタイプ(A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, TXTなど)によって異なる。


## 特徴
RDATAフィールドの形式は、レコードタイプ(A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, TXTなど)によって異なる。
各レコードタイプで使用されるビット数も異なるため、詳細なフォーマットはRFC1035「Domain names - implementation and specification」などを参照してください。


## 応用例
- A レコード：IPv4 アドレスを表す。IPv4 アドレスを含む 4 バイトのデータ。
- AAAA レコード：IPv6 アドレスを表す。IPv6 アドレスを含む 16 バイトのデータ。
- CNAME レコード：別の名前を表すalias情報を持つ。別の名前を指定するために使用されるドメイン名。


## 注意点
- RDATAフィールドの形式は、レコードタイプ(A, AAAA, CNAME, MX, NS, PTR, SOA, SRV, TXTなど)によって異なるため、詳細なフォーマットはRFC1035「Domain names - implementation and specification」などを参照してください。




## 関連用語
- DNS: Domain Name Systemの略で、インターネット上の各コンピュータの通信方法の決定規則であるプロトコルである。