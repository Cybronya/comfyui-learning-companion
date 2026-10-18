---
key: 音频生成/音频生成/IndexTTS 2.5语音克隆（情感参考）_2088943720514281474.json
name: IndexTTS 2.5语音克隆（情感参考）_2088943720514281474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5语音克隆（情感参考）_2088943720514281474.json
hash: bec1225d955cbc00
coverage: 1
learned_at: 2026-10-18 17:45:34
nodes: [T8_IndexTTS25_EmotionControl, NormalizeAudioLoudness, NormalizeAudioLoudness, CR Prompt Text, LoadAudio, LoadAudio, SaveAudioMP3, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_Generate, Float]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS 2.5语音克隆（情感参考）_2088943720514281474.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5语音克隆（情感参考）_2088943720514281474.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（10 个）：
- `T8_IndexTTS25_EmotionControl`
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `CR Prompt Text`
- `LoadAudio`
- `LoadAudio`
- `SaveAudioMP3`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_Generate`
- `Float`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`T8_IndexTTS25_EmotionControl`、`NormalizeAudioLoudness`、`CR Prompt Text`、`LoadAudio`、`SaveAudioMP3`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_Generate`、`Float`

**用到的条目**：CR Prompt Text、SaveAudioMP3、LoadAudio、Float、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、NormalizeAudioLoudness
