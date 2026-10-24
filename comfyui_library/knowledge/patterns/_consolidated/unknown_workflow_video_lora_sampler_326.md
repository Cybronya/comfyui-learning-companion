---
name: unknown_workflow_video_lora_sampler_326
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.798
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/新Wan2.2 Animate-动作迁移_1983713271683457025.json, 视频生成/图生视频/男用动作迁移复制一键跳舞Wan2.2-Animate-视频动作迁移_2067576219452919809.json, 视频生成/图生视频/美女图片生成跳舞视频_1975800896795881473.json, 视频生成/图生视频/美女跳舞视频复刻_1975790920316620801.json, 视频生成/图生视频/表哥超级画质动作复刻V2.1_2002002967475699713.json, 视频生成/图生视频/超稳定！wan2.2超清图片跳舞，动作复刻-动作表情口型_1991126725268471809.json, 视频生成/文生视频/Wan2.2 Animate美女图片跳舞 视频动作迁移_1970282441866964994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_326

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/新Wan2.2 Animate-动作迁移_1983713271683457025.json、视频生成/图生视频/男用动作迁移复制一键跳舞Wan2.2-Animate-视频动作迁移_2067576219452919809.json、视频生成/图生视频/美女图片生成跳舞视频_1975800896795881473.json、视频生成/图生视频/美女跳舞视频复刻_1975790920316620801.json、视频生成/图生视频/表哥超级画质动作复刻V2.1_2002002967475699713.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
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
- `GetNode` —— 5/7 个有
- `SetNode` —— 5/7 个有
- `Text` —— 5/7 个有
- `WanVideoAnimateEmbeds` —— 5/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `LayerUtility: PurgeVRAM` —— 3/7 个有
- `VHS_VideoInfo` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `VHS_VideoInfoLoaded` —— 2/7 个有
- `easy seed` —— 2/7 个有
- `SaveImage` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
