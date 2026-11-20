---
name: unknown_workflow_video_lora_sampler_393
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.589375
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, FaceMaskFromPoseKeypoints, GetImageSizeAndCount, INTConstant, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, PointsEditor, Sam2Segmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2-Animate局部重绘+视频转绘_1969957827202719745.json, 视频生成/图生视频/动作迁移_2017571137424723969.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042478976223940610.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042488839909937154.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2044301999423889409.json, 视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2047561888975822849.json, 视频生成/图生视频/最新WanAnimate之视频换装_1971421860208558082.json, 视频生成/图生视频/角色替换+动作参考_2000210160024944641.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_393

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/wan2.2-Animate局部重绘+视频转绘_1969957827202719745.json、视频生成/图生视频/动作迁移_2017571137424723969.json、视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042478976223940610.json、视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2042488839909937154.json、视频生成/图生视频/图生视频----WanAnimate角色替换+动作参考_2044301999423889409.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 8 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `FaceMaskFromPoseKeypoints`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `PointsEditor`
- `Sam2Segmentation`
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
- `AudioCropProcessUTK` —— 7/8 个有
- `GetImageRangeFromBatch` —— 7/8 个有
- `GetNode` —— 7/8 个有
- `GrowMask` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `WanVideoContextOptions` —— 6/8 个有
- `CM_IntToFloat` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `Fast Bypasser (rgthree)` —— 1/8 个有
- `GrowMaskWithBlur` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `Int` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/8 个有
- `Switch any [Crystools]` —— 1/8 个有
- `Text` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
