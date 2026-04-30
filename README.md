# aws-ai-speech-processing-pipeline
End-to-end AI pipeline using AWS Transcribe, Polly, Textract, and S3 to process documents and convert speech ↔ text
# AI Speech Processing Pipeline (AWS)

## 🚀 Overview

This project demonstrates an end-to-end AI pipeline using AWS services to process documents and speech.

The system extracts text from documents, converts speech to text, and generates audio output using AWS AI services.

---

## 🧠 AWS Services Used

* Amazon Textract – Extract text from PDF documents
* Amazon Transcribe – Convert speech to text
* Amazon Polly – Convert text to speech (MP3)
* Amazon S3 – Store input and output files
* Amazon SageMaker – Execute notebook and orchestrate pipeline

---



---

## ⚙️ How It Works

### Step 1: Document Processing

* PDF file stored in S3
* Text extracted using Amazon Textract

---

### Step 2: Speech to Text

* Audio file processed using Amazon Transcribe
* Transcription output generated

[download.wav](https://github.com/user-attachments/files/27259074/download.wav)

### Step 3: Text to Speech

* Extracted/transcribed text sent to Amazon Polly
* MP3 audio file generated

```python
response = polly.synthesize_speech(
    Text=text[:3000],
    OutputFormat="mp3",
    VoiceId="Joanna"
)

audio_stream = response['AudioStream'].read()

s3.Object(bucket_name, f"diy-output/{filename}.mp3").put(
    Body=audio_stream
)
```

---

### Step 4: Storage

* Output audio stored in Amazon S3

![S3 Output](screenshots/s3-audio-output.png)

---

### Step 5: Playback

* Audio player rendered inside SageMaker notebook

![Audio Player](screenshots/audio-player.png)

---

## 📒 Notebook

Main execution file:

```bash
notebooks/UseAI-Notebook.ipynb
```

---

## 📸 Screenshots

### Notebook Overview

![Notebook](screenshots/notebook-overview.png)

---

## 🔑 Key Features

* End-to-end AI pipeline
* Multi-service AWS integration
* Serverless architecture
* Automated speech processing
* Scalable cloud storage

---

## 🚧 Future Improvements

* Add real-time streaming transcription
* Build API with AWS Lambda + API Gateway
* Add frontend UI for uploads
* Add language translation with Amazon Translate

---

## 👨‍💻 Author

Yonathan Jaramillo

---
