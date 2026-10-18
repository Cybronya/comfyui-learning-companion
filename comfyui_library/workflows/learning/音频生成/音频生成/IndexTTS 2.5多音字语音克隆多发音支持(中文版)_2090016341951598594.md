---
key: 音频生成/音频生成/IndexTTS 2.5多音字语音克隆多发音支持(中文版)_2090016341951598594.json
name: IndexTTS 2.5多音字语音克隆多发音支持(中文版)_2090016341951598594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5多音字语音克隆多发音支持(中文版)_2090016341951598594.json
hash: 28b5ad9fb2bb679f
coverage: 1
learned_at: 2026-10-18 17:45:33
nodes: [T8_IndexTTS25_ModelLoader, CR Prompt Text, T8_IndexTTS25_Pronunciation, CR Prompt Text, SaveAudio, T8_IndexTTS25_Generate, LoadAudio]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS 2.5多音字语音克隆多发音支持(中文版)_2090016341951598594.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5多音字语音克隆多发音支持(中文版)_2090016341951598594.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（7 个）：
- `T8_IndexTTS25_ModelLoader`
- `CR Prompt Text`
- `T8_IndexTTS25_Pronunciation`
- `CR Prompt Text`
- `SaveAudio`
- `T8_IndexTTS25_Generate`
- `LoadAudio`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`T8_IndexTTS25_ModelLoader`、`CR Prompt Text`、`T8_IndexTTS25_Pronunciation`、`SaveAudio`、`T8_IndexTTS25_Generate`、`LoadAudio`

**用到的条目**：CR Prompt Text、SaveAudio、LoadAudio、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、T8_IndexTTS25_Pronunciation、sd15-t2i-basic、sd15-t2i-lora
