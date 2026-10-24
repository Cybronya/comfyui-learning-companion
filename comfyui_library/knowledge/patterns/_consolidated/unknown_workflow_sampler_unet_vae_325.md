---
name: unknown_workflow_sampler_unet_vae_325
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9195
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ComfyNumberConvert, CreateVideo, KSamplerSelect, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, easy int, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/音画同出-多图参考生视频-minimax_h3版_2109948293609517058.json, 视频生成/文生视频/02-04-01-爱小墨-高级流-音画同出-文生视频v1.0_2085907402355990529.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_325

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/音画同出-多图参考生视频-minimax_h3版_2109948293609517058.json、视频生成/文生视频/02-04-01-爱小墨-高级流-音画同出-文生视频v1.0_2085907402355990529.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `EmptyMiniMaxH3LatentAV` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MiniMaxChunkFeedForward` —— 1/2 个有
- `MiniMaxH3AddGuide` —— 1/2 个有
- `MiniMaxH3ImageToVideo` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `MiniMaxH3ReferenceToVideo` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `MiniMaxLowVRAMAttention` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
