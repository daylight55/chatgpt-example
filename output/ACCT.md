---
title: ACCT
---

# ACCT（アカウンタビリティ）

## 特徴
ACCTは、コンピュータネットワークにおける資源の使用を監視するためのプロトコルである。TCP/IPモデルの4層目であるトランスポート層に位置し、アカウンタビリティを担う。また、ACCTは情報セキュリティの分野でも用いられており、システム利用者の行動を監視することができる。

## 応用例
ACCTを使用すると、ネットワーク上で誰がどのような動作をしていたかが把握できるため、不正な動作の場合はその情報を元に対策を講じることができる。また、利用状況に応じてネットワーク資源の配分を調整することも可能となる。

## 注意点
ACCTは通信内容に関する情報は保持しないため、不正アクセスの原因特定には向いていない。また、無効化されていない ACK によってセッションの途中から始まった通信もカウントされてしまうため注意が必要だ。

## 関連用語
- TCP/IPモデル:コンピュータネットワークの通信プロトコルのモデル。4層構造を持つ。トランスポート層は4層目であり、アカウンタビリティを担う。