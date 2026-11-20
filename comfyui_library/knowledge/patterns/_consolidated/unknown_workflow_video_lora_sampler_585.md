---
name: unknown_workflow_video_lora_sampler_585
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6382
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GrowMask, ImageConcatMulti, ImageCropByMaskAndResize, ImageFromBatch, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/即梦4.0+主体替换WanAnimate_1983776120329936897.json, 视频生成/图生视频/KJ版【 主体替换 + 姿势参考 】 Wan2.2+Animate_1970037279043579906.json, 视频生成/图生视频/Nuash版-Wan Animation 数字人+视频人物替换_1969961202665332737.json, 视频生成/图生视频/Wan-Animate 完美复刻官方效果-调参升级版_1969938728464621569.json, 视频生成/图生视频/主体替换调参版本_转身_1980181283542306818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_585

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/即梦4.0+主体替换WanAnimate_1983776120329936897.json、视频生成/图生视频/KJ版【 主体替换 + 姿势参考 】 Wan2.2+Animate_1970037279043579906.json、视频生成/图生视频/Nuash版-Wan Animation 数字人+视频人物替换_1969961202665332737.json、视频生成/图生视频/Wan-Animate 完美复刻官方效果-调参升级版_1969938728464621569.json、视频生成/图生视频/主体替换调参版本_转身_1980181283542306818.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GrowMask`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
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
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `Int` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `WanVideoSetLoRAs` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `LayerMask: LoadSegmentAnythingModels` —— 3/5 个有
- `LayerMask: SegmentAnythingUltra V3` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `Textbox` —— 3/5 个有
- `VHS_VideoInfo` —— 3/5 个有
- `BBoxesToSAM2` —— 2/5 个有
- `CR String To Number` —— 2/5 个有
- `DownloadAndLoadQwenModel` —— 2/5 个有
- `DownloadAndLoadSAM2Model` —— 2/5 个有
- `GetImagesFromBatchIndexed` —— 2/5 个有
- `ImpactSwitch` —— 2/5 个有
- `LayerMask: SAM2VideoUltra` —— 2/5 个有
- `OnnxDetectionModelLoader` —— 2/5 个有
- `PoseAndFaceDetection` —— 2/5 个有
- `QwenVLDetection` —— 2/5 个有
- `Sam2Segmentation` —— 2/5 个有
- `TextBoxNode_UTK` —— 2/5 个有
- `WanVideoLoraSelect` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Image Stitch` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RH_Jimeng4_Image2Image` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `StringToInt` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
