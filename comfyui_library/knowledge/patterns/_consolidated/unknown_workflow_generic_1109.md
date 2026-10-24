---
name: unknown_workflow_generic_1109
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, LayerUtility: PurgeVRAM V2, PreviewAudio]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3-TTS多角色对话_2015354185604141057.json, 音频生成/音频生成/Qwen3-TTS生成多人对话：再现良子高铁点焖子名场面！_2015643221497487361.json, 音频生成/音频生成/动漫角色声音生成_2026586774646034433.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1109

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（音频生成/音频生成/Qwen3-TTS多角色对话_2015354185604141057.json、音频生成/音频生成/Qwen3-TTS生成多人对话：再现良子高铁点焖子名场面！_2015643221497487361.json、音频生成/音频生成/动漫角色声音生成_2026586774646034433.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `PreviewAudio`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `SaveAudioMP3` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
