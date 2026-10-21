---
name: unknown_workflow_video_lora_sampler_422
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8244
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1997886234179567618.json, 视频生成/图生视频/1998823321796009986.json, 视频生成/文生视频/SteadyDancer+SDpose一张人物照片 + 一段姿态（骨架）_1995841055381762050.json, 视频生成/文生视频/SteadyDancer一张人物照片 + 一段姿态（骨架） → 生成一个动作流畅、长得像、不抖的动画视频_1995759327522721794.json, 视频生成/文生视频/卡通人物跳舞_2010624770362052610.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_422

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1997886234179567618.json、视频生成/图生视频/1998823321796009986.json、视频生成/文生视频/SteadyDancer+SDpose一张人物照片 + 一段姿态（骨架）_1995841055381762050.json、视频生成/文生视频/SteadyDancer一张人物照片 + 一段姿态（骨架） → 生成一个动作流畅、长得像、不抖的动画视频_1995759327522721794.json、视频生成/文生视频/卡通人物跳舞_2010624770362052610.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 3/5 个有
- `OnnxDetectionModelLoader` —— 3/5 个有
- `SDPoseOODLoader` —— 3/5 个有
- `SDPoseOODProcessor` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `AILab_ImageStitch` —— 2/5 个有
- `Anything Everywhere3` —— 2/5 个有
- `DrawViTPose` —— 2/5 个有
- `FastUnsharpSharpen` —— 2/5 个有
- `ImageResize+` —— 2/5 个有
- `ImageUpscaleWithModel` —— 2/5 个有
- `PoseAndFaceDetection` —— 2/5 个有
- `PoseDetectionOneToAllAnimation` —— 2/5 个有
- `RIFE VFI` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有
- `WanVideoScheduler` —— 2/5 个有
- `YOLOModelLoader` —— 2/5 个有
- `GetNode` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `LayerColor: ColorAdapter` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `ZML_AnyTypeSwitchFive` —— 1/5 个有
- `ttN float` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
