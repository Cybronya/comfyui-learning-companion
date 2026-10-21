---
name: unknown_workflow_generic_775
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CR Prompt Text, SaveAudio, TDQwen3TTSModelLoader, TDQwen3TTSVoiceDesign]
problems: []
missing: []
members: [图片生成/文生图/N06-Qwen3TTS音频创造_2102308187058823169.json, 音频生成/音频生成/N06-Qwen3TTS音频创造_2101875104526454786.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_775

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/N06-Qwen3TTS音频创造_2102308187058823169.json、音频生成/音频生成/N06-Qwen3TTS音频创造_2101875104526454786.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `SaveAudio`
- `TDQwen3TTSModelLoader`
- `TDQwen3TTSVoiceDesign`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
