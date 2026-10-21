---
name: unknown_workflow_video_lora_sampler_548
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.50425
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: [LayerMask: LoadFlorence2Model, LayerUtility: PurgeVRAM, LayerUtility: Florence2Image2Prompt]
members: [视频生成/图生视频/2055512810020458497.json, 视频生成/图生视频/1994241547038375938.json, 视频生成/文生视频/1969434671211814914.json, 视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_2072999562958381056.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_548

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2055512810020458497.json、视频生成/图生视频/1994241547038375938.json、视频生成/文生视频/1969434671211814914.json、视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_2072999562958381056.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `WanVideoLoraSelectMulti` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `JWInteger` —— 2/4 个有
- `LayerMask: LoadFlorence2Model` —— 2/4 个有
- `LayerUtility: Florence2Image2Prompt` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `WanVideoContextOptions` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `Int` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerMask: LoadFlorence2Model、LayerUtility: PurgeVRAM、LayerUtility: Florence2Image2Prompt
