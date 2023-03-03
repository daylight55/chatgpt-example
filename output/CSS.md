

---
title: CSS
---

# CSS
## 特徴
・HTMLにスタイルを指定するための言語  
・文字の大きさ、フォントの種類、文字の色、背景の色などを指定できる  
・テーブルやマージン、ボーダーなどレイアウトを指定できる  
・アニメーション効果を付与できる  
・マークアップ言語(HTML)とは独立して使用できる  


## 応用例　 
CSSはWebサイトにスタイリングを行うための言語であり、多くの応用例がある。  
ここではCSSの基本的な応用例として文字サイズの指定、テーブルの指定、ボタンの指定を紹介する。

　### 文字サイズの指定

 ```css:sample 
 p {  /* 要素「p」に対して */  font-size: 20px;  /* 20pxサイズの書体を適用 */ }  /* {}内は1セット */```

 文字サイズは「font-size」プロパティによって指定する。単位は「px(ピクセル)」か「em(親要素に対する相対値)」が使われる。また数値だけでも可能だが、「%(パーセンテージ)」や「pt(ポイント)」などの単位も使用できる。

 ### テーブルの指定

 ```css:sample  table, th, td { border: 1px solid black; }```

 テーブルはtableタグで作成する。tableタグにborderプロパティを指定すれば表示される線が変化する。また線の種類(solid, dotted, dashed, double, groove, ridge, inset, outset)や太さ(thin, medium, thick)、色(black, silver, gray...)も指定可能である。

 ### ボタンの指定

 ```css:sample input[type=button], input[type=submit], button { color: #fff; background-color: #337ab7; border-color: #2e6da4; }```

 フォーム内のボタンはinput[type=button]タグかinput[type=submit]タグかbuttonタグで作成することが出来る。これらに対してcolorプロパティ(文字色)、background-colorプロパティ(背景色)、border-colorプロパティ(ボーダーカラー＝線の色)を指定すればデザイン性の高いボタンを作成することが出来る。

 ## 注意点　 
 CSSにはバージョン3までがあり、バージョン4以降はまだ正式版としてリリースされていない。  
 そのためバージョン3までしか対応していないブラウザもあり注意が必要だ。  

 ## 関連用語　 
 HTML（HyperText Markup Language）＝マークアップ言語