---
name: unknown_workflow_video_lora_sampler_284
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.54925
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMask, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: [CR Prompt Text, easy promptConcat]
members: [视频生成/图生视频/2020513230719815681.json, 视频生成/文生视频/1971474322126782465.json, 视频生成/文生视频/1974413564041670657.json, 视频生成/文生视频/1974415771805855745.json, 视频生成/文生视频/1974423112462766082.json, 视频生成/文生视频/1974430400560893954.json, 视频生成/文生视频/1969371914298925058.json, 视频生成/文生视频/1969373357202436097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_284

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2020513230719815681.json、视频生成/文生视频/1971474322126782465.json、视频生成/文生视频/1974413564041670657.json、视频生成/文生视频/1974415771805855745.json、视频生成/文生视频/1974423112462766082.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 8 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 7/8 个有
- `ImageConcatMulti` —— 7/8 个有
- `Sam2Segmentation` —— 7/8 个有
- `WanVideoContextOptions` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `CR Prompt Text` —— 6/8 个有
- `DrawViTPose` —— 6/8 个有
- `JWInteger` —— 6/8 个有
- `OnnxDetectionModelLoader` —— 6/8 个有
- `PoseAndFaceDetection` —— 6/8 个有
- `WanVideoEncode` —— 6/8 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/8 个有
- `WanVideoUni3C_embeds` —— 6/8 个有
- `PointsEditor` —— 5/8 个有
- `ACE_ImageFaceCrop` —— 4/8 个有
- `PoseRetargetPromptHelper` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `DWPreprocessor` —— 2/8 个有
- `EmptyImage` —— 2/8 个有
- `FaceMaskFromPoseKeypoints` —— 2/8 个有
- `INTConstant` —— 2/8 个有
- `ImageBlend` —— 2/8 个有
- `ImageCropByMaskAndResize` —— 2/8 个有
- `PixelPerfectResolution` —— 2/8 个有
- `RH_Captioner` —— 2/8 个有
- `ShowText` —— 2/8 个有
- `easy promptConcat` —— 2/8 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `FloatConstant` —— 1/8 个有
- `GIMMVFI_interpolate` —— 1/8 个有
- `ImageRemoveBackground+` —— 1/8 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/8 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RemBGSession+` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、easy promptConcat
