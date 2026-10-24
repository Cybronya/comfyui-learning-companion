---
name: unknown_workflow_lora_sampler_unet_318
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.443
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, GetNode, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, 孤海注释, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流_2086774898759917569.json, 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频工作流_2086348400169148418.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_318

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流_2086774898759917569.json、视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频工作流_2086348400169148418.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：44%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `GetNode`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `孤海注释`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `MiniMaxChunkFeedForward` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `MiniMaxLowVRAMAttention` —— 1/2 个有
- `PT_H3ConcatAVLatent` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `VAEEncodeAudio` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
