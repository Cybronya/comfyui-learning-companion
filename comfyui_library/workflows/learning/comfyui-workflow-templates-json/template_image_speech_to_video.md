---
key: comfyui-workflow-templates-json/template_image_speech_to_video.json
name: template_image_speech_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/template_image_speech_to_video.json
hash: fb5e9e3deb2664d7
official: true
coverage: 0.647059
learned_at: 2026-10-15 22:24:56
nodes: [PreviewAny, LoadImage, ElevenLabsTextToSpeech, RegexExtract, PreviewAny, PreviewAny, SaveAudioMP3, GeminiNode, SaveVideo, 98fb87e2-23b5-4ecb-aacc-365912414a12, ElevenLabsVoiceSelector, LoadAudio, ElevenLabsInstantVoiceClone, MarkdownNote, RegexExtract, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/template_image_speech_to_video.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/template_image_speech_to_video.json`

## 结构

**生成流程**：Output → Other

**节点**（17 个）：
- `PreviewAny`
- `LoadImage`
- `ElevenLabsTextToSpeech`
- `RegexExtract`
- `PreviewAny`
- `PreviewAny`
- `SaveAudioMP3`
- `GeminiNode`
- `SaveVideo`
- `98fb87e2-23b5-4ecb-aacc-365912414a12`
- `ElevenLabsVoiceSelector`
- `LoadAudio`
- `ElevenLabsInstantVoiceClone`
- `MarkdownNote`
- `RegexExtract`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **65%**（11/17）

**有卡**：`LoadImage`、`ElevenLabsTextToSpeech`、`RegexExtract`、`SaveAudioMP3`、`GeminiNode`、`SaveVideo`、`98fb87e2-23b5-4ecb-aacc-365912414a12`、`ElevenLabsVoiceSelector`、`LoadAudio`、`ElevenLabsInstantVoiceClone`

**用到的条目**：LoadImage、SaveVideo、SaveAudioMP3、LoadAudio、RegexExtract、ElevenLabsInstantVoiceClone、ElevenLabsTextToSpeech、ElevenLabsVoiceSelector
