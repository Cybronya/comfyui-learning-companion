---
name: unknown_workflow_sampler_unet_vae_326
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.865
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, EasyCache, KSamplerSelect, MiniMaxH3ImageToVideo, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 FL2VA开源版-文生视频_首尾视频（本地版）_2084658021799653378.json, 视频生成/文生视频/MiniMax H3 文生视频_2084489178611539970.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_326

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 FL2VA开源版-文生视频_首尾视频（本地版）_2084658021799653378.json、视频生成/文生视频/MiniMax H3 文生视频_2084489178611539970.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `KSamplerSelect`
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `RHMiniMaxH3DecodeAV` —— 1/2 个有
- `RHMiniMaxH3DirectModelLoader` —— 1/2 个有
- `RHMiniMaxH3DirectTextEncoderLoader` —— 1/2 个有
- `RHMiniMaxH3DirectVAELoader` —— 1/2 个有
- `RHMiniMaxH3DualSigmaSampler` —— 1/2 个有
- `RHMiniMaxH3EmptyAVLatent` —— 1/2 个有
- `RHMiniMaxH3T2VATarget` —— 1/2 个有
- `RHMiniMaxH3T2VATextEncode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
