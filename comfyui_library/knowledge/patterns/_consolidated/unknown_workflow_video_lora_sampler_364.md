---
name: unknown_workflow_video_lora_sampler_364
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.749167
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/steady dancer卡通动物动作漫剧电商服装分镜真人_2072526167571263489.json, 视频生成/图生视频/漫剧舞蹈动作迁移1_2077308268699021313.json, 视频生成/文生视频/SteadyDancer+SDpose一张人物照片 + 一段姿态（骨架）_1995841055381762050.json, 视频生成/文生视频/SteadyDancer视频风格化转绘_1998364456965038082.json, 视频生成/文生视频/kj新Pose Detection +SteadyDancer_1998291780594491394.json, 视频生成/文生视频/卡通人物跳舞_2010624770362052610.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_364

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/steady dancer卡通动物动作漫剧电商服装分镜真人_2072526167571263489.json、视频生成/图生视频/漫剧舞蹈动作迁移1_2077308268699021313.json、视频生成/文生视频/SteadyDancer+SDpose一张人物照片 + 一段姿态（骨架）_1995841055381762050.json、视频生成/文生视频/SteadyDancer视频风格化转绘_1998364456965038082.json、视频生成/文生视频/kj新Pose Detection +SteadyDancer_1998291780594491394.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
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
- `PreviewImage` —— 5/6 个有
- `WanVideoScheduler` —— 5/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `SDPoseOODLoader` —— 4/6 个有
- `SDPoseOODProcessor` —— 4/6 个有
- `YOLOModelLoader` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `DF_Int_to_Float` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `Int` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `OnnxDetectionModelLoader` —— 2/6 个有
- `PoseDetectionOneToAllAnimation` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `easy indexAnything` —— 2/6 个有
- `easy mathInt` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `DWPreprocessor` —— 1/6 个有
- `DrawViTPose` —— 1/6 个有
- `JWInteger` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `PoseAndFaceDetection` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `ZML_AnyTypeSwitchFive` —— 1/6 个有
- `ttN float` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
