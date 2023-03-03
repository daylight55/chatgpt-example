

# FTP(File Transfer Protocol)
## 特徴
ファイル転送用のプロトコルで、TCPを使用して通信する。  
クライアントとサーバーの双方向通信に対応しており、ファイルやディレクトリの転送、作成・削除などを行うことができる。  
FTPはアプリケーション層プロトコルであり、OSI参照モデルでは7階層目に位置する。  
IPアドレスとポート番号を使用してファイルを転送するため、NAT越しの通信も可能となっている。  
また、暗号化されていないため、セキュリティは弱く、パスワードなどの機密情報が平文で伝わってしまう。  
FTPクライアントソフトには「FileZilla」「WinSCP」など多数存在する。
## 応用例
・Webサイトの開発・運用に利用されることが多い。  
・OSのダウンロードやアップデートの配布にも利用される。  
・FTPサーバー上に公開フォルダを作成しておくことで、誰からもアクセス可能な公開フォルダとして活用することもできる。  
## 注意点
セキュリティが弱いため、機密情報の漏洩の危険性があり注意が必要だ。  
また、NAT越しの通信も行うことができるため、LAN内の他のマシンからの攻撃を受けやすくなってしまうため注意が必要だ。   
## 関連用語
・TCP/IP(Transmission Control Protocol/Internet Protocol)  
・NAT(Network Address Translation)