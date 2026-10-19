---
name: unknown_workflow_video_lora_sampler_262
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.596375
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetNode, GrowMask, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, Int, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1970037279043579906.json, 视频生成/图生视频/1969961202665332737.json, 视频生成/图生视频/2034955430325129218.json, 视频生成/图生视频/1969228156349673474.json, 视频生成/图生视频/1969558465037410306.json, 视频生成/图生视频/1969378063396073473.json, 视频生成/图生视频/1969410370047799298.json, 视频生成/图生视频/1970135564894826498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_262

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1970037279043579906.json、视频生成/图生视频/1969961202665332737.json、视频生成/图生视频/2034955430325129218.json、视频生成/图生视频/1969228156349673474.json、视频生成/图生视频/1969558465037410306.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 8 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `Int`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 7/8 个有
- `LayerMask: LoadSegmentAnythingModels` —— 7/8 个有
- `LayerMask: SegmentAnythingUltra V3` —— 7/8 个有
- `MathExpression|pysssss` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `ImpactInt` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `Textbox` —— 6/8 个有
- `WanVideoContextOptions` —— 5/8 个有
- `easy showAnything` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetImageSizeAndCount` —— 1/8 个有
- `MaskToImage` —— 1/8 个有
- `PixelPerfectResolution` —— 1/8 个有
- `PointsEditor` —— 1/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `VHS_VideoInfo` —— 1/8 个有
- `VHS_VideoInfoLoaded` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy sam3GetObjectMask` —— 1/8 个有
- `easy sam3ModelLoader` —— 1/8 个有
- `easy sam3VideoSegmentation` —— 1/8 个有
- `easy sam3Visualization` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
