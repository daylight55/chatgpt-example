

# SDP（Session Description Protocol）

## 特徴
SDPは、IPネットワーク上でメディアセッションを定義するためのプロトコルである。SDPはRFC4566によって定義されている。  
SDPは、IPネットワーク上でメディアセッションを定義するための簡易な文法とセマンティクスを持つ。  
SDPは、通話開始前に、その通話に必要なリソースの情報交換に使用される。  
例えば、電話会議の場合、参加者が使用するマイクロフォンとスピーカーの情報や、必要なバンド幅などを交換することができる。  
また、SDPはテキストベースのプロトコルであり、エンコーディング方式もテキストベースのMIMEエンコーディング方式を使用しているため、テキストエディタで編集が可能である。  
これらの特徴からSDPはIETF（Internet Engineering Task Force）によって標準化されている。  


## 応用例 
RTPプロトコル（Real-time Transport Protocol）を使用したメディアセッションの通信手順は以下の通りである。  
1. 通信相手の情報を取得する。  
2. 情報交換のためのSDPファイルを作成し送信する。  
3. SDPファイルの内容に従ってRTPパケットの送受信を行う。  



　通常の電話会議システムでは上記1~3の応用例となっていますが、WebRTC（Web Real-Time Communication）によりブラウザ間の音声・動画通信が簡単に行えるようになりました。  



　WebRTCはP2P(Peer to Peer)通信をサポートしていますが、NAT(Network Address Translation)環境下でP2P通信が不可能な場合もあります。NAT環境下ではTURN(Traversal Using Relays around NAT)サーバーを利用します。TURNサーバーはNAT環境下から外部への転送機能(Relay機能)だけを持ったサーバーです。TURNサーバーはNAT環境下から外部へ転送する際に利用されますが、TURNサーバー内部でRTPパケットの加工処理を行うこともあります。

  WebRTCの応用例としてSkyway(https://webrtc.ecl.ntt.com/) などのビデオチャットツールがあります。

   

　SkywayはNTT Communicationsが運営しています。WebRTCプラットフォーム「SkyWay」の基本的な使い方の説明資料(https://webrtc.ecl.ntt.com/en/getting-started/) やチュートリアル(https://webrtc.ecl.ntt.com/en/tutorial/) が公開されていますので興味のある方は是非チェックしてください!