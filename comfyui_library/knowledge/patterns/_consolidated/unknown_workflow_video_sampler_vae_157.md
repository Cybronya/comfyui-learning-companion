---
name: unknown_workflow_video_sampler_vae_157
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.701333
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageConcatMulti, ImageResizeKJ, InvertMask, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ColorPicker, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MaskPreview+, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1908558258645118978.json, 视频生成/图生视频/1922686919644430338.json, 视频生成/图生视频/1928687484622815233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_157

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1908558258645118978.json、视频生成/图生视频/1922686919644430338.json、视频生成/图生视频/1928687484622815233.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `InvertMask`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview+`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnything_V2` —— 2/3 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/3 个有
- `DownloadAndLoadSAM2Model` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImagePadKJ` —— 2/3 个有
- `InspyrenetRembg` —— 2/3 个有
- `Pick From Batch (mtb)` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `Sam2Segmentation` —— 2/3 个有
- `WanVideoVACEModelSelect` —— 2/3 个有
- `WanVideoVACEStartToEndFrame` —— 2/3 个有
- `easy imageScaleDownToSize` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
