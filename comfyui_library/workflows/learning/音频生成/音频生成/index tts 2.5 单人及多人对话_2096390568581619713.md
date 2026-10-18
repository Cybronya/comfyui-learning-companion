---
key: 音频生成/音频生成/index tts 2.5 单人及多人对话_2096390568581619713.json
name: index tts 2.5 单人及多人对话_2096390568581619713
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/index tts 2.5 单人及多人对话_2096390568581619713.json
hash: aec2bc9d04c0018a
coverage: 1
learned_at: 2026-10-18 17:45:48
nodes: [T8_IndexTTS25_ModelLoader, LoadAudio, T8_IndexTTS25_Generate, NormalizeAudioLoudness, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_EmotionControl, SaveAudioMP3, NormalizeAudioLoudness, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_EmotionControl, T8_IndexTTS25_RoleLibrary, T8_IndexTTS25_ModelLoader, LoadAudio, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_VoiceProfile, NormalizeAudioLoudness, LoadAudio, SaveAudioMP3, T8_IndexTTS25_DialogueScript, SaveAudioMP3, T8_IndexTTS25_DialogueGenerate]
patterns: []
missing: []
---

# 音频生成/音频生成/index tts 2.5 单人及多人对话_2096390568581619713.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/index tts 2.5 单人及多人对话_2096390568581619713.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（21 个）：
- `T8_IndexTTS25_ModelLoader`
- `LoadAudio`
- `T8_IndexTTS25_Generate`
- `NormalizeAudioLoudness`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_EmotionControl`
- `SaveAudioMP3`
- `NormalizeAudioLoudness`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_EmotionControl`
- `T8_IndexTTS25_RoleLibrary`
- `T8_IndexTTS25_ModelLoader`
- `LoadAudio`
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_VoiceProfile`
- `NormalizeAudioLoudness`
- `LoadAudio`
- `SaveAudioMP3`
- `T8_IndexTTS25_DialogueScript`
- `SaveAudioMP3`
- `T8_IndexTTS25_DialogueGenerate`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`T8_IndexTTS25_ModelLoader`、`LoadAudio`、`T8_IndexTTS25_Generate`、`NormalizeAudioLoudness`、`T8_IndexTTS25_EmotionControl`、`SaveAudioMP3`、`T8_IndexTTS25_RoleLibrary`、`T8_IndexTTS25_VoiceProfile`、`T8_IndexTTS25_DialogueScript`、`T8_IndexTTS25_DialogueGenerate`

**用到的条目**：SaveAudioMP3、LoadAudio、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、NormalizeAudioLoudness、T8_IndexTTS25_DialogueGenerate、T8_IndexTTS25_DialogueScript
