---
key: 音频生成/音频生成/VoxCPM+OmniVoice Voice+Longcat：语音设计+克隆_2043295151799406593.json
name: VoxCPM+OmniVoice Voice+Longcat：语音设计+克隆_2043295151799406593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/VoxCPM+OmniVoice Voice+Longcat：语音设计+克隆_2043295151799406593.json
hash: 4b22cad17f693e0c
coverage: 0.935484
learned_at: 2026-10-18 02:28:44
nodes: [Qwen3ASRLoader, Qwen3ASRTranscribe, NormalizeAudioLoudness, NormalizeAudioLoudness, RunningHub_VoxCPM_LoadModel, OmniVoiceWhisperLoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, Note, TextInput_, Fast Muter (rgthree), RunningHub_VoxCPM_Generate, LongCatVoiceCloneTTS, OmniVoiceVoiceCloneTTS, SaveAudioMP3, SaveAudioMP3, SaveAudioMP3, OmniVoiceVoiceDesignTTS, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, CR Prompt Text, InversionDemoLazyIndexSwitch, Note, easy int]
patterns: []
missing: []
---

# 音频生成/音频生成/VoxCPM+OmniVoice Voice+Longcat：语音设计+克隆_2043295151799406593.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/VoxCPM+OmniVoice Voice+Longcat：语音设计+克隆_2043295151799406593.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（31 个）：
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `RunningHub_VoxCPM_LoadModel`
- `OmniVoiceWhisperLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `Note`
- `TextInput_`
- `Fast Muter (rgthree)`
- `RunningHub_VoxCPM_Generate`
- `LongCatVoiceCloneTTS`
- `OmniVoiceVoiceCloneTTS`
- `SaveAudioMP3`
- `SaveAudioMP3`
- `SaveAudioMP3`
- `OmniVoiceVoiceDesignTTS`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `CR Prompt Text`
- `InversionDemoLazyIndexSwitch`
- `Note`
- `easy int`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`Qwen3ASRLoader`、`Qwen3ASRTranscribe`、`NormalizeAudioLoudness`、`RunningHub_VoxCPM_LoadModel`、`OmniVoiceWhisperLoader`、`easy cleanGpuUsed`、`TextInput_`、`Fast Muter (rgthree)`、`RunningHub_VoxCPM_Generate`、`LongCatVoiceCloneTTS`、`OmniVoiceVoiceCloneTTS`、`SaveAudioMP3`、`OmniVoiceVoiceDesignTTS`、`LoadAudio`、`CR Prompt Text`、`InversionDemoLazyIndexSwitch`、`easy int`

**用到的条目**：CR Prompt Text、SaveAudioMP3、LoadAudio、TextInput_、InversionDemoLazyIndexSwitch、Qwen3ASRLoader、Qwen3ASRTranscribe、NormalizeAudioLoudness
