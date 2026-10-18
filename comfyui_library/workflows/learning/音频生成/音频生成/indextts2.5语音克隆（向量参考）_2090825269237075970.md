---
key: 音频生成/音频生成/indextts2.5语音克隆（向量参考）_2090825269237075970.json
name: indextts2.5语音克隆（向量参考）_2090825269237075970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/indextts2.5语音克隆（向量参考）_2090825269237075970.json
hash: 3758a28a8aeef7aa
coverage: 1
learned_at: 2026-10-18 17:45:49
nodes: [T8_IndexTTS25_ModelLoader, T8_IndexTTS25_ModelLoader, LoadAudio, T8_IndexTTS25_Generate, T8_IndexTTS25_Generate, T8_IndexTTS25_EmotionControl, SaveAudio, LoadAudio, T8_IndexTTS25_EmotionControl, SaveAudio]
patterns: []
missing: []
---

# 音频生成/音频生成/indextts2.5语音克隆（向量参考）_2090825269237075970.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/indextts2.5语音克隆（向量参考）_2090825269237075970.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（10 个）：
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_ModelLoader`
- `LoadAudio`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_EmotionControl`
- `SaveAudio`
- `LoadAudio`
- `T8_IndexTTS25_EmotionControl`
- `SaveAudio`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`T8_IndexTTS25_ModelLoader`、`LoadAudio`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_EmotionControl`、`SaveAudio`

**用到的条目**：SaveAudio、LoadAudio、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、sd15-t2i-basic、sd15-t2i-lora、Loader
