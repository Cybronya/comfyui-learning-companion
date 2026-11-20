---
name: unknown_workflow_lora_sampler_unet_389
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6695
common_nodes: [BasicScheduler, CLIPLoader, ConditioningZeroOut, GetNode, ImageFromBatch, ImageStitch, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, ResolutionSelector, SaveImage, SelfLiftAvatarH3Sampler, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/Minimax_H3_人物四视图生成_2110189002128187393.json, 视频生成/图生视频/Minmax_h3_人物多表情_2113091140340772866.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_389

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Minimax_H3_人物四视图生成_2110189002128187393.json、视频生成/图生视频/Minmax_h3_人物多表情_2113091140340772866.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `ImageFromBatch`
- `ImageStitch`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `SaveImage`
- `SelfLiftAvatarH3Sampler`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
