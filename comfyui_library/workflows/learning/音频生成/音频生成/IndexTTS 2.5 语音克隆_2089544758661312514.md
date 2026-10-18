---
key: 音频生成/音频生成/IndexTTS 2.5 语音克隆_2089544758661312514.json
name: IndexTTS 2.5 语音克隆_2089544758661312514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5 语音克隆_2089544758661312514.json
hash: 056dbc351d4a5d24
coverage: 0.8125
learned_at: 2026-10-18 17:45:32
nodes: [LoadAudio, MarkdownNote, SaveAudio, Label (rgthree), CR Prompt Text, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_Generate, T8_IndexTTS25_SamplingConfig, Label (rgthree), LoadAudio, RH_IndexTTS25_Loader, RH_IndexTTS25_Synthesize, LoadAudio, SaveAudioAdvanced, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS 2.5 语音克隆_2089544758661312514.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5 语音克隆_2089544758661312514.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（16 个）：
- `LoadAudio`
- `MarkdownNote`
- `SaveAudio`
- `Label (rgthree)`
- `CR Prompt Text`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_SamplingConfig`
- `Label (rgthree)`
- `LoadAudio`
- `RH_IndexTTS25_Loader`
- `RH_IndexTTS25_Synthesize`
- `LoadAudio`
- `SaveAudioAdvanced`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`LoadAudio`、`SaveAudio`、`Label (rgthree)`、`CR Prompt Text`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_SamplingConfig`、`RH_IndexTTS25_Loader`、`RH_IndexTTS25_Synthesize`、`SaveAudioAdvanced`

**用到的条目**：CR Prompt Text、RH_IndexTTS25_Synthesize、SaveAudio、SaveAudioAdvanced、LoadAudio、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、RH_IndexTTS25_Loader
