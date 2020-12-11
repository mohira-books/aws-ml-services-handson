# AWSのMLサービスを使ってみよう

## 目次

- [Amazon Comprehend](p01_comprehend/README.md)
- [Amazon Rekognition](p02_rekognition/README.md)
- [Amazon Transcribe](p03_transcribe/README.md)

## Cloud9でSDKを実行するための準備
### 1. IAMユーザーの作成

- ルートユーザーは極力使わないこと！
  - 
- 利用するポリシー
    - `AWSCloud9Administrator`
    - `ComprehendFullAccess`
    - `AmazonRekognitionFullAccess`
    - `AmazonTranscribeFullAccess`
    - `AmazonS3FullAccess` (Transcribeを利用する場合)

### 2. Cloud9環境の作成

- スペックはデフォルトでOK

### 3. 必要なモジュールのインストール

```
$ sudo pip install boto3 requests
```

