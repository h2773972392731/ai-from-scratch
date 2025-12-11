from youtube_transcript_api import YouTubeTranscriptApi

video_id = "LF9sd-2jCoY"
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    for entry in transcript:
        print(f"{entry['start']} - {entry['text']}")
except Exception as e:
    print(f"Error retrieving transcript: {e}")
