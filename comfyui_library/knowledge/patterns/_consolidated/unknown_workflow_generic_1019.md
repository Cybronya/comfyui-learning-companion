---
name: unknown_workflow_generic_1019
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8685
common_nodes: [FB_Qwen3TTSDialogueInference, FB_Qwen3TTSRoleBank, FB_Qwen3TTSVoiceClonePrompt, Qwen3TTSModelLoader, Qwen3TTSVoiceDesign, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/余温-设计音色多人对话配音工作流_2107510906858065922.json, 音频生成/音频生成/电商一键生成多人话音频 Qwen3 TTS_2017238871485976577.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1019

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/余温-设计音色多人对话配音工作流_2107510906858065922.json、音频生成/音频生成/电商一键生成多人话音频 Qwen3 TTS_2017238871485976577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `FB_Qwen3TTSDialogueInference`
- `FB_Qwen3TTSRoleBank`
- `FB_Qwen3TTSVoiceClonePrompt`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceDesign`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `Qwen3TTSVoicePresets` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
