---
name: unknown_workflow_video_lora_sampler_727
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.610667
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, INTConstant, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/animate动作参考_1993657124511219713.json, 视频生成/图生视频/wan2.2Animate美女跳舞工作流_2033057095406329858.json, 视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_727

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/animate动作参考_1993657124511219713.json、视频生成/图生视频/wan2.2Animate美女跳舞工作流_2033057095406329858.json、视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `INTConstant`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
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
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/3 个有
- `EmptyImage` —— 1/3 个有
- `GIMMVFI_interpolate` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `LayerMask: LoadFlorence2Model` —— 1/3 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
