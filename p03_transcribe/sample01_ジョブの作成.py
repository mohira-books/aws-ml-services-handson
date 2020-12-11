from pprint import pprint

import boto3
from botocore.exceptions import ClientError


def main():
    client = boto3.client('transcribe', region_name='ap-northeast-1')

    job_name = 'YOUR-JOB-NAME'

    # ex: https://your-bucket-name.s3-ap-northeast-1.amazonaws.com/sample.mp4
    mp4_object_uri = 'YOUR-BUCKET-NAME'

    try:
        response = client.start_transcription_job(TranscriptionJobName=job_name,
                                                  LanguageCode='ja-JP',
                                                  MediaFormat='mp4',
                                                  Media={'MediaFileUri': mp4_object_uri})

        print('Jobの作成に成功しました！')
        pprint(response)

    except ClientError as e:
        print('エラーが起きました！')
        pprint(e.response)
        exit()


if __name__ == '__main__':
    main()
