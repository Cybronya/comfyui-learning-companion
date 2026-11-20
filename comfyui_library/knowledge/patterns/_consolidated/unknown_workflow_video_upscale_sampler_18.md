---
name: unknown_workflow_video_upscale_sampler_18
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.774
common_nodes: [BboxDetectorCombined_v2, DuckHideNode, Fast Groups Bypasser (rgthree), FlashVSRNode, Float to Int, GrowMaskWithBlur, INTConstant, ImageCompositeMasked, ImageConcatMulti, ImageScaleToTotalPixels, JWInteger, LayerUtility: ColorImage V2, LayerUtility: ImageScaleByAspectRatio V2, MaskListToMaskBatch, MaskToImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, SolidMask, UltralyticsDetectorProvider, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [平台全量/视频修复水印去除整合包_2021881966093668353.json, 平台全量/视频修复水印去除整合包_2029108553381842945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_18

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频修复水印去除整合包_2021881966093668353.json、平台全量/视频修复水印去除整合包_2029108553381842945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `BboxDetectorCombined_v2`
- `DuckHideNode`
- `Fast Groups Bypasser (rgthree)`
- `FlashVSRNode`
- `Float to Int`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageCompositeMasked`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `JWInteger`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MaskListToMaskBatch`
- `MaskToImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy imageBatchToImageList`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
