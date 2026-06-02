from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def extract_video_id(url: str) -> str:
    parsed = urlparse(url)

    # https://www.youtube.com/watch?v=VIDEO_ID
    if "youtube.com" in parsed.netloc:
        video_id = parse_qs(parsed.query).get("v")
        if video_id:
            return video_id[0]

    # https://youtu.be/VIDEO_ID
    elif "youtu.be" in parsed.netloc:
        return parsed.path.lstrip("/")

    raise ValueError("Invalid YouTube URL")


def get_transcript(youtube_url: str) -> str:
    video_id = extract_video_id(youtube_url)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)

    text = " ".join(
        snippet.text
        for snippet in transcript.snippets
    )

    return text