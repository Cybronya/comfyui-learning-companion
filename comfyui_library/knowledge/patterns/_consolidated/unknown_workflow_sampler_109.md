---
name: unknown_workflow_sampler_109
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.615
common_nodes: [LoadAudio, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAny, Qwen3ASRLoader, Qwen3ASRTranscribe, Qwen3ForcedAlign, Qwen3ForcedAlignerLoader, easy saveText]
problems: []
missing: []
members: [平台全量/Qwen3ASR语音转文本_2042577822962683905.json, 音频生成/音频生成/Qwen3ASR语音转文本带时间戳_2071420308040544257.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_109

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Qwen3ASR语音转文本_2042577822962683905.json、音频生成/音频生成/Qwen3ASR语音转文本带时间戳_2071420308040544257.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAny`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `Qwen3ForcedAlign`
- `Qwen3ForcedAlignerLoader`
- `easy saveText`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
