---
name: unknown_workflow_video_lora_sampler_249
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6376
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, SetNode, VHS_LoadVideo, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/11dongzuoqianyi(gai1)_2055210834040770561.json, 图片生成/反推提示词/11yjqyyh_2054451210467454978.json, 图片生成/图生图/SteadyDancer动作迁移-_2043535021054627841.json, 图片生成/图生图/SteadyDancer（最强骨骼迁移）_1995352234491883521.json, 图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_1995844904171495425.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_2061068385760399361.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_2062090699058798593.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_2068716358623391746.json, 视频生成/图生视频/【橘子AI】SteadyDancer（百搭骨骼迁移）_1995725668220538882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_249

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/11dongzuoqianyi(gai1)_2055210834040770561.json、图片生成/反推提示词/11yjqyyh_2054451210467454978.json、图片生成/图生图/SteadyDancer动作迁移-_2043535021054627841.json、图片生成/图生图/SteadyDancer（最强骨骼迁移）_1995352234491883521.json、图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `SetNode`
- `VHS_LoadVideo`
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
- `WanVideoScheduler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 9/10 个有
- `GetNode` —— 9/10 个有
- `Int` —— 9/10 个有
- `VHS_VideoCombine` —— 9/10 个有
- `WanVideoSetBlockSwap` —— 9/10 个有
- `SimpleMath+` —— 8/10 个有
- `CR Text` —— 7/10 个有
- `DrawViTPose` —— 7/10 个有
- `PoseAndFaceDetection` —— 7/10 个有
- `WanVideoTorchCompileSettings` —— 7/10 个有
- `Anything Everywhere` —— 6/10 个有
- `ImageUpscaleWithModelBatched` —— 6/10 个有
- `RIFE VFI` —— 6/10 个有
- `RunningHub Deepcleaner` —— 6/10 个有
- `UpscaleModelLoader` —— 6/10 个有
- `ImageConcatMulti` —— 3/10 个有
- `PoseDetectionOneToAllAnimation` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `CreateVideo` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `SaveVideo` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `SDPoseOODLoader` —— 1/10 个有
- `SDPoseOODProcessor` —— 1/10 个有
- `VHS_VideoInfoSource` —— 1/10 个有
- `YOLOModelLoader` —— 1/10 个有
- `easy convertAnything` —— 1/10 个有
- `easy mathInt` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
