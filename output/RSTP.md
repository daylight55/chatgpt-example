

#RSTP
##正称
Rapid Spanning Tree Protocol（ラピッド・スパニング・ツリー・プロトコル）、IEEE 802.1w
##特徴
* スタンダード化された、高速なスパニングツリーアルゴリズムである。
* ネットワークの自動構成機能を備えている。
* IEEE 802.1Dに比べて、フラッピングやブロック化を抑制することができる。また、ネットワークの構成にかかる時間も短縮されている。
* VLANをサポートしている。
##応用例
IEEE802.1wは、IEEE802.1Dに加えて2つのモードをサポートしている。アクティブモードとポートfast startモードの2つである。アクティブモードは、IEEE802.1Dと同じ動作をする。ポートfast startモードは、ネットワークの再構成にかかる時間を短縮するために用いられる。このモードでは、スイッチは常にポートをフォワーディングモードにしており、ネットワーク障害が発生した場合でもすぐにポートをフォワーディングモードに復帰することができる。
##注意点
IEEE802.1wはIEEE802.1Dと互換性がないため注意が必要である。また、セキュリティ上の理由からも使用する際は注意が必要である。
##関連用語
* STP：スパニングツリーアルゴリズムの一種であり、IEEE 802.1D規格で定められている。最大16ビットの長さのMACアドレスフィールドを使用してトランザクションIDを生成するため、MACアドレスの範囲内でトランザクションIDの重複が生じないようにしなければならない。また2ビットのフラグフィールドと8ビットのチェックサムフィールドも使用するため帯域幅の節約が難しくなっていた（後述）。  
RSTPはSTPの欠点を補う形で導入された規格であり、MACアドレスフィールドの長さを4ビットに削減し8ビットのチェックサムフィールドと4ビットのフラグフィールドだけ使用することで帯域幅の節約に対応している  
* BPDU：Bridge Protocol Data Unitの略語であり、OSI参照モデルのデータリンク層以下の層（物理層・データリンク層）の役割を果たすプロトコルデータ単位（PDU）  
BPDUはOSPFパケットと似ていますがOSPFパケットはIPパケット内部に含まれて転送されます  

  RSTP/STP BPDUフォーマット  

 ![](https://github.com/ryo-ma/markdown_exercises/blob/master/stp_bpdu_format.gif)   

　RSTP BPDUフォーマット  

 ![](https://github.com/ryo-ma/markdown_exercises/blob/master/rstp_bpdu_format.gif)   

 図中の項目の意味  

 * プロトコルバージョン: 2bit  STP=0 / RSTP=2 に固定されています(他にもBPDUフォーマットの定義方法が存在します)    

 * プロトコルオプション: 1bit 常に0x00 に固定されています    

 * メッセージタイプ: 1bit 0x00=Configuration Message / 0x02=Topology Change Notification Message / 0x01=Topology Change Acknowledgment Message に固定されています    

 * タイムアウト: 2bit 2^(n+6)sec (n=0~3 の場合) を意味します n=0 の場合 15sec, n=3 の場名 480sec に相当します    

 * 保留: 3bit 常に0x000 に固定されています    

 * フラグメッセージ: 1bit 0x00=Configuration Message が送信された際の挙動, 0x02=Topology Change Notification Message が送信された際の挙動, 0x01=Topology Change Acknowledgment Message が送信された際の挙動 を表します    

 * Root Identifier: 8byte 送信元bridge ID を表します    8byte = 4byte(priority)+4byte(MAC address)=2byte(bridge priority)+6byte(MAC address) の形式となっています    

 * Root Path Cost: 4byte 送信元bridge ID までの経路コストの合計値を表します 経路コストの定義方法は後述      

 * Bridge Identifier: 8byte 送信元bridge ID を表します    8byte = 4byte(priority)+4byte(MAC address)=2byte(bridge priority)+6byte(MAC address) の形式となっています     　　　　　　　　　         ｜priority| MAC address|                                                              ｜priority| MAC address|                                                              ｜priority| MAC address|                                                              ｜priority| MAC address|            |priority| MAC address|            |priority| MAC address|            |priority| MAC address|            |priority| MAC address|            |priority| MAC address