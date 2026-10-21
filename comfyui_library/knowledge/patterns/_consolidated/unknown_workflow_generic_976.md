---
name: unknown_workflow_generic_976
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.626
common_nodes: [PrimitiveStringMultiline, Qwen3TTSModelLoader, Qwen3TTSVoiceDesign, SaveAudio]
problems: []
missing: []
members: [音频生成/音频生成/Qwen3-TTS-VoiceDesign（声音设计）_2014524194331037697.json, 音频生成/音频生成/Qwen3TTS声音设计工作流_2105216069802749954.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_976

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（音频生成/音频生成/Qwen3-TTS-VoiceDesign（声音设计）_2014524194331037697.json、音频生成/音频生成/Qwen3TTS声音设计工作流_2105216069802749954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `PrimitiveStringMultiline`
- `Qwen3TTSModelLoader`
- `Qwen3TTSVoiceDesign`
- `SaveAudio`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
