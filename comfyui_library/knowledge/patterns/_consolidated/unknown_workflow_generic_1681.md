---
name: unknown_workflow_generic_1681
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7835
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, FB_Qwen3TTSVoiceDesign, LayerUtility: PurgeVRAM V2, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3-tts多人音频对话_2051855649033736193.json, 音频生成/音频生成/qwen tts 音色设计+多人对话_2015471317927075841.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1681

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3-tts多人音频对话_2051855649033736193.json、音频生成/音频生成/qwen tts 音色设计+多人对话_2015471317927075841.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `FB_Qwen3TTSVoiceDesign`
- `LayerUtility: PurgeVRAM V2`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `PrimitiveString` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `String` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
