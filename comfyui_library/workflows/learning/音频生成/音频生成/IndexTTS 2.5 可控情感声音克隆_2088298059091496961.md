---
key: 音频生成/音频生成/IndexTTS 2.5 可控情感声音克隆_2088298059091496961.json
name: IndexTTS 2.5 可控情感声音克隆_2088298059091496961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5 可控情感声音克隆_2088298059091496961.json
hash: 952873993fc13060
coverage: 1
learned_at: 2026-10-18 17:45:32
nodes: [SaveAudio, T8_IndexTTS25_ModelLoader, LoadAudio, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_Generate, T8_IndexTTS25_SamplingConfig]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS 2.5 可控情感声音克隆_2088298059091496961.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5 可控情感声音克隆_2088298059091496961.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（9 个）：
- `SaveAudio`
- `T8_IndexTTS25_ModelLoader`
- `LoadAudio`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_SamplingConfig`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`SaveAudio`、`T8_IndexTTS25_ModelLoader`、`LoadAudio`、`T8_IndexTTS25_EmotionControl`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_SamplingConfig`

**用到的条目**：SaveAudio、LoadAudio、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、T8_IndexTTS25_SamplingConfig、sd15-t2i-basic、sd15-t2i-lora
