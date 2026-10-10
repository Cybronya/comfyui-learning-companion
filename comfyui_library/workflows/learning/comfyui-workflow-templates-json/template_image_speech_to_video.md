---
key: comfyui-workflow-templates-json/template_image_speech_to_video.json
name: template_image_speech_to_video
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/template_image_speech_to_video.json
hash: fb5e9e3deb2664d7
official: true
coverage: 0.588235
learned_at: 2026-10-10 22:49:02
nodes: [PreviewAny, LoadImage, ElevenLabsTextToSpeech, RegexExtract, PreviewAny, PreviewAny, SaveAudioMP3, GeminiNode, SaveVideo, 98fb87e2-23b5-4ecb-aacc-365912414a12, ElevenLabsVoiceSelector, LoadAudio, ElevenLabsInstantVoiceClone, MarkdownNote, RegexExtract, MarkdownNote, MarkdownNote]
patterns: []
missing: [98fb87e2-23b5-4ecb-aacc-365912414a12]
discoveries: [次要节点 `98fb87e2-23b5-4ecb-aacc-365912414a12` 知识库中没有该节点类型的任何知识]
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

覆盖率 **59%**（10/17）

**有卡**：`LoadImage`、`ElevenLabsTextToSpeech`、`RegexExtract`、`SaveAudioMP3`、`GeminiNode`、`SaveVideo`、`ElevenLabsVoiceSelector`、`LoadAudio`、`ElevenLabsInstantVoiceClone`

**缺卡**（1）：`98fb87e2-23b5-4ecb-aacc-365912414a12`

**用到的条目**：LoadImage、SaveVideo、SaveAudioMP3、LoadAudio、RegexExtract、ElevenLabsInstantVoiceClone、ElevenLabsTextToSpeech、ElevenLabsVoiceSelector

## 学习发现

- 次要节点 `98fb87e2-23b5-4ecb-aacc-365912414a12` 知识库中没有该节点类型的任何知识
