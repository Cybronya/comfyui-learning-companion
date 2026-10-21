---
name: unknown_workflow_video_lora_sampler_806
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.508
common_nodes: [BBoxesToSAM2, BlockifyMask, CLIPVisionLoader, CR String To Number, DWPreprocessor, DownloadAndLoadQwenModel, DownloadAndLoadSAM2Model, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImagesFromBatchIndexed, GetNode, GrowMask, ImageConcatMulti, ImageCropByMaskAndResize, ImageFromBatch, ImageResizeKJv2, ImpactInt, ImpactSwitch, Int, LayerMask: SAM2VideoUltra, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, QwenVLDetection, Sam2Segmentation, SetNode, TextBoxNode_UTK, Textbox, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1969938728464621569.json, 视频生成/图生视频/1980181283542306818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_806

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1969938728464621569.json、视频生成/图生视频/1980181283542306818.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `BBoxesToSAM2`
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR String To Number`
- `DWPreprocessor`
- `DownloadAndLoadQwenModel`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `GrowMask`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImpactInt`
- `ImpactSwitch`
- `Int`
- `LayerMask: SAM2VideoUltra`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `QwenVLDetection`
- `Sam2Segmentation`
- `SetNode`
- `TextBoxNode_UTK`
- `Textbox`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Image Stitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
