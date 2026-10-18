---
key: 音频生成/音频生成/【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR双人声音克隆_2042617204272795649.json
name: 【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR双人声音克隆_2042617204272795649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR双人声音克隆_2042617204272795649.json
hash: 11a6a3fc073fdc6a
coverage: 0.833333
learned_at: 2026-10-18 02:28:46
nodes: [Qwen3ASRTranscribe, Qwen3ASRLoader, LongCatMultiSpeakerTTS, SaveAudioMP3, NormalizeAudioLoudness, PreviewAny, PreviewAny, Qwen3ASRTranscribe, NormalizeAudioLoudness, CR Prompt Text, LoadAudio, LoadAudio]
patterns: []
missing: []
---

# 音频生成/音频生成/【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR双人声音克隆_2042617204272795649.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/【4月】商业级TTS LongCat-AudioDiT+Qwen3ASR双人声音克隆_2042617204272795649.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（12 个）：
- `Qwen3ASRTranscribe`
- `Qwen3ASRLoader`
- `LongCatMultiSpeakerTTS`
- `SaveAudioMP3`
- `NormalizeAudioLoudness`
- `PreviewAny`
- `PreviewAny`
- `Qwen3ASRTranscribe`
- `NormalizeAudioLoudness`
- `CR Prompt Text`
- `LoadAudio`
- `LoadAudio`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`Qwen3ASRTranscribe`、`Qwen3ASRLoader`、`LongCatMultiSpeakerTTS`、`SaveAudioMP3`、`NormalizeAudioLoudness`、`CR Prompt Text`、`LoadAudio`

**用到的条目**：CR Prompt Text、SaveAudioMP3、LoadAudio、Qwen3ASRLoader、Qwen3ASRTranscribe、NormalizeAudioLoudness、LongCatMultiSpeakerTTS、sd15-t2i-basic
