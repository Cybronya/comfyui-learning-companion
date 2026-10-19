---
name: unknown_workflow_video_lora_sampler_66
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.610333
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, GetNode, GrowMask, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, SetNode, SimpleMath+, VHS_LoadVideo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2005855972839092225.json, 视频生成/图生视频/Animate Wan2.2 最强视频换头+换脸_2082828374803832834.json, 视频生成/图生视频/Animate Wan2.2 最强视频换头+换脸_2101148000168005634.json, 视频生成/图生视频/2005836350404395009.json, 视频生成/图生视频/2005891179520688129.json, 视频生成/图生视频/2009640204046442497.json, 视频生成/图生视频/2010983716067217410.json, 视频生成/图生视频/2014336980489871362.json, 视频生成/图生视频/1970833810306801666.json, 视频生成/图生视频/2041577855473160193.json, 视频生成/图生视频/2071227855530455041.json, 视频生成/图生视频/2009317533723136001.json, 视频生成/图生视频/2021386632020103169.json, 视频生成/图生视频/2041848671586750465.json, 视频生成/图生视频/2067973490745106434.json, 视频生成/图生视频/2073689074594050049.json, 视频生成/图生视频/2041849392579219457.json, 视频生成/图生视频/2041098212999700482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/2005855972839092225.json、视频生成/图生视频/Animate Wan2.2 最强视频换头+换脸_2082828374803832834.json、视频生成/图生视频/Animate Wan2.2 最强视频换头+换脸_2101148000168005634.json、视频生成/图生视频/2005836350404395009.json、视频生成/图生视频/2005891179520688129.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 18 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch+` —— 17/18 个有
- `VHS_VideoCombine` —— 17/18 个有
- `WanVideoLoraSelectMulti` —— 17/18 个有
- `Audio Duration (mtb)` —— 16/18 个有
- `GetImageRangeFromBatch` —— 16/18 个有
- `JWInteger` —— 16/18 个有
- `PrimitiveInt` —— 16/18 个有
- `easy cleanGpuUsed` —— 16/18 个有
- `easy sam3ModelLoader` —— 16/18 个有
- `easy sam3VideoSegmentation` —— 16/18 个有
- `DownloadAndLoadGIMMVFIModel` —— 15/18 个有
- `GIMMVFI_interpolate` —— 15/18 个有
- `Int` —— 15/18 个有
- `JjkText` —— 14/18 个有
- `MaskToImage` —— 12/18 个有
- `CM_IntToFloat` —— 6/18 个有
- `VHS_VideoInfo` —— 4/18 个有
- `WanVideoTorchCompileSettings` —— 4/18 个有
- `easy showAnything` —— 4/18 个有
- `ImageConcatMulti` —— 2/18 个有
- `LayerMask: LoadSegmentAnythingModels` —— 2/18 个有
- `LayerMask: SegmentAnythingUltra V3` —— 2/18 个有
- `Text` —— 2/18 个有
- `AutoCropFaces` —— 1/18 个有
- `AutoNegativePrompt` —— 1/18 个有
- `FlashVSRNode` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `RHHiddenNodes` —— 1/18 个有
- `RIFE VFI` —— 1/18 个有
- `SaveImage` —— 1/18 个有
- `TT_img_enc` —— 1/18 个有
- `TextOverlay` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
