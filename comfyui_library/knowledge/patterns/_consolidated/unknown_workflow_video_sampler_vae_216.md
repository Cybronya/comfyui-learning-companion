---
name: unknown_workflow_video_sampler_vae_216
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [BboxDetectorCombined_v2, GrowMaskWithBlur, ImageCompositeMasked, LayerUtility: ImageScaleByAspectRatio V2, MaskListToMaskBatch, MaskToImage, SolidMask, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [平台全量/视频自动去水印MiniMaxRemover万相去水印_1948383625489317890.json, 视频生成/图生视频/动态水印 去除  自用_2034226640116518914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_216

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频自动去水印MiniMaxRemover万相去水印_1948383625489317890.json、视频生成/图生视频/动态水印 去除  自用_2034226640116518914.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `BboxDetectorCombined_v2`
- `GrowMaskWithBlur`
- `ImageCompositeMasked`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MaskListToMaskBatch`
- `MaskToImage`
- `SolidMask`
- `UltralyticsDetectorProvider`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ColorImage V2` —— 1/2 个有
- `LoadWanVideoT5TextEncoder` —— 1/2 个有
- `WanVideoEasyCache` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoSetRadialAttention` —— 1/2 个有
- `WanVideoTextEncode` —— 1/2 个有
- `WanVideoTextEncodeCached` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
