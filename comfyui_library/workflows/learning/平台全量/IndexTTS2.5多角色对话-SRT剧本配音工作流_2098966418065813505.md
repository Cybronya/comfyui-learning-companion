---
key: 平台全量/IndexTTS2.5多角色对话-SRT剧本配音工作流_2098966418065813505.json
name: IndexTTS2.5多角色对话-SRT剧本配音工作流_2098966418065813505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/IndexTTS2.5多角色对话-SRT剧本配音工作流_2098966418065813505.json
hash: d8ed036c74987bbf
coverage: 1
learned_at: 2026-11-14 00:32:35
nodes: [T8_IndexTTS25_ModelLoader, T8_IndexTTS25_VoiceProfile, T8_IndexTTS25_RoleLibrary, T8_IndexTTS25_DialogueGenerate, SaveAudio, T8_IndexTTS25_VoiceProfile, LoadAudio, LoadAudio, T8_IndexTTS25_DialogueScript]
patterns: []
missing: []
---

# 平台全量/IndexTTS2.5多角色对话-SRT剧本配音工作流_2098966418065813505.json

> 来源文件 `comfyui_library/workflows/平台全量/IndexTTS2.5多角色对话-SRT剧本配音工作流_2098966418065813505.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（9 个）：
- `T8_IndexTTS25_ModelLoader`
- `T8_IndexTTS25_VoiceProfile`
- `T8_IndexTTS25_RoleLibrary`
- `T8_IndexTTS25_DialogueGenerate`
- `SaveAudio`
- `T8_IndexTTS25_VoiceProfile`
- `LoadAudio`
- `LoadAudio`
- `T8_IndexTTS25_DialogueScript`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`T8_IndexTTS25_ModelLoader`、`T8_IndexTTS25_VoiceProfile`、`T8_IndexTTS25_RoleLibrary`、`T8_IndexTTS25_DialogueGenerate`、`SaveAudio`、`LoadAudio`、`T8_IndexTTS25_DialogueScript`

**用到的条目**：SaveAudio、LoadAudio、T8_IndexTTS25_DialogueGenerate、T8_IndexTTS25_DialogueScript、T8_IndexTTS25_ModelLoader、T8_IndexTTS25_RoleLibrary、T8_IndexTTS25_VoiceProfile、image_to_image_controlnet_face_detailer_lora
