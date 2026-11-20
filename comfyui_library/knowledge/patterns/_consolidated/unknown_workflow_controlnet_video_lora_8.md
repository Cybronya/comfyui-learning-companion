---
name: unknown_workflow_controlnet_video_lora_8
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.698615
common_nodes: [CLIPVisionLoader, DownloadAndLoadNLFModel, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, SimpleMath+, VHS_LoadVideo, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/bduck跳舞-升级版_2016000836404514818.json, 视频生成/图生视频/一键“疯狂的鸽子舞”图片跳舞！B站艾橘溪！_2012769463266975745.json, 视频生成/图生视频/一键生成_海豹舞_图片跳舞！_2019406882007425026.json, 视频生成/图生视频/一键生成_海豹舞_图片跳舞！人物模仿海豹跳舞！艾橘溪_2011467663087771649.json, 视频生成/图生视频/人物模仿海豹跳舞一键生成_图生视频_2022325838447910913.json, 视频生成/图生视频/单人动作迁移_2002405950176804865.json, 视频生成/图生视频/双人对打_2058542921317699585.json, 视频生成/图生视频/影视剧替换人物第二步：视频驱动图片（可多人）_2013510010877251586.json, 视频生成/图生视频/支持丝滑转身_2003660932444266497.json, 视频生成/图生视频/最新SCAIL动作迁移美女跳舞，支持双人对战_2001125534966874113.json, 视频生成/图生视频/🐱Scail模型-单双人视频动作迁移-言灵ru😼_2002394851083730946.json, 视频生成/图生视频/🕺丝滑动作迁移-SCAIL无限人数版🕺_2001377941516845057.json, 视频生成/图生视频/🕺丝滑动作迁移-SCAIL适配各种风格也适合双人🕺_2000762623283036162.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_8

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/bduck跳舞-升级版_2016000836404514818.json、视频生成/图生视频/一键“疯狂的鸽子舞”图片跳舞！B站艾橘溪！_2012769463266975745.json、视频生成/图生视频/一键生成_海豹舞_图片跳舞！_2019406882007425026.json、视频生成/图生视频/一键生成_海豹舞_图片跳舞！人物模仿海豹跳舞！艾橘溪_2011467663087771649.json、视频生成/图生视频/人物模仿海豹跳舞一键生成_图生视频_2022325838447910913.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 13 个 workflow 都包含：
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
- `SimpleMath+`
- `VHS_LoadVideo`
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
- `GetNode` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `INTConstant` —— 10/13 个有
- `VHS_VideoCombine` —— 9/13 个有
- `FloatConstant` —— 8/13 个有
- `ImageConcatMulti` —— 7/13 个有
- `WanVideoTorchCompileSettings` —— 6/13 个有
- `AudioToPath` —— 5/13 个有
- `Float to Int` —— 5/13 个有
- `OverlayVideos` —— 5/13 个有
- `PrimitiveFloat` —— 5/13 个有
- `PrimitiveInt` —— 5/13 个有
- `SaveVideo` —— 5/13 个有
- `VideoToPath` —— 5/13 个有
- `easy cleanGpuUsed` —— 5/13 个有
- `CR Text` —— 3/13 个有
- `easy int` —— 3/13 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 2/13 个有
- `DWPreprocessor` —— 2/13 个有
- `Note Plus (mtb)` —— 2/13 个有
- `PreviewImage` —— 2/13 个有
- `Fast Bypasser (rgthree)` —— 1/13 个有
- `ImpactSwitch` —— 1/13 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/13 个有
- `PrimitiveBoolean` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `Text` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
