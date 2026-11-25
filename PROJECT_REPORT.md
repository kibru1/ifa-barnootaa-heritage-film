
# PROJECT REPORT
## Ifa Barnootaa – The Light of Education

**Project:** AI-Content Generation: The Heritage Short  
**Film duration:** 73 seconds  
**Narration language:** Afaan Oromo  
**Year:** 2026

---

## 1. Project Overview

The project, *Ifa Barnootaa – The Light of Education*, is a short AI-assisted heritage film celebrating the importance of education in individual lives, families, and communities.

The film follows a fictional Ethiopian student whose determination to learn is supported by teachers, family, and the community. Through this story, the film communicates that education creates opportunities, builds hope, and contributes to community development.

The intended audience includes Afaan Oromo speakers, students, teachers, families, and community members, particularly young people who can relate to the importance of education.

## 2. What I Set Out to Create and for Whom

I set out to create a 60–90-second cinematic short film narrated in Afaan Oromo, with English subtitles and original background music.

My goals were to:
- Communicate the value of education through a relatable story.
- Use Afaan Oromo narration to make the film accessible to local audiences.
- Explore AI tools for character design, visual storytelling, narration, and production.
- Produce vertical and horizontal versions suitable for different viewing platforms.
- Clearly disclose the use of AI-generated and AI-assisted content.

## 3. Production Process and Tools

The production process included the following stages:

1. Story development and creation of a ten-shot storyboard.
2. Storyboard validation using JSON Schema.
3. Creation of a fictional character reference.
4. Generation of ten cinematic keyframe images using Stable Diffusion Turbo.
5. Creation of Afaan Oromo narration using the MMS text-to-speech model.
6. Generation of original synthesized instrumental background music using Python and NumPy.
7. Animation of still images using FFmpeg pan-and-zoom effects.
8. Audio mixing with background music reduced during narration.
9. Creation and synchronization of English subtitles.
10. Addition of an AI-generated content disclosure end card.
11. Export of vertical 9:16 and horizontal 16:9 MP4 versions.

The final film is approximately 73 seconds long. The visual sequences use animated still images and cinematic camera movement rather than fully AI-generated video footage.

## 4. Audience and Learning

The intended audience is Afaan Oromo-speaking students, teachers, families, and community members.

Audience testing is still pending. The radio cut and near-final film have been prepared, but feedback from the required viewers has not yet been collected.

I plan to ask viewers whether the story is understandable, whether the narration is clear, whether the music is appropriate, whether the visuals are engaging, and what improvements they recommend.

Actual audience feedback will be added after the testing sessions.

## 5. Hardest Problem and How I Addressed It

One of the main challenges was producing clear Afaan Oromo narration using an AI text-to-speech model.

I tested the MMS Afaan Oromo text-to-speech model and listened to a sample before generating the complete narration. After finding the sample quality acceptable, I generated ten separate narration clips.

Another challenge was creating moving visual sequences within the available computing resources. Instead of relying on a full AI video-generation model, I used FFmpeg to animate the generated keyframes with slow pan-and-zoom effects. This provided a practical way to create a complete cinematic sequence.

I also encountered a font-path error while creating the end card. I resolved it by using a supported default font.

## 6. Practices That Helped and Did Not Help

### Practices that helped
- Testing a short narration sample before generating all narration clips.
- Creating a storyboard before producing the visual assets.
- Using a consistent character description to guide image generation.
- Producing separate narration clips to improve timing and synchronization.
- Verifying generated files before final assembly.
- Using FFmpeg for repeatable video editing and exporting.

### Practices that were less effective
- Some long image prompts caused token-truncation warnings, so prompt length and clarity needed more attention.
- Attempting to use an unavailable font path caused an error during end-card creation.
- Fully AI-generated video was not used because of practical resource and workflow limitations.

## 7. Ceiling Work and Limitations

The project demonstrates a complete AI-assisted short-film workflow, but some limitations remain:

- The visual sequences use animated still images rather than fully generated moving footage.
- The background score is an original synthesized instrumental, not a recording of traditional Ethiopian instruments.
- Audience testing and feedback documentation remain incomplete.
- Model-call latency and actual monetary costs were not measured for every production step.
- Afaan Oromo narration and English translations should ideally receive an additional review by fluent speakers.

## 8. Next Steps

The next steps are:

1. Conduct the required radio-cut audience test with at least three viewers.
2. Conduct the near-final film test with at least three viewers.
3. Record genuine feedback and update DESIGN.md.
4. Review the Afaan Oromo narration and English subtitles with fluent speakers.
5. Improve the production pipeline and document any additional experiments.
6. Complete the project walkthrough video.
7. Publish a public post describing the project and disclosing AI use.
8. Complete both assignment submissions.

## 9. Ethical Considerations

The film uses a fictional student character and does not intentionally represent a real identifiable person. AI-generated visuals and AI-assisted narration are disclosed in the end card.

The narration uses the `facebook/mms-tts-orm` model. Its CC-BY-NC 4.0 license should be respected. The relevant model and image-generation licenses should be reviewed before any commercial distribution.

The project aims to represent education and the local setting respectfully and transparently.

## 10. Conclusion

*Ifa Barnootaa – The Light of Education* demonstrates how accessible AI tools and open-source software can support storytelling in Afaan Oromo.

The project combines a locally relevant educational story, AI-assisted narration, generated visual assets, original synthesized music, subtitles, and video editing into a short film.

It also demonstrates practical problem-solving, resource-aware production, and the importance of documenting both successful techniques and limitations.

---

**Project repository:** https://github.com/kibru1/ifa-barnootaa-heritage-film

**AI disclosure:** This film uses AI-generated visuals, AI-assisted Afaan Oromo narration, and original synthesized background music.
