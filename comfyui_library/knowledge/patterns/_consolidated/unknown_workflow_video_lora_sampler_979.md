---
name: unknown_workflow_video_lora_sampler_979
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.521
common_nodes: [ACE_ImageFaceCrop, BlockifyMask, CLIPVisionLoader, CR Prompt Text, ClothesSegment, DrawMaskOnImage, EmptyImage, GetNode, GrowMask, ImageConcanate, ImageFromBatch, ImageResizeKJv2, JWInteger, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PoseRetargetPromptHelper, PreviewImage, PrimitiveInt, SeCModelLoader, SeCVideoSegmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/Wan Animate 视频多服装换装v1_1977304450215890945.json, 平台全量/Wan Animate+KJ_V2版+Sec遮罩_视频换装V1_1977375580100415489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_979

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Wan Animate 视频多服装换装v1_1977304450215890945.json、平台全量/Wan Animate+KJ_V2版+Sec遮罩_视频换装V1_1977375580100415489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 2 个 workflow 都包含：
- `ACE_ImageFaceCrop`
- `BlockifyMask`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ClothesSegment`
- `DrawMaskOnImage`
- `EmptyImage`
- `GetNode`
- `GrowMask`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PoseRetargetPromptHelper`
- `PreviewImage`
- `PrimitiveInt`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有
- `DrawViTPose` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `ImpactMakeImageBatch` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PDIMAGE_LongerSize` —— 1/2 个有
- `PixelPerfectResolution` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `easy batchAnything` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy imageCount` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
