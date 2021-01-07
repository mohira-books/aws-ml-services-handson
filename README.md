# AWSのMLサービスを使ってみよう

## Cloud9でSDKを実行するための準備
### 1. IAMユーザーの作成
- **ルートユーザーは極力使わないこと！**
- 利用するポリシー
    - `AWSCloud9Administrator`
    - `ComprehendFullAccess`
    - `AmazonRekognitionFullAccess`
    - `AmazonTranscribeFullAccess`
    - `AmazonS3FullAccess` (Transcribeを利用する場合)

### 2. Cloud9環境の作成
- スペックはデフォルトでOK

### 3. リポジトリのClone
```
$ git clone https://github.com/mohira-books/aws-ml-services-handson.git
```

### 4. 必要なモジュールのインストール
```
$ sudo pip3 install boto3 requests
```

### 5. 好きな演習を進める
- [演習: Amazon Comprehend](p01_comprehend/README.md)
- [演習: Amazon Rekognition](p02_rekognition/README.md)
- [演習: Amazon Transcribe](p03_transcribe/README.md)