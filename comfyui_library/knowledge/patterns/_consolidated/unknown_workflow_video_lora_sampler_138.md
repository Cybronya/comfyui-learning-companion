---
name: unknown_workflow_video_lora_sampler_138
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.613308
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/动作迁移-SteadyDancer-无限时长生成_2002209657114509313.json, 图片生成/图生图/动作迁移_真人_二次元_Q版-跳舞、带货、口播-SteadyDancer_1999364272306126850.json, 图片生成/图生图/最新SteadyDancer动作迁移美女跳舞_1996553985236549634.json, 图片生成/文生图/动作舞蹈_骨骼迁移_不限时长版_2020834050457473026.json, 图片生成/文生图/腾讯最新开源SteadyDancer超完美动作迁移工作流_2006630138284351490.json, 数字人/数字人/最新SteadyDancer动作迁移动物美女舞蹈必备 超强一致性_1996288612700397569.json, 视频生成/图生视频/26年3月SteadyDancer_骨骼迁移_不限时长版_2032112165968154626.json, 视频生成/图生视频/SteadDancer （KJ版）视频姿势参考_1996519049599270913.json, 视频生成/图生视频/SteadDancer动作迁移_1996568841872351234.json, 视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移_1995783729840787458.json, 视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移，超级Nice!好用到爆!_2039879176072732673.json, 视频生成/图生视频/SteadDancer自适应骨骼绑定动作迁移，超级Nice!好用到爆!_2046114909657763841.json, 视频生成/图生视频/SteadDancer视频姿势参考（KJ）_1996528847946399745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_138

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/动作迁移-SteadyDancer-无限时长生成_2002209657114509313.json、图片生成/图生图/动作迁移_真人_二次元_Q版-跳舞、带货、口播-SteadyDancer_1999364272306126850.json、图片生成/图生图/最新SteadyDancer动作迁移美女跳舞_1996553985236549634.json、图片生成/文生图/动作舞蹈_骨骼迁移_不限时长版_2020834050457473026.json、图片生成/文生图/腾讯最新开源SteadyDancer超完美动作迁移工作流_2006630138284351490.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 13 个 workflow 都包含：
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 12/13 个有
- `WanVideoScheduler` —— 12/13 个有
- `WanVideoSetLoRAs` —— 12/13 个有
- `WanVideoTextEncodeCached` —— 12/13 个有
- `WanVideoBlockSwap` —— 11/13 个有
- `DrawViTPose` —— 9/13 个有
- `PoseAndFaceDetection` —— 9/13 个有
- `WanVideoSetBlockSwap` —— 9/13 个有
- `WanVideoTorchCompileSettings` —— 9/13 个有
- `INTConstant` —— 6/13 个有
- `Int` —— 6/13 个有
- `PreviewImage` —— 6/13 个有
- `PoseDetectionOneToAllAnimation` —— 4/13 个有
- `CR Prompt Text` —— 3/13 个有
- `TextInput_` —— 3/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `AddLabel` —— 1/13 个有
- `Anything Everywhere3` —— 1/13 个有
- `ImageConcanate` —— 1/13 个有
- `ImpactInt` —— 1/13 个有
- `LoadWanVideoT5TextEncoder` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有
- `PrimitiveFloat` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有
- `ToFloat` —— 1/13 个有
- `WanVideoTextEncode` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有
- `easy convertAnything` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
