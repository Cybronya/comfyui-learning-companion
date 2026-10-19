---
key: 数字人/数字人/HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移（测试）_2100411233353682945.json
name: HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移（测试）_2100411233353682945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移（测试）_2100411233353682945.json
hash: c8467da2e1de3ffe
coverage: 0.857143
learned_at: 2026-10-19 00:19:09
nodes: [T8_IndexTTS25_ModelLoader, AudioSeparation, NormalizeAudioLoudness, NormalizeAudioLoudness, WujiCleaner, RH_HeyGemNode, SaveAudioMP3, Fast Groups Bypasser (rgthree), Any Switch (rgthree), easy cleanGpuUsed, GetVideoComponents, SaveVideo, T8_IndexTTS25_Generate, T8_IndexTTS25_EmotionControl, SoundFlow_TrimAudio, LoadVideo, LoadAudio, CR Prompt Text, Float, Fast Groups Bypasser (rgthree), LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移（测试）_2100411233353682945.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/HeyGem +IndexTTS2.5视频生视频数字人快速语音迁移（测试）_2100411233353682945.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（21 个）：
- `T8_IndexTTS25_ModelLoader`
- `AudioSeparation`
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `WujiCleaner`
- `RH_HeyGemNode`
- `SaveAudioMP3`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `easy cleanGpuUsed`
- `GetVideoComponents`
- `SaveVideo`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_EmotionControl`
- `SoundFlow_TrimAudio`
- `LoadVideo`
- `LoadAudio`
- `CR Prompt Text`
- `Float`
- `Fast Groups Bypasser (rgthree)`
- `LoadAudio`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`T8_IndexTTS25_ModelLoader`、`AudioSeparation`、`NormalizeAudioLoudness`、`WujiCleaner`、`RH_HeyGemNode`、`SaveAudioMP3`、`easy cleanGpuUsed`、`GetVideoComponents`、`SaveVideo`、`T8_IndexTTS25_Generate`、`T8_IndexTTS25_EmotionControl`、`SoundFlow_TrimAudio`、`LoadVideo`、`LoadAudio`、`CR Prompt Text`、`Float`

**用到的条目**：CR Prompt Text、SaveVideo、SaveAudioMP3、GetVideoComponents、LoadAudio、LoadVideo、Float、WujiCleaner
