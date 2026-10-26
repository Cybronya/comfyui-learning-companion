---
name: unknown_workflow_video_lora_sampler_151
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.60875
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, SetNode, VHS_LoadVideo, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/11dongzuoqianyi(gai1)_2055210834040770561.json, 图片生成/反推提示词/11yjqyyh_2054451210467454978.json, 图片生成/图生图/SteadyDancer动作迁移-_2043535021054627841.json, 图片生成/图生图/SteadyDancer（最强骨骼迁移）_1995352234491883521.json, 图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json, 视频生成/图生视频/SteadDancer动作迁移_2017466618615439361.json, 视频生成/图生视频/SteadDancer动作迁移（支持动漫人物）长视频一致性加强版_2011405479620124674.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_1995844904171495425.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_2061068385760399361.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_2062090699058798593.json, 视频生成/图生视频/SteadyDancer（最强骨骼迁移）_2068716358623391746.json, 视频生成/图生视频/【橘子AI】SteadyDancer（百搭骨骼迁移）_1995725668220538882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_151

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/反推提示词/11dongzuoqianyi(gai1)_2055210834040770561.json、图片生成/反推提示词/11yjqyyh_2054451210467454978.json、图片生成/图生图/SteadyDancer动作迁移-_2043535021054627841.json、图片生成/图生图/SteadyDancer（最强骨骼迁移）_1995352234491883521.json、图片生成/图生图/wanvideo_SteadyDancer_1997203294399447042.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 12 个 workflow 都包含：
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
- `GetNode` —— 11/12 个有
- `Int` —— 11/12 个有
- `VHS_VideoCombine` —— 11/12 个有
- `SimpleMath+` —— 10/12 个有
- `CR Text` —— 9/12 个有
- `GetImageSizeAndCount` —— 9/12 个有
- `WanVideoSetBlockSwap` —— 9/12 个有
- `WanVideoTorchCompileSettings` —— 9/12 个有
- `DrawViTPose` —— 7/12 个有
- `PoseAndFaceDetection` —— 7/12 个有
- `Anything Everywhere` —— 6/12 个有
- `ImageUpscaleWithModelBatched` —— 6/12 个有
- `RIFE VFI` —— 6/12 个有
- `RunningHub Deepcleaner` —— 6/12 个有
- `UpscaleModelLoader` —— 6/12 个有
- `ImageConcatMulti` —— 5/12 个有
- `PoseDetectionOneToAllAnimation` —— 5/12 个有
- `Fast Groups Muter (rgthree)` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `PrimitiveFloat` —— 3/12 个有
- `PrimitiveInt` —— 3/12 个有
- `CR Prompt Text` —— 2/12 个有
- `CreateVideo` —— 2/12 个有
- `SaveVideo` —— 2/12 个有
- `Label (rgthree)` —— 1/12 个有
- `SDPoseOODLoader` —— 1/12 个有
- `SDPoseOODProcessor` —— 1/12 个有
- `VHS_VideoInfoSource` —— 1/12 个有
- `YOLOModelLoader` —— 1/12 个有
- `easy convertAnything` —— 1/12 个有
- `easy mathInt` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
