

# 概要
## ONUの特徴
### 光ファイバーを利用した高速通信
光ファイバーは電波に比べて伝搬損失が少なく、かつ広帯域を利用できるため、高速なデータ伝送が可能である。また、電波を利用する場合は周波数帯域の制限があり、地上や都市部では他の電波と競合してしまうこともあるが、光ファイバーは地下を伝っていくため競合の心配がない。
### 長距離のデータ伝送に適している
光ファイバーは電波に比べて伝搬損失が少なく、かつ広帯域を利用できるため、長距離のデータ伝送に適している。特にアクセス電話線(POTS:Plain Old Telephone Service)の場合、最大5km程度しか伝送距離がなく、さらに電波の届きやすさにも左右されるため、一般的な住宅では使用することができない。一方で光ファイバーは最大100km程度の距離まで伝送可能であり、さらに届きやすさも考慮する必要がないため、幅広いエリアで使用することが可能となっている。
### 電力供給不要
光ファイバーは有線LAN(Local Area Network)の構成要素の1つとして使用されており、無線LAN(Wireless LAN)に比べて安定したネットワーク環境を構築することが可能となっている。また無線LANの場合は周囲の電波環境に左右されやすく、特に密集したビル内部や都心部では使用することが困難だったりする。一方で有線LANの場合は周囲の電波環境の影響を受けにくく、特にビル内部や都心部でも使用することが可能だったりする。
## ONUの応用例
### PON(Passive Optical Network)システムの構成要素
PON(Passive Optical Network)システムの構成要素の1つとしてONU(Optical Network Unit)を使用しているケースがあります。PONシステムはOLT(Optical Line Terminal)から光ファイバーを引き出しONUへと導入します。OLTからONUまでの長さは20km以内の短距離パスを想定して設計されています。OLTからONUまでの長さが20km以上の場合はアクティブ機器を介在させなければなりません。アクティブ機器の管理・メンテナンスコスト・エネルギーコストを考慮しPONシステムは20km以内の短距離パスを想定して自動的/手動的に選択されます。