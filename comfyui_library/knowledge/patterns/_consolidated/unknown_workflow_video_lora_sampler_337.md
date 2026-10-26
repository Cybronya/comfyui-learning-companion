---
name: unknown_workflow_video_lora_sampler_337
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.722286
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/SCAIL动作迁移：多人同框互动迁移_2013194857988235266.json, 数字人/数字人/SCAIL多人_单人--动作迁移_2001571883931824129.json, 数字人/数字人/SCAIL视频姿势参考支持多人_2019650977418186753.json, 数字人/数字人/Scail 一键跳舞！骨骼完美驱动！_2003096928302899201.json, 数字人/数字人/动作迁移-SCAIL_2000447654070976513.json, 数字人/数字人/萌宠跳舞-动作运镜最强迁移-SCAIL_3D单人多人姿态驱动+自动对齐骨骼+镜头控制+人物360旋转_2019072391724408834.json, 数字人/数字人/视频-动作迁移单人-wan2.1-SCAIL-KJ_2011817884372180993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_337

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/SCAIL动作迁移：多人同框互动迁移_2013194857988235266.json、数字人/数字人/SCAIL多人_单人--动作迁移_2001571883931824129.json、数字人/数字人/SCAIL视频姿势参考支持多人_2019650977418186753.json、数字人/数字人/Scail 一键跳舞！骨骼完美驱动！_2003096928302899201.json、数字人/数字人/动作迁移-SCAIL_2000447654070976513.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadNLFModel` —— 6/7 个有
- `GetNode` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `WanVideoEncode` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `WanVideoUni3C_ControlnetLoader` —— 6/7 个有
- `WanVideoUni3C_embeds` —— 6/7 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 5/7 个有
- `DWPreprocessor` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `LoadWanVideoT5TextEncoder` —— 5/7 个有
- `WanVideoTextEncode` —— 5/7 个有
- `FloatConstant` —— 4/7 个有
- `PreviewImage` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `ImageFromBatch+` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `VHS_VideoInfoLoaded` —— 2/7 个有
- `WanVideoTextEncodeCached` —— 2/7 个有
- `easy anythingIndexSwitch` —— 2/7 个有
- `easy int` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `CM_IntToFloat` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `CustomAddLabel` —— 1/7 个有
- `Florence2ModelLoader` —— 1/7 个有
- `Florence2Run` —— 1/7 个有
- `ImageFromBatch` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `Int` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LoadNLFModel` —— 1/7 个有
- `Manual XY Entry Info` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `SimpleCalculatorKJ` —— 1/7 个有
- `easy positive` —— 1/7 个有
- `easy seed` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
