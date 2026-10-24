---
name: unknown_workflow_video_lora_sampler_94
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.6234
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/SteadyDancer动作迁移-_2043535021054627841.json, 图片生成/图生图/SteadyDancer（最强骨骼迁移）_1995352234491883521.json, 图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json, 图片生成/图生图/动作迁移-SteadyDancer-无限时长生成_2002209657114509313.json, 图片生成/图生图/动作迁移_真人_二次元_Q版-跳舞、带货、口播-SteadyDancer_1999364272306126850.json, 图片生成/图生图/最新SteadyDancer动作迁移美女跳舞_1996553985236549634.json, 图片生成/文生图/动作舞蹈_骨骼迁移_不限时长版_2020834050457473026.json, 图片生成/文生图/腾讯最新开源SteadyDancer超完美动作迁移工作流_2006630138284351490.json, 视频生成/图生视频/26年3月SteadyDancer_骨骼迁移_不限时长版_2032112165968154626.json, 视频生成/图生视频/SteadDancer （KJ版）视频姿势参考_1996519049599270913.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_1995844904171495425.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_2061068385760399361.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_2062090699058798593.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_2068716358623391746.json, 视频生成/图生视频/【橘子AI】SteadyDancer（百搭骨骼迁移）_1995725668220538882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_94

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/SteadyDancer动作迁移-_2043535021054627841.json、图片生成/图生图/SteadyDancer（最强骨骼迁移）_1995352234491883521.json、图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json、图片生成/图生图/动作迁移-SteadyDancer-无限时长生成_2002209657114509313.json、图片生成/图生图/动作迁移_真人_二次元_Q版-跳舞、带货、口播-SteadyDancer_1999364272306126850.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoScheduler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 14/15 个有
- `WanVideoBlockSwap` —— 13/15 个有
- `WanVideoSetBlockSwap` —— 12/15 个有
- `DrawViTPose` —— 10/15 个有
- `PoseAndFaceDetection` —— 10/15 个有
- `WanVideoTorchCompileSettings` —— 10/15 个有
- `ImageConcatMulti` —— 9/15 个有
- `SimpleMath+` —— 8/15 个有
- `Anything Everywhere` —— 6/15 个有
- `CR Text` —— 6/15 个有
- `ImageUpscaleWithModelBatched` —— 6/15 个有
- `PreviewImage` —— 6/15 个有
- `RIFE VFI` —— 6/15 个有
- `RunningHub Deepcleaner` —— 6/15 个有
- `UpscaleModelLoader` —— 6/15 个有
- `PoseDetectionOneToAllAnimation` —— 5/15 个有
- `CR Prompt Text` —— 4/15 个有
- `TextInput_` —— 3/15 个有
- `PrimitiveFloat` —— 2/15 个有
- `easy convertAnything` —— 2/15 个有
- `INTConstant` —— 1/15 个有
- `ImpactInt` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `SDPoseOODLoader` —— 1/15 个有
- `SDPoseOODProcessor` —— 1/15 个有
- `VHS_VideoInfoSource` —— 1/15 个有
- `YOLOModelLoader` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有
- `easy mathInt` —— 1/15 个有
- `easy showAnything` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
