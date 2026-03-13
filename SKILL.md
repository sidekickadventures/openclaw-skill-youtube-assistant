---
name: youtube-content-assistant
description: Generate YouTube titles, descriptions, tags, and thumbnail ideas for your videos
metadata:
  {
    "openclaw": {
      "emoji": "🎬",
      "requires": {
        "bins": ["python3"],
        "env": ["OPENAI_API_KEY"]
      },
      "install": [
        {
          "id": "pip",
          "kind": "pip",
          "package": "openai",
          "label": "Install OpenAI"
        }
      ]
    }
  }
---

# YouTube Content Assistant

## What This Does
I help YouTubers create awesome video titles, descriptions, tags, and thumbnail ideas!

## When to Use
- You need a catchy title for your video
- You want SEO tags so people find your video
- You need a description with timestamps
- You want thumbnail ideas

## How to Use
1. Tell me your video topic
2. I'll generate 10 title options
3. I'll create a full description with timestamps
4. I'll suggest 20+ tags
5. I'll give you thumbnail ideas

## Examples
User: "Help me with my video about baking cookies"
Assistant: "I'll help! Let me generate titles, description, and tags for your cookie baking video..."