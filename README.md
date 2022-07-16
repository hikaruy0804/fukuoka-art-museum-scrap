# fukuoka-art-museum-scrap

### scrapyを使って[福岡市美術館](https://www.fukuoka-art-museum.jp/exhibition/)の企画展情報を取得します。

##### 1.scrapyをインストール　※設定方法は省略
```
pip install scrapy
```
##### 2.プロジェクトフォルダ(fukuoka_city_museum_scrap)をPCに保存
##### 3.ターミナル上でプロジェクトフォルダ(fukuoka_city_museum_scrap)に移動し実行


jsonの場合
```
scrapy crawl [museum_scrap] -o [出力したいファイル名].json"   
```
csvの場合
```
scrapy crawl [museum_scrap] -o [出力したいファイル名].json"   
```

#### 4.フォルダ内に保存完了
