# SYSTEM ARCHITECTURE
## Ifa Barnootaa – The Light of Education

### 1. Overview
The project uses a modular AI-assisted film production
workflow to create a 73-second Afaan Oromo short film.

### 2. Production Pipeline

1. Story development
   - Define the educational theme and target audience.
   - Create a ten-scene storyboard.
   - Validate storyboard data using JSON Schema.

2. Narration generation
   - Model: facebook/mms-tts-orm
   - Generate Afaan Oromo speech for each scene.
   - Save individual narration audio clips.

3. Character and visual generation
   - Create a fictional character description.
   - Generate a character reference image.
   - Generate ten cinematic keyframes using SD-Turbo.

4. Video generation
   - Animate each keyframe with FFmpeg pan-and-zoom.
   - Produce ten seven-second video scenes.
   - Concatenate the scenes and AI disclosure end card.

5. Music and audio
   - Synthesize original instrumental background music.
   - Combine narration and music.
   - Reduce music volume during speech (audio ducking).

6. Subtitles
   - Prepare English translations.
   - Synchronize subtitle timings with narration.
   - Burn subtitles into the exported videos.

7. Export
   - Vertical video: 720 x 1280.
   - Horizontal video: 1280 x 720.
   - Radio cut: black screen with narration and music.

### 3. Tools and Technologies

- Python
- Kaggle GPU environment
- PyTorch and Hugging Face Transformers
- Stability AI SD-Turbo
- Facebook MMS TTS Afaan Oromo model
- FFmpeg
- Pillow
- JSON Schema

### 4. Data Flow

Storyboard
    -> Narration and subtitles
    -> Character reference and keyframes
    -> Animated video scenes
    -> Music and narration mixing
    -> Final editing and subtitle rendering
    -> Vertical and horizontal MP4 exports

### 5. Important Implementation Decision
Full AI video generation was not used for the final scenes.
Instead, the generated still images were animated using
FFmpeg pan-and-zoom effects. This provided a reliable
production method within the available compute resources.

### 6. Output Files

- outputs/ifa_barnootaa_vertical_9x16.mp4
- outputs/ifa_barnootaa_horizontal_16x9.mp4
- outputs/ifa_barnootaa_radio_cut.mp4
