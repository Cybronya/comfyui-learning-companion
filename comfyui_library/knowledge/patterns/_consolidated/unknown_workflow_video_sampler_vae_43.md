---
name: unknown_workflow_video_sampler_vae_43
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7123
common_nodes: [AddLabel, EmptyImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageConcatMulti, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVACEEncode, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/1927072484653223937.json, 视频生成/图生视频/1927172015592210434.json, 视频生成/图生视频/1922883836873510914.json, 视频生成/图生视频/1972511577779990529.json, 视频生成/图生视频/1922695812248387585.json, 视频生成/图生视频/1922711009637842946.json, 视频生成/图生视频/1988044304205680642.json, 视频生成/图生视频/1928697950808215553.json, 视频生成/图生视频/1934990691049086977.json, 视频生成/文生视频/1937481495915466754.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_43

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1927072484653223937.json、视频生成/图生视频/1927172015592210434.json、视频生成/图生视频/1922883836873510914.json、视频生成/图生视频/1972511577779990529.json、视频生成/图生视频/1922695812248387585.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 10 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 9/10 个有
- `ImageConcanate` —— 9/10 个有
- `ImagePadKJ` —— 9/10 个有
- `InpaintPreprocessor` —— 9/10 个有
- `LayerMask: LoadSegmentAnythingModels` —— 9/10 个有
- `LayerMask: SegmentAnythingUltra V3` —— 9/10 个有
- `MaskToImage` —— 9/10 个有
- `WanVideoVACEModelSelect` —— 9/10 个有
- `WanVideoVACEStartToEndFrame` —— 9/10 个有
- `Fast Groups Bypasser (rgthree)` —— 8/10 个有
- `WanVideoTeaCache` —— 8/10 个有
- `WanVideoTextEncode` —— 8/10 个有
- `MaskPreview+` —— 7/10 个有
- `ImageResizeKJv2` —— 6/10 个有
- `ImageBlend` —— 5/10 个有
- `DownloadAndLoadSAM2Model` —— 4/10 个有
- `PointsEditor` —— 4/10 个有
- `Sam2Segmentation` —— 4/10 个有
- `WanVideoTorchCompileSettings` —— 4/10 个有
- `ImageCompositeMasked` —— 3/10 个有
- `PreviewAnimation` —— 3/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `MaskPreview` —— 2/10 个有
- `VHS_VideoInfo` —— 2/10 个有
- `WanVideoApplyNAG` —— 2/10 个有
- `WanVideoTextEncodeSingle` —— 2/10 个有
- `ImageResize+` —— 1/10 个有
- `InvertMask` —— 1/10 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
