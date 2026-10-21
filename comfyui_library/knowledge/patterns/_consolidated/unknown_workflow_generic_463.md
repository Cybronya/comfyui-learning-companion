---
name: unknown_workflow_generic_463
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9625
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, LayerUtility: PurgeVRAM V2, SaveAudio]
problems: []
missing: []
members: ["音频生成/音频生成/Qwen3-TTS,支持8种角色+音色设计_2015765564215529474.json", 音频生成/音频生成/Qwen3-TTS多人对话控制_2017150035233873921.json, 音频生成/音频生成/Qwen3-TTS生成多人对话：再现良子高铁点焖子名场面！_2015643221497487361.json, 音频生成/音频生成/支持8种角色+音色设计_2050145140706160641.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_463

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（音频生成/音频生成/Qwen3-TTS,支持8种角色+音色设计_2015765564215529474.json、音频生成/音频生成/Qwen3-TTS多人对话控制_2017150035233873921.json、音频生成/音频生成/Qwen3-TTS生成多人对话：再现良子高铁点焖子名场面！_2015643221497487361.json、音频生成/音频生成/支持8种角色+音色设计_2050145140706160641.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `Label (rgthree)` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `FB_Qwen3TTSLoadSpeaker` —— 1/4 个有
- `LoadAudio` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
