---
name: unknown_workflow_video_lora_sampler_538
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.502
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/角色迁移组线下版+全节点注释_2055512810020458497.json, 视频生成/图生视频/首尾帧+角色替换 Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1994241547038375938.json, 视频生成/文生视频/Wan 2.2-动作迁移（Wan Animate版）_1969619629620555777.json, 视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_538

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/角色迁移组线下版+全节点注释_2055512810020458497.json、视频生成/图生视频/首尾帧+角色替换 Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1994241547038375938.json、视频生成/文生视频/Wan 2.2-动作迁移（Wan Animate版）_1969619629620555777.json、视频生成/文生视频/Wan-Animate​​角色动画 (Character Animation)_1969434671211814914.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
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
- `GetImageSizeAndCount` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `WanVideoLoraSelectMulti` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `Int` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetImageSize` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `LayerMask: LoadFlorence2Model` —— 1/4 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `WanVideoContextOptions` —— 1/4 个有
- `WanVideoLoraSelect` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
