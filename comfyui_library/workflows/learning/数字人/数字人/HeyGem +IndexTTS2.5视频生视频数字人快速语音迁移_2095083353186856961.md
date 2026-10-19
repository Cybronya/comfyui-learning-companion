---
key: 数字人/数字人/HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移_2095083353186856961.json
name: HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移_2095083353186856961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移_2095083353186856961.json
hash: 890f6c4b21ad5a5b
coverage: 0.857143
learned_at: 2026-10-18 22:17:10
nodes: [Float, T8_IndexTTS25_ModelLoader, SoundFlow_TrimAudio, AudioSeparation, NormalizeAudioLoudness, CR Prompt Text, NormalizeAudioLoudness, WujiCleaner, RH_HeyGemNode, SaveAudioMP3, Fast Groups Bypasser (rgthree), Any Switch (rgthree), easy cleanGpuUsed, GetVideoComponents, LoadVideo, Fast Groups Bypasser (rgthree), SaveVideo, LoadAudio, LoadAudio, T8_IndexTTS25_Generate, T8_IndexTTS25_EmotionControl]
patterns: []
missing: []
---

# 数字人/数字人/HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移_2095083353186856961.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移_2095083353186856961.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（21 个）：
- `Float`
- `T8_IndexTTS25_ModelLoader`
- `SoundFlow_TrimAudio`
- `AudioSeparation`
- `NormalizeAudioLoudness`
- `CR Prompt Text`
- `NormalizeAudioLoudness`
- `WujiCleaner`
- `RH_HeyGemNode`
- `SaveAudioMP3`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `easy cleanGpuUsed`
- `GetVideoComponents`
- `LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `SaveVideo`
- `LoadAudio`
- `LoadAudio`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_EmotionControl`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`Float`、`T8_IndexTTS25_ModelLoader`、`SoundFlow_TrimAudio`、`AudioSeparation`、`NormalizeAudioLoudness`、`CR Prompt Text`、`WujiCleaner`、`RH_HeyGemNode`、`SaveAudioMP3`、`easy cleanGpuUsed`、`GetVideoComponents`、`LoadVideo`、`SaveVideo`、`LoadAudio`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_EmotionControl`

**用到的条目**：CR Prompt Text、SaveVideo、SaveAudioMP3、GetVideoComponents、LoadAudio、LoadVideo、Float、WujiCleaner
