---
name: unknown_workflow_video_upscale_latent_upscale_155
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [BasicGuider, CLIPLoader, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3LatentUpscaleBy32T8, PathchSageAttentionKJ, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/长视频_2096817182402502658.json, 视频生成/文生视频/（9.8）MiniMax H3 导演台全能工作流_2096955930675073026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_155

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/长视频_2096817182402502658.json、视频生成/文生视频/（9.8）MiniMax H3 导演台全能工作流_2096955930675073026.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3LatentUpscaleBy32T8`
- `PathchSageAttentionKJ`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `JZL_MiniMaxAssetManager` —— 1/2 个有
- `MiniMaxH3Director` —— 1/2 个有
- `MiniMaxH3DirectorRefine` —— 1/2 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/2 个有
- `MiniMaxH3SigmaShift` —— 1/2 个有
- `ModelAttentionBackend` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `XB_ReferenceAny` —— 1/2 个有
- `XB_Sage_BlockSwap` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
