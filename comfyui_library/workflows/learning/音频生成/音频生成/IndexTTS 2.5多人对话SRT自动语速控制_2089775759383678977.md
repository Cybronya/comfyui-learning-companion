---
key: 音频生成/音频生成/IndexTTS 2.5多人对话SRT自动语速控制_2089775759383678977.json
name: IndexTTS 2.5多人对话SRT自动语速控制_2089775759383678977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5多人对话SRT自动语速控制_2089775759383678977.json
hash: 8bfdd641bc28fb74
coverage: 1
learned_at: 2026-10-18 17:45:32
nodes: [T8_IndexTTS25_ModelLoader, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_RoleLibrary, T8_IndexTTS25_DialogueGenerate, LoadAudio, LoadAudio, SaveAudio, T8_IndexTTS25_DialogueScript]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS 2.5多人对话SRT自动语速控制_2089775759383678977.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS 2.5多人对话SRT自动语速控制_2089775759383678977.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（9 个）：
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_RoleLibrary`
- `T8_IndexTTS25_DialogueGenerate`
- `LoadAudio`
- `LoadAudio`
- `SaveAudio`
- `T8_IndexTTS25_DialogueScript`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_VoiceProfile`、`T8_IndexTTS25_RoleLibrary`、`T8_IndexTTS25_DialogueGenerate`、`LoadAudio`、`SaveAudio`、`T8_IndexTTS25_DialogueScript`

**用到的条目**：SaveAudio、LoadAudio、T8_IndexTTS25_ModelLoader、T8_IndexTTS25_DialogueGenerate、T8_IndexTTS25_DialogueScript、T8_IndexTTS25_RoleLibrary、T8_IndexTTS25_VoiceProfile、sd15-t2i-basic
