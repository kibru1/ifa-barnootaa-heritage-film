# Ifa Barnootaa – The Light of Education

## An AI-Generated Afaan Oromo Heritage Short Film

## About the Project

**Ifa Barnootaa (The Light of Education)** is an AI-generated Afaan Oromo heritage short film celebrating the transformative power of education in Ethiopian communities.

The film follows a fictional young Ethiopian student's educational journey, highlighting the importance of teachers, family support, determination, knowledge, and equal educational opportunities.

This project explores how artificial intelligence and digital storytelling can support cultural expression, educational awareness, and creative multimedia production.

## Project Objectives

- Celebrate the importance of education in society.
- Promote Afaan Oromo through AI-assisted digital storytelling.
- Explore AI-powered image generation and multimedia production.
- Demonstrate how AI technologies can support cultural storytelling.
- Create an engaging short film with narration and original background music.

## Film Information

| Item | Description |
|---|---|
| Project title | Ifa Barnootaa – The Light of Education |
| Story theme | Power of Education |
| Language | Afaan Oromo |
| Country | Ethiopia |
| Duration | 73 seconds |
| Video formats | Vertical (9:16) and Horizontal (16:9) |
| Production environment | Kaggle GPU |
| Production approach | AI-assisted content generation |

## Final Film Deliverables

The completed film is available in two formats. The videos are hosted on Google Drive because of GitHub's individual file-size upload restrictions.

**Video 1**

[Watch the film on Google Drive](https://drive.google.com/file/d/1m8VWuvFTuq5cQAOV9RrDfz0nuxgCHSXb/view?usp=drive_link)

**Video 2**

[Watch the film on Google Drive](https://drive.google.com/file/d/1OZVwTDvudeMi5mjBsEbIr7_GnGNDF1X3/view?usp=sharing)

Both versions contain Afaan Oromo narration, original synthesized background music, English subtitles, and an AI-generated content disclosure.

## Technologies and Tools

- Python
- Kaggle Notebooks
- Stable Diffusion Turbo (SD-Turbo) for image generation
- Meta MMS Text-to-Speech (`facebook/mms-tts-orm`) for Afaan Oromo narration
- NumPy for original synthesized background music
- FFmpeg for video animation, editing, audio mixing, and assembly
- JSON Schema for storyboard validation

## Production Workflow

1. Story development and script preparation.
2. Storyboard creation and JSON Schema validation.
3. Character description and reference image generation.
4. Generation of ten cinematic keyframe images.
5. Animation of still images using the Ken Burns pan-and-zoom technique.
6. Afaan Oromo narration generation using AI text-to-speech.
7. Creation of original synthesized instrumental background music.
8. English subtitle preparation and synchronization.
9. Audio mixing with background music ducking during narration.
10. Film assembly, AI disclosure end card, and export into vertical and horizontal formats.

**Production note:** The video shots use animated AI-generated still images with slow pan-and-zoom effects rather than fully generated AI video footage.

## Repository Structure

```text
ifa-barnootaa-heritage-film/
│
├── README.md
│
└── ifa_barnootaa/
    ├── storyboard.json
    ├── runs.jsonl
    │
    ├── schema/
    │   └── storyboard.schema.json
    │
    ├── pipeline/
    │   ├── assemble_film.py
    │   └── README.md
    │
    ├── assets/
    │   ├── character_reference/
    │   ├── keyframes/
    │   ├── video_shots/
    │   ├── audio/
    │   ├── subtitles/
    │   └── end_card/
    │
    ├── outputs/
    │   ├── ifa_barnootaa_radio_cut.mp4
    │   ├── ifa_barnootaa_vertical_9x16.mp4
    │   └── ifa_barnootaa_horizontal_16x9.mp4
    │
    └── docs/
        ├── DESIGN.md
        ├── ARCHITECTURE.md
        ├── EXPERIMENTS.md
        ├── FAILURES.md
        ├── COSTS.md
        └── ETHICS.md
```

*Note: The large final video files and some production media assets are shared separately because of GitHub upload-size restrictions. The repository contains the project files and documentation that were uploaded.*

## Pipeline

The final video export script is available at:

`ifa_barnootaa/pipeline/assemble_film.py`

It uses the existing production assets to export the vertical, horizontal, and radio-cut versions of the film.

The production assets were generated through the Kaggle notebook workflow. The assembly script handles final exports and does not independently regenerate all AI models or production assets.

## Documentation

The `docs/` directory contains:

- **DESIGN.md:** Project purpose, target audience, creative decisions, and audience-testing plan.
- **ARCHITECTURE.md:** Production architecture and workflow.
- **EXPERIMENTS.md:** Documented production experiments.
- **FAILURES.md:** Production challenges, errors, and solutions.
- **COSTS.md:** Tools, computing environment, and cost considerations.
- **ETHICS.md:** AI disclosure, licensing, responsible use, and cultural considerations.

## Audience Testing

Audience feedback is an important part of evaluating the film.

The project documentation includes a plan for collecting feedback on the radio cut and the near-final film. Testing results will be documented when genuine audience responses have been collected.

## Ethical Considerations

- The main student character is fictional and AI-generated.
- No real person's face or voice was cloned.
- AI-generated content is disclosed in the final film.
- The background music is original synthesized instrumental music.
- Cultural representation should be reviewed carefully and respectfully.
- The MMS text-to-speech model is distributed under a CC-BY-NC 4.0 license; its non-commercial restrictions should be respected.

## Limitations

- The film uses animated still images rather than fully generated AI video.
- AI-generated images may not perfectly represent every Ethiopian cultural detail.
- Afaan Oromo AI narration should be reviewed by fluent speakers.
- Audience testing and feedback remain important areas for further improvement.

## Author

**Kibru Alemu Terfasa**

Ethiopia

Email: kibrualemu812@gmail.com

LinkedIn: Kibru Alemu

## Acknowledgment

This project explores the use of artificial intelligence for cultural storytelling, educational awareness, and creative multimedia production.

**Ifa Barnootaa – Education is the Light of the Future.**
