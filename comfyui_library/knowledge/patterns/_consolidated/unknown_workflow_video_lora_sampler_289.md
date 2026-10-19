---
name: unknown_workflow_video_lora_sampler_289
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.759625
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1983713271683457025.json, 视频生成/图生视频/2067576219452919809.json, 视频生成/图生视频/1975800896795881473.json, 视频生成/图生视频/1975790920316620801.json, 视频生成/图生视频/2002002967475699713.json, 视频生成/图生视频/1991126725268471809.json, 视频生成/文生视频/1969619629620555777.json, 视频生成/文生视频/1970282441866964994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_289

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1983713271683457025.json、视频生成/图生视频/2067576219452919809.json、视频生成/图生视频/1975800896795881473.json、视频生成/图生视频/1975790920316620801.json、视频生成/图生视频/2002002967475699713.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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
- `GetNode` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `WanVideoAnimateEmbeds` —— 6/8 个有
- `Text` —— 5/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `ImageConcatMulti` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `LayerUtility: PurgeVRAM` —— 3/8 个有
- `VHS_VideoInfo` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `RHHiddenNodes` —— 2/8 个有
- `VHS_VideoInfoLoaded` —— 2/8 个有
- `easy seed` —— 2/8 个有
- `Int` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `TT_img_enc` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
