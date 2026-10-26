---
name: unknown_workflow_video_sampler_vae_202
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.459
common_nodes: [Float, GetNode, ImpactSwitch, JWStringSplit, LoadWanVideoT5TextEncoder, PrimitiveString, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader, easy convertAnything]
problems: []
missing: []
members: [视频生成/文生视频/文生视频-FusionX_1942908050997207041.json, 视频生成/文生视频/文生视频-FusionX_1967512356920156162.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_202

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/文生视频-FusionX_1942908050997207041.json、视频生成/文生视频/文生视频-FusionX_1967512356920156162.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：46%

## 共有节点

全部 2 个 workflow 都包含：
- `Float`
- `GetNode`
- `ImpactSwitch`
- `JWStringSplit`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveString`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy convertAnything`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
