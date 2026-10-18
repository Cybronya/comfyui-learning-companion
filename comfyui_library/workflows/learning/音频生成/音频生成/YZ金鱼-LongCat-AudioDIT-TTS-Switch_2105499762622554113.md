---
key: 音频生成/音频生成/YZ金鱼-LongCat-AudioDIT-TTS-Switch_2105499762622554113.json
name: YZ金鱼-LongCat-AudioDIT-TTS-Switch_2105499762622554113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/YZ金鱼-LongCat-AudioDIT-TTS-Switch_2105499762622554113.json
hash: 4857267aa542c59e
coverage: 0.636364
learned_at: 2026-10-18 18:02:31
nodes: [Note, Reroute, Qwen3ASRLoader, Qwen3ASRLoader, Reroute, Reroute, NormalizeAudioLoudness, Note, NormalizeAudioLoudness, NormalizeAudioLoudness, Qwen3ASRTranscribe, Qwen3ASRTranscribe, LongCatMultiSpeakerTTS, LongCatVoiceCloneTTS, LongCatTTS, LoadAudio, LoadAudio, SetNode, SetNode, GetNode, AudioCrop, GetNode, Qwen3ASRLoader, Qwen3ASRTranscribe, AudioCrop, CR Prompt Text, SetNode, AudioCrop, GetNode, Int, SaveAudioAdvanced, easy anythingIndexSwitch, GetNode]
patterns: []
missing: []
---

# 音频生成/音频生成/YZ金鱼-LongCat-AudioDIT-TTS-Switch_2105499762622554113.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/YZ金鱼-LongCat-AudioDIT-TTS-Switch_2105499762622554113.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（33 个）：
- `Note`
- `Reroute`
- `Qwen3ASRLoader`
- `Qwen3ASRLoader`
- `Reroute`
- `Reroute`
- `NormalizeAudioLoudness`
- `Note`
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `Qwen3ASRTranscribe`
- `Qwen3ASRTranscribe`
- `LongCatMultiSpeakerTTS`
- `LongCatVoiceCloneTTS`
- `LongCatTTS`
- `LoadAudio`
- `LoadAudio`
- `SetNode`
- `SetNode`
- `GetNode`
- `AudioCrop`
- `GetNode`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `AudioCrop`
- `CR Prompt Text`
- `SetNode`
- `AudioCrop`
- `GetNode`
- `Int`
- `SaveAudioAdvanced`
- `easy anythingIndexSwitch`
- `GetNode`

## 知识

覆盖率 **64%**（21/33）

**有卡**：`Qwen3ASRLoader`、`NormalizeAudioLoudness`、`Qwen3ASRTranscribe`、`LongCatMultiSpeakerTTS`、`LongCatVoiceCloneTTS`、`LongCatTTS`、`LoadAudio`、`AudioCrop`、`CR Prompt Text`、`Int`、`SaveAudioAdvanced`、`easy anythingIndexSwitch`

**用到的条目**：CR Prompt Text、SaveAudioAdvanced、Int、LoadAudio、AudioCrop、Qwen3ASRLoader、Qwen3ASRTranscribe、NormalizeAudioLoudness
