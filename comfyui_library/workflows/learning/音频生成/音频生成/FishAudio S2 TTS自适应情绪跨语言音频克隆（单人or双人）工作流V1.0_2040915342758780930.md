---
key: 音频生成/音频生成/FishAudio S2 TTS自适应情绪跨语言音频克隆（单人or双人）工作流V1.0_2040915342758780930.json
name: FishAudio S2 TTS自适应情绪跨语言音频克隆（单人or双人）工作流V1.0_2040915342758780930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/FishAudio S2 TTS自适应情绪跨语言音频克隆（单人or双人）工作流V1.0_2040915342758780930.json
hash: 2f641fd85aeeb93c
coverage: 0.6875
learned_at: 2026-10-18 02:28:39
nodes: [FishS2VoiceCloneTTS, RHHiddenNodes, ShowText|pysssss, SaveAudioMP3, WujiCleaner, WujiCleaner, WujiAudioLoader, WujiAudioLoader, FishS2MultiSpeakerTTS, RHHiddenNodes, SaveAudioMP3, PrimitiveStringMultiline, WujiAudioLoader, PrimitiveStringMultiline, Fast Groups Muter (rgthree), ShowText|pysssss]
patterns: []
missing: []
---

# 音频生成/音频生成/FishAudio S2 TTS自适应情绪跨语言音频克隆（单人or双人）工作流V1.0_2040915342758780930.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/FishAudio S2 TTS自适应情绪跨语言音频克隆（单人or双人）工作流V1.0_2040915342758780930.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（16 个）：
- `FishS2VoiceCloneTTS`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `SaveAudioMP3`
- `WujiCleaner`
- `WujiCleaner`
- `WujiAudioLoader`
- `WujiAudioLoader`
- `FishS2MultiSpeakerTTS`
- `RHHiddenNodes`
- `SaveAudioMP3`
- `PrimitiveStringMultiline`
- `WujiAudioLoader`
- `PrimitiveStringMultiline`
- `Fast Groups Muter (rgthree)`
- `ShowText|pysssss`

## 知识

覆盖率 **69%**（11/16）

**有卡**：`FishS2VoiceCloneTTS`、`RHHiddenNodes`、`SaveAudioMP3`、`WujiCleaner`、`WujiAudioLoader`、`FishS2MultiSpeakerTTS`

**用到的条目**：SaveAudioMP3、RHHiddenNodes、WujiAudioLoader、WujiCleaner、FishS2VoiceCloneTTS、FishS2MultiSpeakerTTS、sd15-t2i-basic、sd15-t2i-lora
