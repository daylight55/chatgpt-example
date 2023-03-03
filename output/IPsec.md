

# IPsec
IPsec(Internet Protocol Security)は、インターネットプロトコルをセキュアにするための技術である。

## 特徴
IPsecは、IPパケットの認証と暗号化を行う。認証はSender Authentication Header(AH)で行われ、暗号化はEncapsulating Security Payload(ESP)で行われる。また、IPsecはトunnnelモードとTransportモードの2つがある。Tunnnelモードでは、通信元・通信先のアドレスを隠蔽して通信することができる。一方、Transportモードではアドレスが通信相手に伝わってしまうため、セキュリティレベルは低くなる。

## 応用例
VPN(Virtual Private Network)の構築に利用されることが多い。また、IoTデバイスの通信をセキュリティ対策する場合にも利用される。

## 注意点
セキュリティレベルの高いTunnnelモードの通信を行う場合、パフォーマンスが劣化することがあるため注意が必要である。また、IoTデバイスの場合はCPUのパワー不足などによりセキュリティ対策を施すことが難しい場合もあるため注意が必要である。

## 関連用語
IPSec over L2TPv3:L2TPv3プロトコル上にIPsecを実装したプロトコル