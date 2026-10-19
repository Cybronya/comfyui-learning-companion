---
name: unknown_workflow_video_lora_sampler_315
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.597143
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetImageSizeAndCount, GetNode, GrowMask, INTConstant, ImageResizeKJv2, LoadImage, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [LayerMask: MaskInvert]
members: [视频生成/图生视频/1970452175312875521.json, 视频生成/图生视频/1971495725483933698.json, 视频生成/文生视频/1974519641752080386.json, 视频生成/文生视频/1977718983715606530.json, 视频生成/文生视频/Wan-Animate+Sa2VA多人场景角色替换_1989959828757991425.json, 视频生成/文生视频/Wan-Animate-SecNodes角色替换_2072999489906188288.json, 视频生成/文生视频/Wan-Animate多人场景角色替换_2072999526493102080.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_315

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1970452175312875521.json、视频生成/图生视频/1971495725483933698.json、视频生成/文生视频/1974519641752080386.json、视频生成/文生视频/1977718983715606530.json、视频生成/文生视频/Wan-Animate+Sa2VA多人场景角色替换_1989959828757991425.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 7 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMask`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `PoseAndFaceDetection`
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
- `OnnxDetectionModelLoader` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `DrawViTPose` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 5/7 个有
- `Float` —— 5/7 个有
- `LayerMask: MaskInvert` —— 5/7 个有
- `PointsEditor` —— 5/7 个有
- `Setter` —— 5/7 个有
- `easy ifElse` —— 5/7 个有
- `DownloadAndLoadSAM2Model` —— 4/7 个有
- `Sam2Segmentation` —— 4/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `SeCModelLoader` —— 2/7 个有
- `SeCVideoSegmentation` —— 2/7 个有
- `DWPreprocessor` —— 1/7 个有
- `FloatConstant` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `ImageBlend` —— 1/7 个有
- `JWImageExtractFromBatch` —— 1/7 个有
- `LayerMask: SAM2VideoUltra` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `Sa2VANodeTpl` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `WanVideoExperimentalArgs` —— 1/7 个有
- `WanVideoSLG` —— 1/7 个有
- `WanVideoScheduler` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: MaskInvert
