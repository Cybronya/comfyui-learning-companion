---
key: 音频生成/音频生成/多人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS等 6个模型_2042818567011307521.json
name: 多人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS等 6个模型_2042818567011307521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/多人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS等 6个模型_2042818567011307521.json
hash: 260cb8128597ef4c
coverage: 0.808511
learned_at: 2026-10-18 02:28:48
nodes: [CR Text, CR Text, CR Text, RunningHub_VoxCPM_MultiSpeaker, CR Text, RunningHub_VoxCPM_LoadModel, Note, CR Text, CR Text, LayerUtility: TextJoin, RH_LLMAPI_Pro_Node, SaveText|pysssss, CR Prompt Text, easy showAnything, SaveAudio, NormalizeAudioLoudness, NormalizeAudioLoudness, SaveAudioMP3, Qwen3ASRTranscribe, Qwen3ASRTranscribe, CR Prompt Text, LongCatMultiSpeakerTTS, Qwen3ASRLoader, Note, Qwen3ASRTranscribe, Qwen3ASRTranscribe, Qwen3ASRLoader, OmniVoiceMultiSpeakerTTS, SaveAudio, CR Text, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, PrimitiveStringMultiline, CR Prompt Text, PrimitiveStringMultiline, CR Prompt Text, LoadAudio, LoadAudio, CR Prompt Text, SaveAudio, IndexTTS2Run, Note, Note, SaveAudio, Note, AudioCrop, AudioCrop, AudioCrop, CR Prompt Text, FishS2MultiSpeakerTTS, LoadAudio, LoadAudio, LoadAudio, Note, Note, easy float, easy float, easy float, easy float, easy float, CR Prompt Text, easy int, CR Prompt Text, CR Prompt Text, CR Prompt Text, easy showAnything, FB_Qwen3TTSVoiceClonePrompt, WhisperSTT, SaveAudio, Note, Note, FB_Qwen3TTSVoiceClonePrompt, easy showAnything, WhisperSTT, WhisperSTT, FB_Qwen3TTSVoiceClonePrompt, easy showAnything, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, FB_Qwen3TTSRoleBank, VRAMReserver, LoadAudio, LoadAudio, LoadAudio, FB_Qwen3TTSDialogueInference, Note, Note, Fast Groups Bypasser (rgthree), LoadAudio, SaveAudio]
patterns: []
missing: []
---

# 音频生成/音频生成/多人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS等 6个模型_2042818567011307521.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/多人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS等 6个模型_2042818567011307521.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（94 个）：
- `CR Text`
- `CR Text`
- `CR Text`
- `RunningHub_VoxCPM_MultiSpeaker`
- `CR Text`
- `RunningHub_VoxCPM_LoadModel`
- `Note`
- `CR Text`
- `CR Text`
- `LayerUtility: TextJoin`
- `RH_LLMAPI_Pro_Node`
- `SaveText|pysssss`
- `CR Prompt Text`
- `easy showAnything`
- `SaveAudio`
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `SaveAudioMP3`
- `Qwen3ASRTranscribe`
- `Qwen3ASRTranscribe`
- `CR Prompt Text`
- `LongCatMultiSpeakerTTS`
- `Qwen3ASRLoader`
- `Note`
- `Qwen3ASRTranscribe`
- `Qwen3ASRTranscribe`
- `Qwen3ASRLoader`
- `OmniVoiceMultiSpeakerTTS`
- `SaveAudio`
- `CR Text`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `CR Prompt Text`
- `PrimitiveStringMultiline`
- `CR Prompt Text`
- `LoadAudio`
- `LoadAudio`
- `CR Prompt Text`
- `SaveAudio`
- `IndexTTS2Run`
- `Note`
- `Note`
- `SaveAudio`
- `Note`
- `AudioCrop`
- `AudioCrop`
- `AudioCrop`
- `CR Prompt Text`
- `FishS2MultiSpeakerTTS`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `Note`
- `Note`
- `easy float`
- `easy float`
- `easy float`
- `easy float`
- `easy float`
- `CR Prompt Text`
- `easy int`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `easy showAnything`
- `FB_Qwen3TTSVoiceClonePrompt`
- `WhisperSTT`
- `SaveAudio`
- `Note`
- `Note`
- `FB_Qwen3TTSVoiceClonePrompt`
- `easy showAnything`
- `WhisperSTT`
- `WhisperSTT`
- `FB_Qwen3TTSVoiceClonePrompt`
- `easy showAnything`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `FB_Qwen3TTSRoleBank`
- `VRAMReserver`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `FB_Qwen3TTSDialogueInference`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`
- `SaveAudio`

## 知识

覆盖率 **81%**（76/94）

**有卡**：`CR Text`、`RunningHub_VoxCPM_MultiSpeaker`、`RunningHub_VoxCPM_LoadModel`、`LayerUtility: TextJoin`、`RH_LLMAPI_Pro_Node`、`SaveText|pysssss`、`CR Prompt Text`、`SaveAudio`、`NormalizeAudioLoudness`、`SaveAudioMP3`、`Qwen3ASRTranscribe`、`LongCatMultiSpeakerTTS`、`Qwen3ASRLoader`、`OmniVoiceMultiSpeakerTTS`、`LoadAudio`、`IndexTTS2Run`、`AudioCrop`、`FishS2MultiSpeakerTTS`、`easy float`、`easy int`、`FB_Qwen3TTSVoiceClonePrompt`、`WhisperSTT`、`LayerUtility: PurgeVRAM V2`、`FB_Qwen3TTSRoleBank`、`VRAMReserver`、`FB_Qwen3TTSDialogueInference`

**用到的条目**：FB_Qwen3TTSVoiceClonePrompt、CR Prompt Text、SaveAudio、SaveAudioMP3、SaveText|pysssss、LoadAudio、RH_LLMAPI_Pro_Node、AudioCrop
