---
key: 声音克隆IndexTTS2.5情感参考_2102959457717276673.json
name: 声音克隆IndexTTS2.5情感参考_2102959457717276673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/声音克隆IndexTTS2.5情感参考_2102959457717276673.json
hash: b8a34e1f695e7f73
coverage: 0.727273
learned_at: 2026-10-10 20:59:42
nodes: [LoadAudio, T8_IndexTTS25_Generate, SaveAudioNode, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_EmotionControl, CR Prompt Text, LoadAudio, Float, SaveAudio, EmptyImage, PreviewImage]
patterns: []
missing: [CR Prompt Text, SaveAudioNode]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `SaveAudioNode` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 声音克隆IndexTTS2.5情感参考_2102959457717276673.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/声音克隆IndexTTS2.5情感参考_2102959457717276673.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（11 个）：
- `LoadAudio`
- `T8_IndexTTS25_Generate`
- `SaveAudioNode`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_EmotionControl`
- `CR Prompt Text`
- `LoadAudio`
- `Float`
- `SaveAudio`
- `EmptyImage`
- `PreviewImage`

## 知识

覆盖率 **73%**（8/11）

**有卡**：`LoadAudio`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_EmotionControl`、`Float`、`SaveAudio`、`EmptyImage`

**缺卡**（2）：`CR Prompt Text`、`SaveAudioNode`

**用到的条目**：SaveAudio、EmptyImage、LoadAudio、Float、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、sd15-t2i-basic

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `SaveAudioNode` 仅有 SaveImage 的通用知识，没有该节点自己的说明
