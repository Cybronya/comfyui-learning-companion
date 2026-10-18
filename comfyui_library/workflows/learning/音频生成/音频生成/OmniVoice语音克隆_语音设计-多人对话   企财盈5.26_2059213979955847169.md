---
key: 音频生成/音频生成/OmniVoice语音克隆_语音设计-多人对话   企财盈5.26_2059213979955847169.json
name: OmniVoice语音克隆_语音设计-多人对话   企财盈5.26_2059213979955847169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/OmniVoice语音克隆_语音设计-多人对话   企财盈5.26_2059213979955847169.json
hash: b7f01f9c1b0e7887
coverage: 0.8125
learned_at: 2026-10-18 03:04:53
nodes: [Apply Whisper, OmniVoiceMultiSpeakerTTS, LoadAudio, CR Prompt Text, AudioSeparation, Apply Whisper, LoadAudio, AudioSeparation, AudioSeparation, CR Prompt Text, OmniVoiceVoiceDesignTTS, CR Prompt Text, SaveAudio, SaveAudio, LayerUtility: TextJoin, Fast Groups Bypasser (rgthree), OmniVoiceLongformTTS, CR Prompt Text, MarkdownNote, CR Prompt Text, easy showAnything, CR Prompt Text, OmniVoiceWhisperLoader, easy showAnything, easy showAnything, MarkdownNote, Comfly_LLm_API, SaveAudio, LoadAudio, CR Prompt Text, Qwen3_VQA, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
---

# 音频生成/音频生成/OmniVoice语音克隆_语音设计-多人对话   企财盈5.26_2059213979955847169.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/OmniVoice语音克隆_语音设计-多人对话   企财盈5.26_2059213979955847169.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（32 个）：
- `Apply Whisper`
- `OmniVoiceMultiSpeakerTTS`
- `LoadAudio`
- `CR Prompt Text`
- `AudioSeparation`
- `Apply Whisper`
- `LoadAudio`
- `AudioSeparation`
- `AudioSeparation`
- `CR Prompt Text`
- `OmniVoiceVoiceDesignTTS`
- `CR Prompt Text`
- `SaveAudio`
- `SaveAudio`
- `LayerUtility: TextJoin`
- `Fast Groups Bypasser (rgthree)`
- `OmniVoiceLongformTTS`
- `CR Prompt Text`
- `MarkdownNote`
- `CR Prompt Text`
- `easy showAnything`
- `CR Prompt Text`
- `OmniVoiceWhisperLoader`
- `easy showAnything`
- `easy showAnything`
- `MarkdownNote`
- `Comfly_LLm_API`
- `SaveAudio`
- `LoadAudio`
- `CR Prompt Text`
- `Qwen3_VQA`
- `RH_LLMAPI_Pro_Node`

## 知识

覆盖率 **81%**（26/32）

**有卡**：`Apply Whisper`、`OmniVoiceMultiSpeakerTTS`、`LoadAudio`、`CR Prompt Text`、`AudioSeparation`、`OmniVoiceVoiceDesignTTS`、`SaveAudio`、`LayerUtility: TextJoin`、`OmniVoiceLongformTTS`、`OmniVoiceWhisperLoader`、`Comfly_LLm_API`、`Qwen3_VQA`、`RH_LLMAPI_Pro_Node`

**用到的条目**：CR Prompt Text、SaveAudio、LoadAudio、Qwen3_VQA、RH_LLMAPI_Pro_Node、AudioSeparation、OmniVoiceVoiceDesignTTS、Comfly_LLm_API
