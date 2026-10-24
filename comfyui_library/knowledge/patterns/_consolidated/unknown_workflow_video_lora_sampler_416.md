---
name: unknown_workflow_video_lora_sampler_416
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5572
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan-Animate-KJ工作流（自动遮罩）_1970452175312875521.json, 视频生成/图生视频/WanAnimateV2-人物编辑_1975882698759737345.json, 视频生成/图生视频/WanAnimate_V2_视频人物自动替换(单人)_2006252507227496450.json, 视频生成/图生视频/WanAnimate_V2_视频动作迁移(单人)_2006246424253571074.json, 视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_416

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan-Animate-KJ工作流（自动遮罩）_1970452175312875521.json、视频生成/图生视频/WanAnimateV2-人物编辑_1975882698759737345.json、视频生成/图生视频/WanAnimate_V2_视频人物自动替换(单人)_2006252507227496450.json、视频生成/图生视频/WanAnimate_V2_视频动作迁移(单人)_2006246424253571074.json、视频生成/图生视频/wan2.2 animate视频换头视频换脸工作流_1977864752590454786.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
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
- `DrawViTPose` —— 4/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/5 个有
- `GIMMVFI_interpolate` —— 3/5 个有
- `GrowMaskWithBlur` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `LayerUtility: PurgeVRAM V2` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `GrowMask` —— 2/5 个有
- `ImageBlend` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `WanVideoContextOptions` —— 2/5 个有
- `Bookmark (rgthree)` —— 1/5 个有
- `FloatConstant` —— 1/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `WanVideoExperimentalArgs` —— 1/5 个有
- `WanVideoSLG` —— 1/5 个有
- `WanVideoScheduler` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
