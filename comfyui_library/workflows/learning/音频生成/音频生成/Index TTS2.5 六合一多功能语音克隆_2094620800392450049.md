---
key: 音频生成/音频生成/Index TTS2.5 六合一多功能语音克隆_2094620800392450049.json
name: Index TTS2.5 六合一多功能语音克隆_2094620800392450049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/Index TTS2.5 六合一多功能语音克隆_2094620800392450049.json
hash: 1b60924b272c3d0e
coverage: 0.96
learned_at: 2026-10-18 17:45:32
nodes: [LoadAudio, NormalizeAudioLoudness, NormalizeAudioLoudness, CR Prompt Text, Float, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_Generate, SaveAudioMP3, LoadAudio, NormalizeAudioLoudness, T8_IndexTTS25_ModelLoader, LoadAudio, CR Prompt Text, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_Generate, SaveAudioMP3, T8_IndexTTS25_Generate, SaveAudioMP3, LoadAudio, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_EmotionControl, NormalizeAudioLoudness, Float, T8_IndexTTS25_Generate, SaveAudioMP3, LoadAudio, T8_IndexTTS25_ModelLoader, CR Prompt Text, PrimitiveStringMultiline, T8_IndexTTS25_EmotionControl, NormalizeAudioLoudness, CR Prompt Text, LoadAudio, T8_IndexTTS25_Generate, T8_IndexTTS25_ModelLoader, NormalizeAudioLoudness, CR Prompt Text, T8_IndexTTS25_Pronunciation, CR Prompt Text, SaveAudioMP3, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_ModelLoader, SaveAudio, T8_IndexTTS25_DialogueGenerate, T8_IndexTTS25_RoleLibrary, T8_IndexTTS25_DialogueScript, LoadAudio, LoadAudio, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 音频生成/音频生成/Index TTS2.5 六合一多功能语音克隆_2094620800392450049.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/Index TTS2.5 六合一多功能语音克隆_2094620800392450049.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（50 个）：
- `LoadAudio`
- `NormalizeAudioLoudness`
- `NormalizeAudioLoudness`
- `CR Prompt Text`
- `Float`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_Generate`
- `SaveAudioMP3`
- `LoadAudio`
- `NormalizeAudioLoudness`
- `T8_IndexTTS25_ModelLoader`
- `LoadAudio`
- `CR Prompt Text`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_Generate`
- `SaveAudioMP3`
- `T8_IndexTTS25_Generate`
- `SaveAudioMP3`
- `LoadAudio`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_EmotionControl`
- `NormalizeAudioLoudness`
- `Float`
- `T8_IndexTTS25_Generate`
- `SaveAudioMP3`
- `LoadAudio`
- `T8_IndexTTS25_ModelLoader`
- `CR Prompt Text`
- `PrimitiveStringMultiline`
- `T8_IndexTTS25_EmotionControl`
- `NormalizeAudioLoudness`
- `CR Prompt Text`
- `LoadAudio`
- `T8_IndexTTS25_Generate`
- `T8_IndexTTS25_ModelLoader`
- `NormalizeAudioLoudness`
- `CR Prompt Text`
- `T8_IndexTTS25_Pronunciation`
- `CR Prompt Text`
- `SaveAudioMP3`
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_ModelLoader`
- `SaveAudio`
- `T8_IndexTTS25_DialogueGenerate`
- `T8_IndexTTS25_RoleLibrary`
- `T8_IndexTTS25_DialogueScript`
- `LoadAudio`
- `LoadAudio`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **96%**（48/50）

**有卡**：`LoadAudio`、`NormalizeAudioLoudness`、`CR Prompt Text`、`Float`、`T8_IndexTTS25_EmotionControl`、`T8_IndexTTS25_Generate`、`SaveAudioMP3`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_Pronunciation`、`T8_IndexTTS25_VoiceProfile`、`SaveAudio`、`T8_IndexTTS25_DialogueGenerate`、`T8_IndexTTS25_RoleLibrary`、`T8_IndexTTS25_DialogueScript`

**用到的条目**：CR Prompt Text、SaveAudio、SaveAudioMP3、LoadAudio、Float、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader
