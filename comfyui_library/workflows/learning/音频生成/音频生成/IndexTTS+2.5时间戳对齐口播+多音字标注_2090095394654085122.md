---
key: 音频生成/音频生成/IndexTTS+2.5时间戳对齐口播+多音字标注_2090095394654085122.json
name: IndexTTS+2.5时间戳对齐口播+多音字标注_2090095394654085122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS+2.5时间戳对齐口播+多音字标注_2090095394654085122.json
hash: fdd4db2ad0b3f7e6
coverage: 0.928571
learned_at: 2026-10-18 17:45:35
nodes: [T8_IndexTTS25_ModelLoader, LoadAudio, AudioCrop, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_DialogueGenerate, T8_IndexTTS25_RoleLibrary, T8_IndexTTS25_DialogueScript, SaveAudio, CR Prompt Text, CR Prompt Text, RHLLMChatNode, CR Prompt Text, T8_IndexTTS25_Pronunciation, JjkText]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS+2.5时间戳对齐口播+多音字标注_2090095394654085122.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS+2.5时间戳对齐口播+多音字标注_2090095394654085122.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（14 个）：
- `T8_IndexTTS25_ModelLoader`
- `LoadAudio`
- `AudioCrop`
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_DialogueGenerate`
- `T8_IndexTTS25_RoleLibrary`
- `T8_IndexTTS25_DialogueScript`
- `SaveAudio`
- `CR Prompt Text`
- `CR Prompt Text`
- `RHLLMChatNode`
- `CR Prompt Text`
- `T8_IndexTTS25_Pronunciation`
- `JjkText`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`T8_IndexTTS25_ModelLoader`、`LoadAudio`、`AudioCrop`、`T8_IndexTTS25_VoiceProfile`、`T8_IndexTTS25_DialogueGenerate`、`T8_IndexTTS25_RoleLibrary`、`T8_IndexTTS25_DialogueScript`、`SaveAudio`、`CR Prompt Text`、`RHLLMChatNode`、`T8_IndexTTS25_Pronunciation`

**用到的条目**：CR Prompt Text、SaveAudio、LoadAudio、RHLLMChatNode、AudioCrop、T8_IndexTTS25_ModelLoader、T8_IndexTTS25_DialogueGenerate、T8_IndexTTS25_DialogueScript
