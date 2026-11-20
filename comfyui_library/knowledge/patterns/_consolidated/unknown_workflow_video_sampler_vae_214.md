---
name: unknown_workflow_video_sampler_vae_214
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.943
common_nodes: [CR Prompt Text, CR Text, ColorMatch, Display Any (rgthree), GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMaskWithBlur, ImageBatchGet, ImageCompositeMasked, ImpactSwitch, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, MaskListToMaskBatch, MaskToImage, PreviewBridge, PrimitiveInt, SAMModelLoader (segment anything), SolidMask, VHS_DuplicateMasks, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/MinimaxRemove视频去水印（最新去水印，速度快）_1937673106788126722.json, 平台全量/MinimaxRemove视频去水印（最新去水印，速度快）_1977342516464898049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_214

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/MinimaxRemove视频去水印（最新去水印，速度快）_1937673106788126722.json、平台全量/MinimaxRemove视频去水印（最新去水印，速度快）_1977342516464898049.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CR Text`
- `ColorMatch`
- `Display Any (rgthree)`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMaskWithBlur`
- `ImageBatchGet`
- `ImageCompositeMasked`
- `ImpactSwitch`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `MaskListToMaskBatch`
- `MaskToImage`
- `PreviewBridge`
- `PrimitiveInt`
- `SAMModelLoader (segment anything)`
- `SolidMask`
- `VHS_DuplicateMasks`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
