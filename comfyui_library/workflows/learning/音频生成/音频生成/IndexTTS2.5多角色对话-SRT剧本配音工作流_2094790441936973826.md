---
key: 音频生成/音频生成/IndexTTS2.5多角色对话-SRT剧本配音工作流_2094790441936973826.json
name: IndexTTS2.5多角色对话-SRT剧本配音工作流_2094790441936973826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/IndexTTS2.5多角色对话-SRT剧本配音工作流_2094790441936973826.json
hash: 09e7144b9d91deeb
coverage: 1
learned_at: 2026-10-18 17:45:35
nodes: [T8_IndexTTS25_ModelLoader, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_RoleLibrary, T8_IndexTTS25_DialogueGenerate, LoadAudio, LoadAudio, SaveAudio, T8_IndexTTS25_DialogueScript]
patterns: []
missing: []
---

# 音频生成/音频生成/IndexTTS2.5多角色对话-SRT剧本配音工作流_2094790441936973826.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/IndexTTS2.5多角色对话-SRT剧本配音工作流_2094790441936973826.json`

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
