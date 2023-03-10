---
title: VRRP
---

#VRRP（Virtual Router Redundancy Protocol）
##特徴
VRRPはOSPFやBGPなどのルーティングプロトコルとは異なり、複数のルータをバックアップするために使用される。VRRPはRFC 3768で規定されている。

VRRPでは「バックアップ」と呼ばれる仮想的なルータを構成することができ、通常のルータに比べてフェイルオーバーの時間を短縮することができる。また、バックアップルータを構成する際にはIPアドレスの冗長化も可能であり、通常のルータに比べて安定性の高いシステム構築が可能となっている。

##応用例
VRRPを利用したネットワーク構成例を3つ紹介する。

###1. スタンダードモード  
スタンダードモードとは、通常の2台のルータを用意し、1台のルータがダウンした場合に2台目のルータが自動的に運用を開始する方式である。

  <img src="https://i.imgur.com/pG0rYxK.png" width=50%>  
図1: スタンダードモードの構成例  

  スタンダードモードの構成例を図1に示す。通常の状態ではRouter_Aが運用しているが、Router_Aがダウンした場合にRouter_Bが自動的に運用を開始する。Router_Bの運用開始手順は以下の通りである。  

    1) Router_Aから応答がなくなったら、Router_Bは自動的に運用を開始する  

    2) Router_Aからの応答が復旧した場合、Router_Bは自動的に運用を停止する  

    3) Router_Aからの応答復旧前にRouter_Bの運用間隔（デフォルトは3秒）よりも長く過ぎた場合、Router_Bは自動的に運用を停止する  

  これらの条件を満たさない限りRouter_Bは運用を継続していくことになっていく。また、上記の条件2・3の応答復旧チェック方法として「ポーリング」「トリガー」「マスク」の3パターンが存在しています。ポーリング方式とトリガー方式の違いは主要な機能の違いであり、マスク方式は2つの機能の違いである。

    ポーリング方式：VRRPインタフェース上でARPパケットの送信・受信チェック  

      <img src="https://i.imgur.com/9CcVLCu.png" width=50%>  
      図2: ポーリング方式の概観図  

    トリガー方式：ICMP ECHO要求パケットの送信・受信チェック  

      <img src="https://i.imgur.com/oZlHhXk.png" width=50%>  
      図3: トリガー方式の概観図  

    マスク方式：応答チェック対象外としたIPアドレスやMACアドレスの一覧表（マスクテーブル）の管理機能  

      <img src="https://i.imgur.com/F8q7Cjc.png" width=50%>  
      図4: マスク方式の概観図    

###2. セミハイブリッドモード  
セミハイブリッドモードとは、通常の状態でバックアップルータも運用しており、1台のルータだけダウンした場合もバックアップルータからサービスを継続させられるような構成である。セミハイブリッドモードの場合もフェールオーバーテスト機能やマスク機能の組み合わせなども利用可能であり、必要な機能の組み合わせだけ利用すればよく、機能使い分けも容易だったりするメリットがあります。  
               
               
               
               
               
               
               
               
               
               
                セミハイブリッドモードの概観図如下所示:                                                                                                                                                                                                                 <img src=" https://i.imgur.com/LxzrkWi .png" width=70%>                                                          図5 : セミハイブリッドモード 概観図                                                     ### 3 . ハイブリッドモード                                              ハイブリッドモード は , 通常の状態 で バックアップ ルータ を