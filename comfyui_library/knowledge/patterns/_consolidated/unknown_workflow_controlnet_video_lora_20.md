---
name: unknown_workflow_controlnet_video_lora_20
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.651857
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/视频编辑_动作迁移_多人_长视频_Scail_2002350987564183553.json, 平台全量/🕺丝滑动作迁移-SCAIL适配各种风格也适合双人🕺_2036317753467998209.json, 数字人/数字人/动作迁移-SCAIL_2000447654070976513.json, 视频生成/图生视频/044-SCAIL动作迁移3.0-适配各种风格-单双人均可25-12-16_2000835179973406721.json, 视频生成/图生视频/SCAIL 单人_双人，支持丝滑转身，Q版，动物等角色，支持不同构图_2007356620417798146.json, 视频生成/图生视频/SCAIL 多人动作迁移_2001530537791614977.json, 视频生成/图生视频/适配各种风格也适合双人动作迁移丝滑_2002389202262212609.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_20

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/视频编辑_动作迁移_多人_长视频_Scail_2002350987564183553.json、平台全量/🕺丝滑动作迁移-SCAIL适配各种风格也适合双人🕺_2036317753467998209.json、数字人/数字人/动作迁移-SCAIL_2000447654070976513.json、视频生成/图生视频/044-SCAIL动作迁移3.0-适配各种风格-单双人均可25-12-16_2000835179973406721.json、视频生成/图生视频/SCAIL 单人_双人，支持丝滑转身，Q版，动物等角色，支持不同构图_2007356620417798146.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `ImageConcatMulti` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `FloatConstant` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `WanVideoTorchCompileSettings` —— 4/7 个有
- `easy int` —— 4/7 个有
- `Fast Bypasser (rgthree)` —— 3/7 个有
- `INTConstant` —— 3/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/7 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 2/7 个有
- `DWPreprocessor` —— 2/7 个有
- `VHS_VideoInfoLoaded` —— 2/7 个有
- `CR SDXL Aspect Ratio` —— 1/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GIMMVFI_interpolate` —— 1/7 个有
- `ImageScaleBy` —— 1/7 个有
- `ImageScaleToMaxDimension` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SeedVR2LoadDiTModel` —— 1/7 个有
- `SeedVR2LoadVAEModel` —— 1/7 个有
- `SeedVR2VideoUpscaler` —— 1/7 个有
- `SimpleCalculatorKJ` —— 1/7 个有
- `WanVideoLoraSelectMulti` —— 1/7 个有
- `easy compare` —— 1/7 个有
- `easy ifElse` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
