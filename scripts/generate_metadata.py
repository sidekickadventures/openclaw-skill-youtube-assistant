#!/usr/bin/env python3
"""
YouTube Metadata Generator for OpenClaw
"""

import argparse
import json
import os
import sys
import openai

# Get API key from environment
openai.api_key = os.environ.get("OPENAI_API_KEY", "")
MODEL = "gpt-3.5-turbo"  # Cheaper and faster!

def generate_titles(topic, audience="general", count=10):
    """Make up cool video titles"""
    prompt = f"Generate {count} YouTube titles for a video about '{topic}'. Target audience: {audience}. Return as JSON array."
    
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=500
        )
        return json.loads(response.choices[0].message.content)
    except:
        return [f"How to Master {topic}", f"{topic} for Beginners", f"The Ultimate {topic} Guide"]

def generate_description(topic, key_points=None):
    """Write a video description"""
    if key_points is None:
        key_points = ["Introduction", "Main content", "Tips and tricks"]
    
    prompt = f"Write a YouTube description for a video about '{topic}'. Include timestamps for: {', '.join(key_points)}"
    
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=800
        )
        return response.choices[0].message.content
    except:
        return f"Check out this video about {topic}! Learn everything you need to know."

def generate_tags(topic, count=20):
    """Generate YouTube tags"""
    prompt = f"Generate {count} YouTube SEO tags for a video about '{topic}'. Return as JSON array."
    
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=500
        )
        return json.loads(response.choices[0].message.content)
    except:
        words = topic.lower().split()
        return words + [f"{topic} tutorial", f"how to {topic}", f"best {topic}"]

def main():
    parser = argparse.ArgumentParser(description="Generate YouTube metadata")
    parser.add_argument("--type", choices=["titles", "description", "tags", "all"], required=True)
    parser.add_argument("--topic", required=True, help="Video topic")
    parser.add_argument("--audience", default="general", help="Target audience")
    parser.add_argument("--count", type=int, default=10, help="Number to generate")
    
    args = parser.parse_args()
    
    if args.type == "titles" or args.type == "all":
        titles = generate_titles(args.topic, args.audience, args.count)
        print("\n🎬 TITLE OPTIONS:")
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title}")
    
    if args.type == "description" or args.type == "all":
        desc = generate_description(args.topic)
        print("\n📝 DESCRIPTION:")
        print(desc)
    
    if args.type == "tags" or args.type == "all":
        tags = generate_tags(args.topic, args.count)
        print("\n🏷️ TAGS:")
        print(", ".join(tags))

if __name__ == "__main__":
    main()