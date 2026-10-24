---
name: unknown_workflow_video_lora_sampler_66
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.718263
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, VHS_LoadVideo, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_2003025271127175169.json, 视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_uni3c_2003035793427972097.json, 视频生成/图生视频/【遇见AI】SCAIL-Pose姿势迁移，支持丝滑转身，支持双人对打_2000492359223832578.json, 视频生成/图生视频/一键SCAIL多只宠物跳舞_2014755319490023425.json, 视频生成/图生视频/一键“疯狂的鸽子舞”图片跳舞！B站艾橘溪！_2012769463266975745.json, 视频生成/图生视频/一键生成_海豹舞_图片跳舞！_2019406882007425026.json, 视频生成/图生视频/一键生成_海豹舞_图片跳舞！人物模仿海豹跳舞！艾橘溪_2011467663087771649.json, 视频生成/图生视频/丝滑动作迁移-SCAIL无限人数版_2001543214261780482.json, 视频生成/图生视频/人物模仿海豹跳舞一键生成_图生视频_2022325838447910913.json, 视频生成/图生视频/动作迁移-丝滑转身-SCAIL_2001524857722531841.json, 视频生成/图生视频/单人动作迁移_2002405950176804865.json, 视频生成/图生视频/双人对打_2058542921317699585.json, 视频生成/图生视频/支持丝滑转身_2003660932444266497.json, 视频生成/图生视频/最新SCAIL动作迁移美女跳舞，支持双人对战_2000446117890359297.json, 视频生成/图生视频/最新SCAIL动作迁移美女跳舞，支持双人对战_2001125534966874113.json, 视频生成/图生视频/适配各种风格也适合双人动作迁移丝滑_2002389202262212609.json, 视频生成/图生视频/🕺丝滑动作迁移-SCAIL无限人数版🕺_2001377941516845057.json, 视频生成/图生视频/🕺丝滑动作迁移-SCAIL适配各种风格也适合双人🕺_2000762623283036162.json, 视频生成/文生视频/SCAIL 动物多人跳舞小猫小狗人物跳舞视频工作流 scaila 多人跳舞跨物种舞蹈模仿单人跳舞_2015990564986036225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_2003025271127175169.json、视频生成/图生视频/wanvideo_SCAIL_pose_control_two_charactors_uni3c_2003035793427972097.json、视频生成/图生视频/【遇见AI】SCAIL-Pose姿势迁移，支持丝滑转身，支持双人对打_2000492359223832578.json、视频生成/图生视频/一键SCAIL多只宠物跳舞_2014755319490023425.json、视频生成/图生视频/一键“疯狂的鸽子舞”图片跳舞！B站艾橘溪！_2012769463266975745.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_LoadVideo`
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
- `GetImageSizeAndCount` —— 18/19 个有
- `WanVideoEncode` —— 18/19 个有
- `WanVideoUni3C_ControlnetLoader` —— 18/19 个有
- `WanVideoUni3C_embeds` —— 18/19 个有
- `NLFPredict` —— 17/19 个有
- `OnnxDetectionModelLoader` —— 17/19 个有
- `PoseDetectionVitPoseToDWPose` —— 17/19 个有
- `RenderNLFPoses` —— 17/19 个有
- `DownloadAndLoadNLFModel` —— 16/19 个有
- `LoadWanVideoT5TextEncoder` —— 16/19 个有
- `SimpleMath+` —— 16/19 个有
- `WanVideoTextEncode` —— 16/19 个有
- `GetNode` —— 15/19 个有
- `SetNode` —— 15/19 个有
- `VHS_VideoCombine` —— 15/19 个有
- `FloatConstant` —— 13/19 个有
- `INTConstant` —— 12/19 个有
- `ImageConcatMulti` —— 12/19 个有
- `WanVideoTorchCompileSettings` —— 9/19 个有
- `CR Text` —— 7/19 个有
- `easy int` —— 6/19 个有
- `easy cleanGpuUsed` —— 5/19 个有
- `AudioToPath` —— 4/19 个有
- `Float to Int` —— 4/19 个有
- `OverlayVideos` —— 4/19 个有
- `PrimitiveFloat` —— 4/19 个有
- `PrimitiveInt` —— 4/19 个有
- `SaveVideo` —— 4/19 个有
- `VideoToPath` —— 4/19 个有
- `WanVideoTextEncodeCached` —— 3/19 个有
- `Bookmark (rgthree)` —— 2/19 个有
- `Fast Bypasser (rgthree)` —— 2/19 个有
- `MemoryCleaner` —— 2/19 个有
- `Mute / Bypass Repeater (rgthree)` —— 2/19 个有
- `Note Plus (mtb)` —— 2/19 个有
- `Int` —— 1/19 个有
- `LoadNLFModel` —— 1/19 个有
- `Seed` —— 1/19 个有
- `SimpleCalculatorKJ` —— 1/19 个有
- `WanVideoLoraSelectMulti` —— 1/19 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
