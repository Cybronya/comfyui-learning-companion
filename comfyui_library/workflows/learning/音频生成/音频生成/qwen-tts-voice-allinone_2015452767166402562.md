---
key: 音频生成/音频生成/qwen-tts-voice-allinone_2015452767166402562.json
name: qwen-tts-voice-allinone_2015452767166402562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/qwen-tts-voice-allinone_2015452767166402562.json
hash: 1626abac3054da03
coverage: 1
learned_at: 2026-10-18 02:07:08
nodes: [Qwen3TTSModelLoader, Qwen3TTSModelLoader, Qwen3TTSVoiceDesign, SaveAudioMP3, Qwen3TTSModelLoader, SaveAudioMP3, Qwen3TTSCustomVoice, SaveAudioMP3, LoadAudio, Qwen3TTSVoiceClone]
patterns: []
missing: []
---

# 音频生成/音频生成/qwen-tts-voice-allinone_2015452767166402562.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/qwen-tts-voice-allinone_2015452767166402562.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（10 个）：
- `Qwen3TTSModelLoader`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceDesign`
- `SaveAudioMP3`
- `Qwen3TTSModelLoader`
- `SaveAudioMP3`
- `Qwen3TTSCustomVoice`
- `SaveAudioMP3`
- `LoadAudio`
- `Qwen3TTSVoiceClone`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`Qwen3TTSModelLoader`、`Qwen3TTSVoiceDesign`、`SaveAudioMP3`、`Qwen3TTSCustomVoice`、`LoadAudio`、`Qwen3TTSVoiceClone`

**用到的条目**：SaveAudioMP3、LoadAudio、Qwen3TTSModelLoader、Qwen3TTSVoiceClone、Qwen3TTSVoiceDesign、Qwen3TTSCustomVoice、sd15-t2i-basic、sd15-t2i-lora
