# NGO-AzureFunctionsBlob

## 概要
- Blobとの連携テスト
- .txtの場合、文末にhogeを加え、コンテナに出力
- .csvの場合、各要素にhogeを加える、コンテナに出力
- 上記以外の拡張子の場合、logging.warnだけだして何もしない

## 現状の悩み
- csvをoutputblobに保存するやり方がよくわからない。
- outputblob.set(df.to_string())とするとテキスト情報として出力される（列が結合される）ため意図したものにならない
