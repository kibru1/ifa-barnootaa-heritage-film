# FAILURES AND LIMITATIONS
## Ifa Barnootaa

### 1. Font loading issue
Problem:
An initial attempt to load a specific DejaVu font file failed
because the expected font path was unavailable.

Resolution:
The end-card generation code was changed to use Pillow's
built-in default font.

### 2. Python cell syntax error
Problem:
A plain-text success message was entered into a Python cell,
causing a SyntaxError.

Resolution:
The message was treated as output text rather than executable
Python code.

### 3. Video generation limitation
Problem:
Full AI-generated character motion was not included in the
final production.

Resolution:
The generated keyframes were animated using FFmpeg
pan-and-zoom effects.

### 4. Prompt length warnings
Problem:
Some SD-Turbo prompts exceeded the CLIP token limit.

Resolution:
Images were generated successfully, but future prompts
should be shortened to reduce truncation.

### 5. Remaining limitations
- Visuals are animated still images.
- Music is synthesized, not a traditional instrument recording.
- Audience feedback must be collected and entered before submission.
