---
key: 视频生成/文生视频/IndexTTS 2.5情感文本控制语音克隆_2100454570265767937.json
name: IndexTTS 2.5情感文本控制语音克隆_2100454570265767937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/IndexTTS 2.5情感文本控制语音克隆_2100454570265767937.json
hash: b53a6dd1c6c69753
coverage: 0.777778
learned_at: 2026-10-11 22:12:33
nodes: [SaveAudio, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_SamplingConfig, LoadAudio, CR Prompt Text, T8_IndexTTS25_Generate, CR Prompt Text, Float, T8_IndexTTS25_EmotionControl]
patterns: []
missing: [CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/IndexTTS 2.5情感文本控制语音克隆_2100454570265767937.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/IndexTTS 2.5情感文本控制语音克隆_2100454570265767937.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（9 个）：
- `SaveAudio`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_SamplingConfig`
- `LoadAudio`
- `CR Prompt Text`
- `T8_IndexTTS25_Generate`
- `CR Prompt Text`
- `Float`
- `T8_IndexTTS25_EmotionControl`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`SaveAudio`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_SamplingConfig`、`LoadAudio`、`T8_IndexTTS25_Generate`、`Float`、`T8_IndexTTS25_EmotionControl`

**缺卡**（2）：`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：SaveAudio、LoadAudio、Float、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、T8_IndexTTS25_SamplingConfig、sd15-t2i-basic

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
