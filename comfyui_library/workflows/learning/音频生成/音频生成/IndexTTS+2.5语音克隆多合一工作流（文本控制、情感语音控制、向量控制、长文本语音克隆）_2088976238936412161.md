---
key: 音频生成/音频生成/IndexTTS+2.5语音克隆多合一工作流（文本控制、情感语音控制、向量控制、长文本语音克隆）_2088976238936412161.json
name: IndexTTS+2.5语音克隆多合一工作流（文本控制、情感语音控制、向量控制、长文本语音克隆）_2088976238936412161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS+2.5语音克隆多合一工作流（文本控制、情感语音控制、向量控制、长文本语音克隆）_2088976238936412161.json
hash: e09afe6c51949586
coverage: 0.896552
learned_at: 2026-10-18 17:45:35
nodes: [CR Prompt Text, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_ModelLoader, Fast Groups Bypasser (rgthree), CR Prompt Text, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_EmotionControl, CR Prompt Text, JjkText, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_ModelLoader, LoadAudio, JjkText, CR Prompt Text, T8_IndexTTS25_SamplingConfig, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_Generate, SaveAudioAdvanced, LoadAudio, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_Generate, SaveAudioAdvanced, LoadAudio, LoadAudio, LoadAudio, T8_IndexTTS25_Generate, SaveAudioAdvanced, T8_IndexTTS25_Generate, SaveAudioAdvanced]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS+2.5语音克隆多合一工作流（文本控制、情感语音控制、向量控制、长文本语音克隆）_2088976238936412161.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS+2.5语音克隆多合一工作流（文本控制、情感语音控制、向量控制、长文本语音克隆）_2088976238936412161.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（29 个）：
- `CR Prompt Text`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_ModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `CR Prompt Text`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_EmotionControl`
- `CR Prompt Text`
- `JjkText`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_ModelLoader`
- `LoadAudio`
- `JjkText`
- `CR Prompt Text`
- `T8_IndexTTS25_SamplingConfig`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_Generate`
- `SaveAudioAdvanced`
- `LoadAudio`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_Generate`
- `SaveAudioAdvanced`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `T8_IndexTTS25_Generate`
- `SaveAudioAdvanced`
- `T8_IndexTTS25_Generate`
- `SaveAudioAdvanced`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`CR Prompt Text`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_EmotionControl`、`LoadAudio`、`T8_IndexTTS25_SamplingConfig`、`T8_IndexTTS25_Generate`、`SaveAudioAdvanced`

**用到的条目**：CR Prompt Text、SaveAudioAdvanced、LoadAudio、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、T8_IndexTTS25_SamplingConfig、sd15-t2i-basic
