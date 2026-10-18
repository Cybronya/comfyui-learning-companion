---
key: 音频生成/音频生成/声音克隆（音色参考+情感语气控制）IndexTTS 2.5_2108928627483176962.json
name: 声音克隆（音色参考+情感语气控制）IndexTTS 2.5_2108928627483176962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/声音克隆（音色参考+情感语气控制）IndexTTS 2.5_2108928627483176962.json
hash: 2fcf44297a9502df
coverage: 0.7
learned_at: 2026-10-18 18:02:38
nodes: [T8_IndexTTS25_ModelLoader, Reroute, Reroute, T8_IndexTTS25_EmotionControl, Note, T8_IndexTTS25_Generate, LoadAudio, CR Prompt Text, CR Prompt Text, SaveAudio]
patterns: []
missing: []
---

# 音频生成/音频生成/声音克隆（音色参考+情感语气控制）IndexTTS 2.5_2108928627483176962.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/声音克隆（音色参考+情感语气控制）IndexTTS 2.5_2108928627483176962.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（10 个）：
- `T8_IndexTTS25_ModelLoader`
- `Reroute`
- `Reroute`
- `T8_IndexTTS25_EmotionControl`
- `Note`
- `T8_IndexTTS25_Generate`
- `LoadAudio`
- `CR Prompt Text`
- `CR Prompt Text`
- `SaveAudio`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_EmotionControl`、`T8_IndexTTS25_Generate`、`LoadAudio`、`CR Prompt Text`、`SaveAudio`

**用到的条目**：CR Prompt Text、SaveAudio、LoadAudio、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、sd15-t2i-basic、sd15-t2i-lora
