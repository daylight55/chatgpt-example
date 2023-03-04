---
title: AC
---

# AC（アクセスコントロール）
正称はアクセスコントロール（Access Control）である。

## 特徴
ACは、情報へのアクセスを制限するための技術である。情報へのアクセスを制限することにより、悪意ある第三者からの情報漏えいを防止し、機密性・完全性・可用性などの観点からシステムの安全性を確保することができる。また、情報へのアクセスを制限することにより、特定の目的に適した使用者だけが情報にアクセスでき、情報が悪用されないようにすることもできる。
一般的なACは、認証（Authentication）と認可（Authorization）の2つの機能を備えている。認証はユーザーまたはコンピューターが自分自身を特定できるか否かを確認する機能であり、認可はユーザーまたはコンピューターがアクセス権限を持っているか否かを確認する機能である。


## 応用例
応用例としては、OSやWebサーバなどによく使われている。OSの場合、一般的なACはオペレーティングシステムがユーザーまたはプログラムに対してファイルシステム上のファイルやディレクトリに対するアクセス権限を与えられた上で動作させられていく仕組みとなっている。Webサーバの場合、通常はHTTPプロトコルに従って通信していく際にユーザー名とパスワードの組み合わせを送信し、サーバ側でパスワードの照合処理を行うことで認証された上で通信が行われていく仕組みとなっている。


## 注意点
ACの導入に伴う注意点としては、「バックドア」「ルート認証」「キャッシュポップ」「バッファオーバーフロー」「サイドチャネルアタック」「ディレクティブバッファインジェクション」「マルウェア」「ランタイムエラー」などが挙げられる。バックドアはAC導入前に事前に仕込んだものであり、通常の経路以外からも情報 systems. ルート認証 はOS上で動作す キャッシュポップ るプログラム に対し ディレクティブバッファインジェクション て特定の操作 マルウェア を 行う ランタイムエラ 事前 準備 が必要 サイドチャネルアタック に なっ たり バッファオーバーフロー し ます 。