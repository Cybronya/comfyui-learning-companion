---
key: 音频生成/音频生成/IndexTTS 2.5语音克隆（长文本）_2088942789395574786.json
name: IndexTTS 2.5语音克隆（长文本）_2088942789395574786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5语音克隆（长文本）_2088942789395574786.json
hash: c2eb30c939e60214
coverage: 1
learned_at: 2026-10-18 17:45:35
nodes: [NormalizeAudioLoudness, LoadAudio, SaveAudioMP3, CR Prompt Text, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_Generate, T8_IndexTTS25_SamplingConfig]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS 2.5语音克隆（长文本）_2088942789395574786.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5语音克隆（长文本）_2088942789395574786.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（7 个）：
- `NormalizeAudioLoudness`
- `LoadAudio`
- `SaveAudioMP3`
- `CR Prompt Text`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_SamplingConfig`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`NormalizeAudioLoudness`、`LoadAudio`、`SaveAudioMP3`、`CR Prompt Text`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_SamplingConfig`

**用到的条目**：CR Prompt Text、SaveAudioMP3、LoadAudio、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、NormalizeAudioLoudness、T8_IndexTTS25_SamplingConfig、sd15-t2i-basic
