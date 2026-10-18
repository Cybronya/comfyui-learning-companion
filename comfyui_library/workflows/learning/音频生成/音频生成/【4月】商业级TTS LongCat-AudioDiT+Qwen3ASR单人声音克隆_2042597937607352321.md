---
key: 音频生成/音频生成/【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR单人声音克隆_2042597937607352321.json
name: 【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR单人声音克隆_2042597937607352321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR单人声音克隆_2042597937607352321.json
hash: 55bf21d7b753f3a8
coverage: 0.875
learned_at: 2026-10-18 02:28:46
nodes: [LongCatVoiceCloneTTS, Qwen3ASRLoader, SaveAudioMP3, CR Prompt Text, LoadAudio, Qwen3ASRTranscribe, PreviewAny, NormalizeAudioLoudness]
patterns: []
missing: []
---

# 音频生成/音频生成/【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR单人声音克隆_2042597937607352321.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR单人声音克隆_2042597937607352321.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `LongCatVoiceCloneTTS`
- `Qwen3ASRLoader`
- `SaveAudioMP3`
- `CR Prompt Text`
- `LoadAudio`
- `Qwen3ASRTranscribe`
- `PreviewAny`
- `NormalizeAudioLoudness`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`LongCatVoiceCloneTTS`、`Qwen3ASRLoader`、`SaveAudioMP3`、`CR Prompt Text`、`LoadAudio`、`Qwen3ASRTranscribe`、`NormalizeAudioLoudness`

**用到的条目**：CR Prompt Text、SaveAudioMP3、LoadAudio、Qwen3ASRLoader、Qwen3ASRTranscribe、NormalizeAudioLoudness、LongCatVoiceCloneTTS、sd15-t2i-basic
