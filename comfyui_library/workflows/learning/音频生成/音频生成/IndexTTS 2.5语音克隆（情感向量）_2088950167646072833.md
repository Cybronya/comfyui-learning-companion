---
key: 音频生成/音频生成/IndexTTS 2.5语音克隆（情感向量）_2088950167646072833.json
name: IndexTTS 2.5语音克隆（情感向量）_2088950167646072833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5语音克隆（情感向量）_2088950167646072833.json
hash: 57ddf5747e007a25
coverage: 1
learned_at: 2026-10-18 17:45:34
nodes: [T8_IndexTTS25_EmotionControl, NormalizeAudioLoudness, LoadAudio, Float, Float, Float, Float, Float, Float, Float, CR Prompt Text, Float, Float, T8_IndexTTS25_ModelLoader, T8_IndexTTS25_Generate, SaveAudioMP3]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS 2.5语音克隆（情感向量）_2088950167646072833.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5语音克隆（情感向量）_2088950167646072833.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（16 个）：
- `T8_IndexTTS25_EmotionControl`
- `NormalizeAudioLoudness`
- `LoadAudio`
- `Float`
- `Float`
- `Float`
- `Float`
- `Float`
- `Float`
- `Float`
- `CR Prompt Text`
- `Float`
- `Float`
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_Generate`
- `SaveAudioMP3`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`T8_IndexTTS25_EmotionControl`、`NormalizeAudioLoudness`、`LoadAudio`、`Float`、`CR Prompt Text`、`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_Generate`、`SaveAudioMP3`

**用到的条目**：CR Prompt Text、SaveAudioMP3、LoadAudio、Float、T8_IndexTTS25_EmotionControl、T8_IndexTTS25_Generate、T8_IndexTTS25_ModelLoader、NormalizeAudioLoudness
