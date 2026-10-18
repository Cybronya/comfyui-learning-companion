---
key: 音频生成/音频生成/单人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS、Fish Audio、Qwen3 TTS_2042810459358760962.json
name: 单人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS、Fish Audio、Qwen3 TTS_2042810459358760962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/单人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS、Fish Audio、Qwen3 TTS_2042810459358760962.json
hash: 27e7291f211a03e1
coverage: 0.818182
learned_at: 2026-10-18 02:28:47
nodes: [RunningHub_VoxCPM_LoadModel, CR Text, Note, CR Text, RunningHub_VoxCPM_Generate, easy showAnything, CR Text, RunningHub_VoxCPM_LoadModel, RunningHub_VoxCPM_Generate, LayerUtility: TextJoin, CR Prompt Text, CR Text, RH_LLMAPI_Pro_Node, SaveAudio, CR Text, CR Text, CR Prompt Text, IndexTTS2Run, Note, SaveAudio, CR Prompt Text, Qwen3TTSVoiceClone, Apply Whisper, ShowText|pysssss, SaveAudio, CR Prompt Text, Qwen3TTSModelLoader, ShowText|pysssss, Apply Whisper, SaveAudio, Qwen3TTSModelLoader, Qwen3TTSVoiceClone, easy showAnything, RunningHub SeedXPro Translator, CR Prompt Text, Audio To Text (mtb), easy clearCacheAll, ShowText|pysssss, Load Whisper (mtb), FishS2VoiceCloneTTS, CR Prompt Text, SaveAudio, Note, Qwen3ASRLoader, Qwen3ASRTranscribe, Qwen3ASRLoader, Qwen3ASRTranscribe, OmniVoiceLongformTTS, SaveAudio, OmniVoiceVoiceCloneTTS, SaveAudio, CR Text, CR Text, easy showAnything, RunningHub SeedXPro Translator, NormalizeAudioLoudness, CR Prompt Text, SaveAudio, SaveAudioMP3, Qwen3ASRLoader, Qwen3ASRTranscribe, LongCatVoiceCloneTTS, Note, Fast Groups Bypasser (rgthree), Note, Note, Note, LoadAudio, SaveAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio]
patterns: []
missing: []
---

# 音频生成/音频生成/单人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS、Fish Audio、Qwen3 TTS_2042810459358760962.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/单人声音克隆合集--VoxCPM2、LongCat、OmniVoice、indexTTS、Fish Audio、Qwen3 TTS_2042810459358760962.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（77 个）：
- `RunningHub_VoxCPM_LoadModel`
- `CR Text`
- `Note`
- `CR Text`
- `RunningHub_VoxCPM_Generate`
- `easy showAnything`
- `CR Text`
- `RunningHub_VoxCPM_LoadModel`
- `RunningHub_VoxCPM_Generate`
- `LayerUtility: TextJoin`
- `CR Prompt Text`
- `CR Text`
- `RH_LLMAPI_Pro_Node`
- `SaveAudio`
- `CR Text`
- `CR Text`
- `CR Prompt Text`
- `IndexTTS2Run`
- `Note`
- `SaveAudio`
- `CR Prompt Text`
- `Qwen3TTSVoiceClone`
- `Apply Whisper`
- `ShowText|pysssss`
- `SaveAudio`
- `CR Prompt Text`
- `Qwen3TTSModelLoader`
- `ShowText|pysssss`
- `Apply Whisper`
- `SaveAudio`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceClone`
- `easy showAnything`
- `RunningHub SeedXPro Translator`
- `CR Prompt Text`
- `Audio To Text (mtb)`
- `easy clearCacheAll`
- `ShowText|pysssss`
- `Load Whisper (mtb)`
- `FishS2VoiceCloneTTS`
- `CR Prompt Text`
- `SaveAudio`
- `Note`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `OmniVoiceLongformTTS`
- `SaveAudio`
- `OmniVoiceVoiceCloneTTS`
- `SaveAudio`
- `CR Text`
- `CR Text`
- `easy showAnything`
- `RunningHub SeedXPro Translator`
- `NormalizeAudioLoudness`
- `CR Prompt Text`
- `SaveAudio`
- `SaveAudioMP3`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `LongCatVoiceCloneTTS`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `Note`
- `LoadAudio`
- `SaveAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`

## 知识

覆盖率 **82%**（63/77）

**有卡**：`RunningHub_VoxCPM_LoadModel`、`CR Text`、`RunningHub_VoxCPM_Generate`、`LayerUtility: TextJoin`、`CR Prompt Text`、`RH_LLMAPI_Pro_Node`、`SaveAudio`、`IndexTTS2Run`、`Qwen3TTSVoiceClone`、`Apply Whisper`、`Qwen3TTSModelLoader`、`RunningHub SeedXPro Translator`、`Audio To Text (mtb)`、`easy clearCacheAll`、`Load Whisper (mtb)`、`FishS2VoiceCloneTTS`、`Qwen3ASRLoader`、`Qwen3ASRTranscribe`、`OmniVoiceLongformTTS`、`OmniVoiceVoiceCloneTTS`、`NormalizeAudioLoudness`、`SaveAudioMP3`、`LongCatVoiceCloneTTS`、`LoadAudio`

**用到的条目**：RunningHub SeedXPro Translator、CR Prompt Text、SaveAudio、SaveAudioMP3、LoadAudio、RH_LLMAPI_Pro_Node、IndexTTS2Run、FishS2VoiceCloneTTS
