---
key: 音频生成/音频生成/IndexTTS 2.5情感向量控制语音克隆_2089188391467438081.json
name: IndexTTS 2.5情感向量控制语音克隆_2089188391467438081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5情感向量控制语音克隆_2089188391467438081.json
hash: 8d549d80e417d86c
coverage: 0.894737
learned_at: 2026-10-18 17:45:33
nodes: [Float, Float, Float, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_EmotionControl, Float, Float, Float, Float, Float, T8_IndexTTS25_Pronunciation, 孤海注释, 孤海注释, T8_IndexTTS25_SamplingConfig, LoadAudio, CR Prompt Text, Float, SaveAudio, T8_IndexTTS25_Generate]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS 2.5情感向量控制语音克隆_2089188391467438081.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5情感向量控制语音克隆_2089188391467438081.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（19 个）：
- `Float`
- `Float`
- `Float`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_EmotionControl`
- `Float`
- `Float`
- `Float`
- `Float`
- `Float`
- `T8_IndexTTS25_Pronunciation`
- `孤海注释`
- `孤海注释`
- `T8_IndexTTS25_SamplingConfig`
- `LoadAudio`
- `CR Prompt Text`
- `Float`
- `SaveAudio`
- `T8_IndexTTS25_Generate`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`Float`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_EmotionControl`、`T8_IndexTTS25_Pronunciation`、`T8_IndexTTS25_SamplingConfig`、`LoadAudio`、`CR Prompt Text`、`SaveAudio`、`T8_IndexTTS25_Generate`

**用到的条目**：CR Prompt Text、SaveAudio、LoadAudio、Float、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、T8_IndexTTS25_SamplingConfig
