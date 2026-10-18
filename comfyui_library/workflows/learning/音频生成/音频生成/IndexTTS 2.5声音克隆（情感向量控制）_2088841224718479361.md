---
key: 音频生成/音频生成/IndexTTS 2.5声音克隆（情感向量控制）_2088841224718479361.json
name: IndexTTS 2.5声音克隆（情感向量控制）_2088841224718479361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5声音克隆（情感向量控制）_2088841224718479361.json
hash: f9f51662b1a240b6
coverage: 0.625
learned_at: 2026-10-18 17:45:32
nodes: [SaveAudio, Note, Float, Float, Note, Note, Float, Float, Note, Note, Float, Float, Note, Float, Note, Note, Float, T8_IndexTTS25_Generate, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_ModelLoader, Note, LoadAudio, CR Prompt Text, Float]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS 2.5声音克隆（情感向量控制）_2088841224718479361.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5声音克隆（情感向量控制）_2088841224718479361.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（24 个）：
- `SaveAudio`
- `Note`
- `Float`
- `Float`
- `Note`
- `Note`
- `Float`
- `Float`
- `Note`
- `Note`
- `Float`
- `Float`
- `Note`
- `Float`
- `Note`
- `Note`
- `Float`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_ModelLoader`
- `Note`
- `LoadAudio`
- `CR Prompt Text`
- `Float`

## 知识

覆盖率 **62%**（15/24）

**有卡**：`SaveAudio`、`Float`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_EmotionControl`、`T8_IndexTTS25_ModelLoader`、`LoadAudio`、`CR Prompt Text`

**用到的条目**：CR Prompt Text、SaveAudio、LoadAudio、Float、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、sd15-t2i-basic
