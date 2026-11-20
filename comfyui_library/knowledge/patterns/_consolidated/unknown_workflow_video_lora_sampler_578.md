---
name: unknown_workflow_video_lora_sampler_578
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5124
common_nodes: [CLIPVisionLoader, GetNode, ImageConcatMulti, ImageResizeKJv2, JWInteger, LoadImage, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan Animate2.2动物主体替换_1976653610421567490.json, 平台全量/Wan Animate2.2只替换人脸_1971453832461008897.json, 平台全量/Wan Animate2.2只替换人脸_1989336407636406273.json, 平台全量/Wan Animate2.2替换主体和背景_1971588251523936257.json, 平台全量/Wan2.2 Animate高质量多人测试_1988538984588558337.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_578

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/Wan Animate2.2动物主体替换_1976653610421567490.json、平台全量/Wan Animate2.2只替换人脸_1971453832461008897.json、平台全量/Wan Animate2.2只替换人脸_1989336407636406273.json、平台全量/Wan Animate2.2替换主体和背景_1971588251523936257.json、平台全量/Wan2.2 Animate高质量多人测试_1988538984588558337.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `PreviewImage`
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
- `Anything Everywhere` —— 4/5 个有
- `BlockifyMask` —— 4/5 个有
- `CR Prompt Text` —— 4/5 个有
- `DrawMaskOnImage` —— 4/5 个有
- `GetImageSizeAndCount` —— 4/5 个有
- `ImageFromBatch+` —— 4/5 个有
- `Manual XY Entry Info` —— 4/5 个有
- `WanVideoEncode` —— 4/5 个有
- `WanVideoUni3C_ControlnetLoader` —— 4/5 个有
- `WanVideoUni3C_embeds` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `DWPreprocessor` —— 3/5 个有
- `FaceMaskFromPoseKeypoints` —— 3/5 个有
- `ImageCropByMaskAndResize` —— 3/5 个有
- `PixelPerfectResolution` —— 3/5 个有
- `APersonMaskGenerator` —— 2/5 个有
- `ApplyFaceProcessor` —— 2/5 个有
- `DrawViTPose` —— 2/5 个有
- `FaceProcessorLoader` —— 2/5 个有
- `LayerMask: MaskPreview` —— 2/5 个有
- `OnnxDetectionModelLoader` —— 2/5 个有
- `PointsEditor` —— 2/5 个有
- `PoseAndFaceDetection` —— 2/5 个有
- `SeCModelLoader` —— 2/5 个有
- `SeCVideoSegmentation` —— 2/5 个有
- `AnimalPosePreprocessor` —— 1/5 个有
- `BBoxesToSAM2` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `DownloadAndLoadQwenModel` —— 1/5 个有
- `GrowMask` —— 1/5 个有
- `ImageBatchGet` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerMask: SAM2VideoUltra` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `PoseRetargetPromptHelper` —— 1/5 个有
- `QwenVLDetection` —— 1/5 个有
- `RepeatImageBatch` —— 1/5 个有
- `Sam2VideoSegmentation` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
