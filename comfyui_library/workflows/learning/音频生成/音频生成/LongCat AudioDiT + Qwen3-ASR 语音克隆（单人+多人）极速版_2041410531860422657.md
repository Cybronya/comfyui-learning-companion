---
key: 音频生成/音频生成/LongCat AudioDiT + Qwen3-ASR 语音克隆（单人+多人）极速版_2041410531860422657.json
name: LongCat AudioDiT + Qwen3-ASR 语音克隆（单人+多人）极速版_2041410531860422657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/LongCat AudioDiT + Qwen3-ASR 语音克隆（单人+多人）极速版_2041410531860422657.json
hash: 454359509cf4aa0e
coverage: 0.96
learned_at: 2026-10-18 02:28:41
nodes: [NormalizeAudioLoudness, ShowText|pysssss, SaveAudio, SaveAudioMP3, SaveAudio, SaveAudioMP3, CR Prompt Text, Qwen3ASRTranscribe, Qwen3ASRLoader, SaveAudio, NormalizeAudioLoudness, CR Prompt Text, LongCatTTS, LongCatVoiceCloneTTS, NormalizeAudioLoudness, LoadAudio, CR Prompt Text, LoadAudio, LoadAudio, Qwen3ASRLoader, Qwen3ASRLoader, SaveAudioMP3, Qwen3ASRTranscribe, Qwen3ASRTranscribe, LongCatMultiSpeakerTTS]
patterns: []
missing: []
---

# 音频生成/音频生成/LongCat AudioDiT + Qwen3-ASR 语音克隆（单人+多人）极速版_2041410531860422657.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/LongCat AudioDiT + Qwen3-ASR 语音克隆（单人+多人）极速版_2041410531860422657.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（25 个）：
- `NormalizeAudioLoudness`
- `ShowText|pysssss`
- `SaveAudio`
- `SaveAudioMP3`
- `SaveAudio`
- `SaveAudioMP3`
- `CR Prompt Text`
- `Qwen3ASRTranscribe`
- `Qwen3ASRLoader`
- `SaveAudio`
- `NormalizeAudioLoudness`
- `CR Prompt Text`
- `LongCatTTS`
- `LongCatVoiceCloneTTS`
- `NormalizeAudioLoudness`
- `LoadAudio`
- `CR Prompt Text`
- `LoadAudio`
- `LoadAudio`
- `Qwen3ASRLoader`
- `Qwen3ASRLoader`
- `SaveAudioMP3`
- `Qwen3ASRTranscribe`
- `Qwen3ASRTranscribe`
- `LongCatMultiSpeakerTTS`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`NormalizeAudioLoudness`、`SaveAudio`、`SaveAudioMP3`、`CR Prompt Text`、`Qwen3ASRTranscribe`、`Qwen3ASRLoader`、`LongCatTTS`、`LongCatVoiceCloneTTS`、`LoadAudio`、`LongCatMultiSpeakerTTS`

**用到的条目**：CR Prompt Text、SaveAudio、SaveAudioMP3、LoadAudio、Qwen3ASRLoader、Qwen3ASRTranscribe、NormalizeAudioLoudness、LongCatVoiceCloneTTS
