---
name: unknown_workflow_video_sampler_vae_194
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/大融合参考生视频 FusionX Phantom_1934266814887063554.json, 视频生成/文生视频/Wan2.1 最新 FusionX 电商模特主播讲解产品视频 风格一致性_1943186431659425794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_194

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/大融合参考生视频 FusionX Phantom_1934266814887063554.json、视频生成/文生视频/Wan2.1 最新 FusionX 电商模特主播讲解产品视频 风格一致性_1943186431659425794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 1/2 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/2 个有
- `WanVideoApplyNAG` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTextEncodeSingle` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
