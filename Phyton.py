import boto3
from IPython.display import Audio, display

# Initialize clients
polly = boto3.client('polly')
s3 = boto3.resource('s3')

# 🔴 IMPORTANT: your bucket name (already correct from your screen)
bucket_name = "lab-data-bucket-141477058256-09a7fa60"

def text_to_speech(text, filename):
    # Generate speech using Polly
    response = polly.synthesize_speech(
        Text=text[:3000],
        OutputFormat="mp3",
        VoiceId="Joanna"
    )

    # Get audio stream
    audio_stream = response['AudioStream'].read()

    # ✅ Upload to S3 (CORRECT PATH)
    s3.Object(bucket_name, f"diy-output/{filename}.mp3").put(
        Body=audio_stream
    )

    print(f"Audio saved: s3://{bucket_name}/diy-output/{filename}.mp3")

    # Return audio player
    return Audio(data=audio_stream, autoplay=False)


# ✅ CALL FUNCTION (CORRECT NAME)
audio_player = text_to_speech(extracted_text[:3000], "diy-result")
display(audio_player)
