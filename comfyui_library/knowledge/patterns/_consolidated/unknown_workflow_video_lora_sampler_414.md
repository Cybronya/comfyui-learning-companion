---
name: unknown_workflow_video_lora_sampler_414
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5104
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan Animate2.2动作迁移V3(Move) 骨骼增强版_2073292954780917762.json, 视频生成/图生视频/Wan Animate2.2动作迁移_1969366584278085634.json, 视频生成/图生视频/Wan-Animate动作表情迁移不遮罩_1968169520768647170.json, 视频生成/图生视频/Wan2.2 Animate人物动作+表情迁移_1972599286972231682.json, 视频生成/图生视频/animate动作参考_1993657124511219713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_414

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan Animate2.2动作迁移V3(Move) 骨骼增强版_2073292954780917762.json、视频生成/图生视频/Wan Animate2.2动作迁移_1969366584278085634.json、视频生成/图生视频/Wan-Animate动作表情迁移不遮罩_1968169520768647170.json、视频生成/图生视频/Wan2.2 Animate人物动作+表情迁移_1972599286972231682.json、视频生成/图生视频/animate动作参考_1993657124511219713.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
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
- `DWPreprocessor` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `PixelPerfectResolution` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `FaceMaskFromPoseKeypoints` —— 3/5 个有
- `ImageCropByMaskAndResize` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `EmptyImage` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `OnnxDetectionModelLoader` —— 2/5 个有
- `PoseAndFaceDetection` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GIMMVFI_interpolate` —— 1/5 个有
- `Int` —— 1/5 个有
- `PlaySound|pysssss` —— 1/5 个有
- `PoseDetectionOneToAllAnimation` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `Switch image [Crystools]` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有
- `VHS_VideoInfoLoaded` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
